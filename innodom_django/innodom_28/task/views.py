from django.shortcuts import render, redirect
from task.models import Task, Status
from django.contrib.auth.models import User
from task.forms import CreateTask, TaskUpdateForm
from django.shortcuts import (
    get_object_or_404,
)

# Status.objects.create(name="В ожидании")
# Status.objects.create(name="В процессе")
# Status.objects.create(name="Завершено")


def home_page(request):
    task = Task.objects.all()
    context = {'tasks': task}
    return render(
        request=request,
        template_name='task/all_task.html',
        context=context
    )


def get_all_task(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(
        request=request,
        template_name='task/all_task.html',
        context=context
    )


def create_new_task(request):
    statuses = Status.objects.all()
    creators = User.objects.all()

    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            product_data = form.cleaned_data
            Task.objects.create(**product_data)
            return redirect("all-task")
        context = {
            'form': form,
            'statuses': statuses,
            'creators': creators
        }
    else:
        form = CreateTask()
        context = {
            'form': form,
            'statuses': statuses,
            'creators': creators
        }

    return render(
        request=request,
        template_name='task/create_task.html',
        context=context
    )


def update_task(request):
    task = Task.objects.all()
    statuses = Status.objects.all()

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('all-task')

        context = {
            "form": form,
            "task": task,
            "statuses": statuses
        }
    else:
        form = TaskUpdateForm()

        context = {
            "form": form,
            "task": task,
            "statuses": statuses
        }

    return render(
        request=request,
        template_name='update_task.html',
        context=context
    )
