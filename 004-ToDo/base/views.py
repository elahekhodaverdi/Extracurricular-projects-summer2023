from django.shortcuts import render, redirect
from .forms import TaskForm, CategoryForm, MyUserCreationForm,UserForm
from .models import Task, Category, User
from django.utils import timezone
from django.contrib.auth import authenticate , login, logout
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.db.models import Q


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context ={'page': page}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def signupPage(request):
    form  = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
            
    context = {'form': form}
    return render(request, 'base/login.html', context)

@login_required(login_url ='/login')
def tasksPage(request):
    sort_by, q  = request.GET.get('sort_by', ''),  request.GET.get('q', '')
    user = request.user
    tasks = user.task_set.all()
    print(q)
    if q:
        if q == 'today':
            date = timezone.now().date()
        elif q == 'tomorrow':
            date = timezone.now().date() + timezone.timedelta(days=1)
        else:
            date = datetime.strptime(q, "%d-%m-%y").date()
        tasks = Task.objects.filter(due_date=date)
    
    fields = [field for field in Task._meta.fields
              if field.editable and field.name not in ['user','completed','id', 'description']]
    if sort_by:
        tasks = tasks.order_by(sort_by)

    context = {'tasks': tasks, 'fields': fields}
    return render(request, 'base/tasks.html', context)

@login_required(login_url ='/login')
def taskPage(request,pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.completed = not(task.completed)
        task.save()
        return redirect('home')
    comments = task.comment_set.all()
    context = {'task':task, 'comments':comments}
    return render(request,'base/task.html', context)
    
@login_required(login_url ='/login')
def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'base/task-form.html',context)

@login_required(login_url ='/login')
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    if request.user == task.user:
        task.delete()
    return redirect('home')

@login_required(login_url ='/login')
def categoriesPage(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    
    return render(request,'base/categories.html',context)

@login_required(login_url ='/login')
def categoryPage(request, pk):
    category = Category.objects.get(id=pk)
    tasks = category.task_set.filter(user = request.user)
    context = {'tasks': tasks, 'category': category}
    
    return render(request, 'base/category.html', context)
     
@login_required(login_url ='/login')
def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.user != task.user:
        return redirect('home')
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/task-form.html' , context)

@login_required(login_url ='/login')
def createCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form
            category.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'base/category-form.html',context)
