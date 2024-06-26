from django.forms import ModelForm
from .models import Task, Category, User

from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['name', 'username', 'email' , 'password1', 'password2']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['completed','user']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','username', 'email']
