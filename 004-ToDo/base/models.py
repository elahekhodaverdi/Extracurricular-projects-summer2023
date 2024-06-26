from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from enum import Enum
# Create your models here.
  
class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []  

class Priority(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    DONTCARE = 4 
  
    def __str__(self):
      return str(self.value)
  
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name    

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    priority : Priority = Priority.DONTCARE
    class Meta:
        ordering = ('due_date','-updated_at')
        
    def __str__(self):
        return self.description[0:50]
    
    def formatted_date(self):
        today = timezone.now().date()
        tomorrow = today + timezone.timedelta(days=1)
        if self.due_date == today:
            return 'Today'
        elif self.due_date == tomorrow:
            return 'Tomorrow'
        else:
            return self.due_date.strftime('%d %b %Y')
    
    
    
class Comment(models.Model):
    body = models.TextField(null = True)
    task = models.ForeignKey(Task, on_delete = models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self) -> str:
        return self.body
    
    
    
    
    
    
         