from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.models import User
from .decorators import *


def register(request):  # регистрация
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # валидация данных
            user = form.save()
            login(request, user)
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@unauthenticated_user  # залогиненный юзер не может открыть эту страницу
def user_login(request):  # аутентификация
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():  # валидация данных
            user = form.get_user()
            login(request, user)
            return redirect('user_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def user_list(request):  # вывод списка всех юзеров
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


@login_required
def user_update(request, pk):  # обновление юзера
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)  # обновляем конкретного юзера по его primary key
        if form.is_valid():  # валидация данных
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'users/user_update.html', {'form': form})


@login_required
def user_delete(request, pk):  # удаление юзера
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('user_list')


def user_create(request):  # добавление нового юзера
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # валидация данных
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/user_new.html', {'form': form})


def user_logout(request):  # выход
    logout(request)
    return redirect('user_list')
