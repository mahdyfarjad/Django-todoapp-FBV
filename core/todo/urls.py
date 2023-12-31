from django.urls import path, include
from . import views

# todo URLs

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('add_task/', views.add_task, name='add-task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete-task'),
    path('task_complete/<int:id>/', views.task_complete, name='task-complete'),
    path('api/v1/', include('todo.api.v1.urls')),

]