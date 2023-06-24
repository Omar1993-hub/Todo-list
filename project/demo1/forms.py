from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, CheckboxInput
from .models import Todo , TodoItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
        exclude = ['user']

class TodoItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = ['item_Title', 'description', 'is_completed']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Title',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Description',
            }),
            'is_completed': CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

