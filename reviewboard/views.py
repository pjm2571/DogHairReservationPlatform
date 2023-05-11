from .models import ReviewPost
from .forms import PostForm
from django.utils import timezone
import datetime
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

def review_post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('review_post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'reviewboard/review_post_edit.html', {'form': form})

def review_post_list(request):
    query = request.GET.get('search') #검색어를 받아옴

    if query:
        searchPosts = ReviewPost.objects.filter( #검색어를 포함한 게시글을 찾아옴
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    else:
        searchPosts = ReviewPost.objects.all() #검색어가 없을 경우 모든 게시글을 보여줌

    posts = ReviewPost.objects.all()
    today = datetime.date.today()
    context = {'today': today, 'posts': posts, 'searchPosts':searchPosts}
    return render(request, 'reviewboard/review_post_list.html', context)

def review_post_detail(request, pk):
    post = get_object_or_404(ReviewPost, pk=pk)
    return render(request, 'reviewboard/review_post_detail.html', {'post': post})

def review_post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('review_post_list')  # 게시글 리스트 페이지로 이동
    else:
        form = PostForm()
    return render(request, 'reviewboard/review_post_form.html', {'form': form})

def review_post_edit(request, pk):
    post = get_object_or_404(ReviewPost, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('review_post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'reviewboard/review_post_form.html', {'form': form})

def review_post_delete(request, pk):
    post = get_object_or_404(ReviewPost, pk=pk)
    post.delete()
    return redirect('review_post_list')
