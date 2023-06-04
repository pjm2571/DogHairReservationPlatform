from pyexpat.errors import messages
from tkinter.messagebox import QUESTION

from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from .models import ReviewPost
from .models import Recommended_ReviewPost
from .forms import PostForm
from django.utils import timezone
import datetime
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from main.views import Main


# 이건 머지?
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


# Post List
def review_post_list(request):
    query = request.GET.get('search')
    if query:
        searchPosts = ReviewPost.objects.order_by('-created_at').filter(  # -created_at은 게시물 역순으로 정렬
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    else:
        searchPosts = ReviewPost.objects.all().order_by('-created_at')

    today = datetime.date.today()
    # 페이징요소들
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(searchPosts, 13)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'today': today, 'searchPosts': page_obj}
    return render(request, 'reviewboard/review_post_list.html', context)


# Post 상세보기
def review_post_detail(request, pk):
    post = get_object_or_404(ReviewPost, pk=pk)

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

    context['post'] = post

    context['is_Recommended'] = False

    if Recommended_ReviewPost.objects.filter(user=user, post=post).exists():
        context['is_Recommended'] = True

    return render(request, 'reviewboard/review_post_detail.html', context)


# Post 생성
def review_post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # request.FILES은 이미지를 업로드에 필요한 매개변수다
        if form.is_valid():
            post = form.save(commit=False)
            nickname = request.session['nickname']
            post.author = nickname
            # post.published_date = timezone.now()
            post.save()
            return redirect('review_post_list')  # 게시글 리스트 페이지로 이동
    else:
        form = PostForm()
    return render(request, 'reviewboard/review_post_form.html', {'form': form})


# Post 수정
def review_post_edit(request, pk):
    post = get_object_or_404(ReviewPost, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('review_post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'reviewboard/review_post_form.html', {'form': form})


# Post 삭제
def review_post_delete(request, pk):
    post = get_object_or_404(ReviewPost, pk=pk)
    post.delete()
    return redirect('review_post_list')


class review_post_like(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', None)
        post_id = request.data.get('post_id', None)

        user = User.objects.filter(id=user_id).first()
        post = ReviewPost.objects.filter(id=post_id).first()

        # 이미 존재하는 경우 오류 처리
        if Recommended_ReviewPost.objects.filter(user=user, post=post).exists():
            return Response(status=400, data=dict(message="이미 추천된 게시물입니다."))

        post.liked_num += 1
        post.save()

        Recommended_ReviewPost.objects.create(
            user=user,
            post=post
        )

        return Response(status=200, data=dict(message="추천하였습니다."))
