from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required(login_url="/accounts/login/")
def todo_list(request):
    if request.user.is_authenticated:
        print(request.user.username)
    context = {
        'tasks': Task.objects.filter(user=request.user),
    }
    return render(request, 'todo/main.html/', context)

@login_required(login_url="/accounts/login/")
def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        Task.objects.create(user=request.user, title=str(task))
        return redirect('/todo/')


@login_required(login_url="/accounts/login/")
def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        task.delete()
        return redirect('/todo/')
    
@login_required(login_url="/accounts/login/")
def task_complete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
    
        if task.complete:
            ValueError('task is alreedy completed')

        task.complete = True
        task.save()

        return redirect('/todo/')
    