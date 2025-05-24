from django.urls import path

from . import views

urlpatterns = [
    path('task_list/',views.task_list, name = 'task_list'),
    path('add/',views.task_forms, name = 'add_task'),
    path('update/<int:pk>',views.update_task, name = 'update'),
    path('delete/<int:pk>',views.delete_task, name = 'delete')
]
