from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Task


def create_task(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request=request, template_name='create.html')
    else:
        form = request.POST

        new_task = Task(
            name = form.get('name'),
            description = form.get('description'),
            priority = form.get('priority'),
        )
        new_task.save()

        return render(request=request, template_name='create.html')

def task_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }

    return render(request=request, template_name='list.html', context=context)
