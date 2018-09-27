from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserForm
from .models import CustomUser

def index(request):
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
    return render(request, 'blog/register.html', {'form': form, 'error_msg': error_msg})


def signin(request):
    return render(request, 'blog/signin.html')


def signout(request):
    return render(request, 'blog/index.html')
