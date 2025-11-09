import base64
import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils.text import slugify


from .models import Task, User


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

def counter_view(request: HttpRequest) -> HttpResponse:
    
    body = request.body.decode()

    data = json.loads(body)
    print(data['name'], data['age'])

    return HttpResponse()


def get_user(request: HttpRequest, slug: str) -> HttpResponse:

    text = "salom DUNYO, kfjnasdkjbfasdkj"
    slug = slugify(text)

    data = [
        {
            "name": "Samsung Televizor",
            "price": 213,
            "slug_name": "samsung-televizor", # SEO
            "id": 1
        }
    ]

    response = JsonResponse(
        data=data,
        safe=False,
        headers={"Accept-Language": "uzbek"},
        status=202
    )
    return response



def create_user(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body.decode())

    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        tg_id=data['tg_id']
    )
    user.save()

    return JsonResponse({'message': 'ok'}, status=201)

def get_user_by_id(request: HttpRequest, pk: int) -> JsonResponse:
    user = get_object_or_404(User, pk=pk)
    
    return JsonResponse({
        'id': user.id,
        'fullname': user.full_name,
        'age': user.age,
        'tg_id': user.tg_id
    })

