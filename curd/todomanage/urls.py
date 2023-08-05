
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
path('', views.todo_list, name='todo_list'),
    path('/todo_create/', views.todo_create, name='todo_create'),
    path('update/<int:todo_id>/', views.todo_update, name='todo_update'),
    path('delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
]
