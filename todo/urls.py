from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.login_view, name='login'),
   path('register/', views.register_view, name='register'),
   path('profile/<int:user_id>', views.profile_view, name='profile'),
   path('todo/', views.to_do, name='todo'),
   path('todo_change/<int:todo_id>', views.change_status, name='change_status'),
   path('todo_delete/<int:todo_id>', views.delete_todo, name='delete_todo'),
   path('todo_edit/<int:todo_id>', views.edit_todo, name='edit_todo'),

   
]
