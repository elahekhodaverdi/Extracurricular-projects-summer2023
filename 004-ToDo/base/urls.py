from django.contrib import admin
from django.urls import path
from . import views


urlpatterns =[
    path('', views.tasksPage, name='home'),
    path('tasks/', views.tasksPage, name='tasks'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('categories/', views.categoriesPage, name='categories'),
    path('categories/<str:pk>', views.categoryPage, name='category'),
    path('task/<str:pk>', views.taskPage, name='task'),
    path('create-task/', views.createTask, name='create-task'),
    path('create-category/', views.createCategory, name='create-category'),
    path('delete-task/<str:pk>', views.deleteTask, name='delete-task'),
    path('update-task/<str:pk>', views.updateTask, name='update-task'),
    
]