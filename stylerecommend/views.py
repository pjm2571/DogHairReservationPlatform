from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from roboflow import Roboflow
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os

rf = Roboflow(api_key="EPMQtZ4ullm6HypfiWGV")
project = rf.workspace().project("final_project_yu")
model = project.version(2).model

hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')


# Create your views here.


def getStyleRecommend(request):
    return render(request, 'stylerecommend/recommendHair.html')


class calculateStyle(APIView):
    def get(self, request):
        return render(request, '')

    def post(self, request):
        imgSrc = request.data.get('imgSrc', None)
        predict_make(imgSrc)
        return Response(status=200, data=dict(message="업로드가 완료되었습니다."))


def load_and_preprocess_image(image_path):
    image = tf.image.decode_image(tf.io.read_file(image_path))
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, (320, 320))  # 이미지 크기 조정
    image = image[tf.newaxis, :]
    return image


def predict_make(my_img):
    predicted_class = model.predict(my_img, confidence=40).json()['predictions'][-1]['class_id']
    # class id  ['beagle', 'chihuahua', 'dober', 'object', 'pome']
    print(predicted_class)
    if predicted_class == 0:
        style_image_path = '../dog_pic/beagle/beagle2.jpeg'
    elif predicted_class == 1:
        style_image_path = '../dog_pic/chuiwa/chuiwa2.jpeg'
    elif predicted_class == 2:
        style_image_path = '../dog_pic/dober/dober2.jpeg'
    elif predicted_class == 3:
        style_image_path = '../dog_pic/malte/malte2.jpeg'
    elif predicted_class == 4:
        style_image_path = '../dog_pic/pome/pome2.jpeg'
    input_img = load_and_preprocess_image(my_img)
    style_img = load_and_preprocess_image(style_image_path)
    stylized_image = hub_model(tf.constant(input_img), tf.constant(style_img))[0]
    stylized_image = np.array(stylized_image)  # EagerTensor를 NumPy 배열로 변환합니다.
    stylized_image = stylized_image[0]  # 첫 번째 이미지를 선택합니다.
    tf.keras.utils.save_img(os.path.join(os.getcwd(), 'output_image.jpg'), stylized_image)
    print("style이미지 저장완료")
