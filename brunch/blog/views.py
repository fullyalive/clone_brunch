from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import PostForm, CustomUserForm
from .models import Post, CustomUser


def index(request):
    return render(request, 'blog/index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    error_msg = ''
    if request.method == 'POST':    # 양식 제출
        form = CustomUserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
        else:
            error_msg = '다시 입력해주세요'
    else:
        form = CustomUserForm()
    return render(request, 'blog/register.html', {'form': form, 'error_msg': error_msg})


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    error_msg = ''
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_msg = '존재하지 않는 계정입니다.'
    else:
        form = CustomUserForm()
    return render(request, 'blog/signin.html', {'form': form, 'error_msg': error_msg})


def signout(request):
    logout(request)
    return redirect('index')


def create_post(request):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():  # author auto-field
            post = form.save(commit=False)
            post.author = CustomUser.objects.get(email=request.user.email)
            form.save()
            return redirect('my_post')

    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


def my_post(request):
    if not request.user.is_authenticated:
        return redirect('index')

    posts = Post.objects.filter(author=request.user.id).order_by('-date')
    return render(request, 'blog/my_post.html', {'posts': posts})


def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/show_post.html', {'post': post})
