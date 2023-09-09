import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from form import TaskForm, TaskDeleteForm,TaskUpdateForm
from django.shortcuts import render, redirect



@login_required
def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print("=="*5, "Le formulaire bien recu")
        if form.is_valid():
            print("=="*5, "Le formulaire est valide")
            task = form.save(commit=False)  
            task.user = request.user  
            task.save()  
            return redirect('tasks')
    else:
        print("=="*5, "Le formulaire n'est pas valide")
        form = TaskForm()
    return render(request, 'tasks/tables.html', {'form': form})

@login_required
def updateTask(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect('user_account/tables.html')
    else:
        form = TaskUpdateForm(request.POST or None, instance=task)
    return render(request, 'tasks/taskUpdate.html', {'form': form})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskDeleteForm(request.POST, instance=task)
        if form.is_valid():
            task.delete()
            return redirect('user_account/tables.html')
    else:
        form = TaskDeleteForm(instance=task)
    return render(request, 'user_account.html', {'form': form, 'task': task})


   
