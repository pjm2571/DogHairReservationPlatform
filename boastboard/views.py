from .models import BoastPost
from .forms import PostForm
from django.utils import timezone
import datetime
from django.shortcuts import render, redirect, get_object_or_404

def boast_post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('boast_post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'boastboard/boast_post_edit.html', {'form': form})


def boast_post_list(request):
    posts = BoastPost.objects.all().order_by('-id')
    today = datetime.date.today()
    context = {'today': today, 'posts': posts}
    return render(request, 'boastboard/boast_post_list.html', context)

def boast_post_detail(request, pk):
    post = get_object_or_404(BoastPost, pk=pk)
    return render(request, 'boastboard/boast_post_detail.html', {'post': post})

def boast_post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('boast_post_list')  # 게시글 리스트 페이지로 이동
    else:
        form = PostForm()
    return render(request, 'boastboard/boast_post_form.html', {'form': form})

def boast_post_edit(request, pk):
    post = get_object_or_404(BoastPost, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('boast_post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'boastboard/boast_post_form.html', {'form': form})

def boast_post_delete(request, pk):
    post = get_object_or_404(BoastPost, pk=pk)
    post.delete()
    return redirect('boast_post_list')

