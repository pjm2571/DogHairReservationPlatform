from .models import FreePost
from .forms import PostForm
from django.utils import timezone
import datetime
from django.shortcuts import render, redirect, get_object_or_404

def freeboard_post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('freeboard_post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'freeboard/freeboard_post_edit.html', {'form': form})


def freeboard_post_list(request):
    posts = FreePost.objects.all()
    today = datetime.date.today()
    context = {'today': today, 'posts': posts}
    return render(request, 'freeboard/freeboard_post_list.html', context)

def freeboard_post_detail(request, pk):
    post = get_object_or_404(FreePost, pk=pk)
    return render(request, 'freeboard/freeboard_post_detail.html', {'post': post})

def freeboard_post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('freeboard_post_list')  # 게시글 리스트 페이지로 이동
    else:
        form = PostForm()
    return render(request, 'freeboard/freeboard_post_form.html', {'form': form})

def freeboard_post_edit(request, pk):
    post = get_object_or_404(FreePost, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('freeboard_post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'freeboard/freeboard_post_form.html', {'form': form})

def freeboard_post_delete(request, pk):
    post = get_object_or_404(FreePost, pk=pk)
    post.delete()
    return redirect('freeboard_post_list')

