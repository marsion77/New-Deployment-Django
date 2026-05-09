from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


# Show tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


# Add task
def add_task(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})


# Update task
def update_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = TaskForm(instance=task)

    return render(request, 'update_task.html', {'form': form})


# Delete task
def delete_task(request, id):

    task = get_object_or_404(Task, id=id)
    task.delete()

    return redirect('/')