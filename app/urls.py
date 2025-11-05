from django.urls import path

from .views import create_task, task_list


urlpatterns = [
    path('', create_task, name='task_create'),
    path('list/', task_list, name='task_list'),
]
