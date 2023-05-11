from django.shortcuts import render

def boardlist(request):
    return render(request, 'boardlist/boardlist.html')
