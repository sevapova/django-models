from django.urls import path

from .views import create_task, task_list, counter_view, get_user, create_user, get_user_by_id


urlpatterns = [
    path('', create_task, name='task_create'),
    path('list/', task_list, name='task_list'),
    path('counter/', counter_view, name='counter'),
    path('users/<int:pk>', get_user_by_id),
    path('users/<slug:slug>', get_user, name='get_user'),
    path('users/', create_user, name='create_user'),
]

