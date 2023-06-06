from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from user.models import User
from .chatgpt import chat_with_gpt





@method_decorator(csrf_exempt, name='dispatch')
def chat_view(request):
    if request.method == 'POST':
        
           
        message = request.POST.get('message')
        print(f"Received message: {message}")
        
        # Process the message as needed
        response = chat_with_gpt(message,0)  # Call your chat_with_gpt function
        
        response_data = {
            'message': response
        }
        print(response_data)
        print(type(response_data['message']))
        my_list = response_data['message'].split('\n')
        
        print(my_list)
        print(type(my_list))

        
        
        return render(request, 'gptjango/gpt.html', {'result': my_list})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

def new_page(request):
    # 새로운 페이지의 동작 정의
    context = {}
    loginCheck = request.session.get('loginCheck', '')

    if loginCheck == '':
        context['loginCheck'] = False
        context['user'] = None
    else:
        context['loginCheck'] = True
        email = request.session['email']
        user = User.objects.filter(email=email).first()
        context['user'] = user

    return render(request, 'gptjango/gpt.html', context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

from django.http import JsonResponse

def solution(request):
    if request.method == 'POST':
        selected_answer = request.POST.get('selected_answer')  # Get the selected answer
        print(f"Received selected answer: {selected_answer}")
        # Process the selected answer and generate the solution
        solution = chat_with_gpt(selected_answer, 1)
        print(solution)
        solution_list = solution.split('\n')

        return JsonResponse({'solution': solution_list})  # Send the solution list as JSON response
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

