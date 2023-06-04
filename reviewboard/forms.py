from django import forms
from .models import ReviewPost

class PostForm(forms.ModelForm):
    class Meta: #Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.
        model = ReviewPost 
        fields = ['title', 'content','imgfile']
        labels = {
            'title':'제목', 
            'content':'내용',
            'imgfile':''
        }
