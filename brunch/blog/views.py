from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import PostForm, CustomUserForm
from .models import CustomUser, Post, Comment


def index(request):
    print('인덱스입니당')
    return render(request, 'blog/index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    error_msg = ''
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
        else:
            error_msg = '다시 입력해주세요'
    else:
        form = CustomUserForm()
    return render(request, 'blog/register.html', {'form':form, 'error_msg': error_msg})   


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
    return render(request, 'blog/signin.html', {'form':form, 'error_msg':error_msg})



def signout(request):
    logout(request)
    return redirect('index')


def create_post(request):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid(): # author auto-field
            post = form.save(commit=False)
            post.author = CustomUser.objects.get(email=request.user.email)
            form.save()
            return redirect('my_post')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form':form})


def my_post(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    posts = Post.objects.filter(author=request.user.id).order_by('-date')
    return render(request, 'blog/my_post.html', {'posts': posts})


def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'blog/show_post.html', {'post': post, 'comments': comments})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user != post.author:
        return redirect('index')

    post.delete()
    return redirect('my_post')

def update_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user != post.author:
        return redirect('index')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('my_post')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/update_post.html', {'form': form})


@login_required
def subscribe(request, author_name):
    if not request.user.is_authenticated:
        return redirect('index')
    author = CustomUser.objects.get(name=author_name)
    request.user.following.add(author)
    return redirect('index')

@login_required
def list_following(request, user_name):
    user_obj = CustomUser.objects.get(name=user_name)
    following = list(user_obj.following.all())
    return render(request, 'blog/following.html', {'following':following})

def list_post(request, user_name):
    user_obj = CustomUser.objects.get(name=user_name)
    posts = Post.objects.filter(author=user_obj).order_by('-date')
    return render(request, 'blog/list_post.html', {'posts':posts})

def search_post(request):
    posts = Post.objects.all()
    q = request.GET.get('q','')
    if q:
        posts = posts.filter(Q(title__icontains=q)
                             | Q(contents__icontains=q)
                             | Q(author__name__icontains = q)
        )
    return render(request, 'blog/search_post.html', {'posts':posts})
