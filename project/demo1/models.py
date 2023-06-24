from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class TodoItem(models.Model):
    item_Title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    itemCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item_Title




