from django.shortcuts import render, redirect

from django.urls import reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.core.exceptions import ObjectDoesNotExist

from .forms import *

def home(request):
    if request.user.is_authenticated:
        return redirect('dash')
    return render(request, 'users/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect('dash', user.id)
            return redirect('dash')
        return redirect('login_view')
    elif request.method == 'GET':
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_view')


def register_view(request):
    if request.method == 'GET':
        context = {'form': CustomUserCreationForm}
        return render(request, 'users/register.html', context)
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dash')
        return redirect('register_view')

# For using with pk in URL
# def dash(request, pk):
#     if request.user.id == int(pk):
#         form = TaskForm()
#         context = {'form': form}
#         return render(request, 'users/dash.html', context)
#     elif request.user.id != pk:
#         return render(request, 'users/unauth.html')


def dash(request):
    if request.user.is_authenticated == False:
        return redirect('login_view')
    if request.method == 'GET':
        form = TaskForm(initial={'owner': request.user})
        tasks = Task.objects.filter(owner=request.user)
        remaining_tasks = tasks.filter(complete=False)
        completed_tasks = tasks.filter(complete=True)
        context = {'form': form, 'tasks': tasks, 'remaining_tasks': remaining_tasks, 'completed_tasks': completed_tasks}
        return render(request, 'users/dash.html', context)
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dash')


def view_task(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, 'users/unexist.html')
    if task.owner != request.user:
        return render(request, 'users/unauth.html')
    form = TaskDoneForm(instance=task)
    context = {'task': task, 'form': form}
    if request.method == 'POST':
        form = TaskDoneForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('view_task', pk)
    return render(request, 'tasks/view.html', context)


def edit_task(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, 'users/unexist.html')
        
    if task.owner != request.user:
        return render(request, 'users/unauth.html')
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('dash')
    
    context = {'form': form}
    return render(request, 'tasks/edit.html', context)


def delete_task(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, 'users/unexist.html')
    if task.owner != request.user:
        return render(request, 'users/unauth.html')
    
    if request.method == 'POST':
        task.delete()
        return redirect('dash')
    
    context = {'task': task}
    return render(request, 'tasks/delete.html', context)