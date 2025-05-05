from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task-list'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
    path('complete/<int:pk>/', views.complete_task, name='complete-task'),
]