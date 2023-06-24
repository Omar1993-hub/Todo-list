from django.shortcuts import render , redirect
from .models import *
from .forms import *
from .filters import TodoFilter
from .forms import UserForm, TodoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required , user_passes_test

# Create your views here.
@login_required(login_url='login')
def home(request, id=""):
    user = request.user
    todos = Todo.objects.all()
    filter = TodoFilter(request.GET, queryset=todos)

    if request.method == 'GET':  # Corrected 'GEST' to 'GET'
        todos = filter.qs  # Assign filtered queryset to 'todos' variable

    if user is not None:
        todos = todos.filter(user=user)  # Apply user filter to 'todos'
    else:
        return redirect('login')

    if id:
        todo = Todo.objects.get(id=id)
        print(request.POST)
        todoItem = TodoItem.objects.create(
            item_Title=request.POST.get('item_Title'),
            description=request.POST.get('description'),
            itemCreated=request.POST.get('itemCreated'),
            todo=todo,
        )
        todoItem.save()
        return redirect('base')

    context = {
        'todos': todos,
        'user': user,
        'filter': filter,
    }
    return render(request, 'todo.html', context)
# def home(request, id=""):
#     user = request.user
#     todos = Todo.objects.all()
#     filter = TodoFilter(request.GET, queryset=todos)
#     if request.method == 'GET':
#         filter = filter.qs
#     if user is not None:
#         todos = Todo.objects.filter(user=user)
#     else:
#         return redirect('login')
#     if id:
#         todo= Todo.objects.get(id=id)
#         print(request.POST)
#         todoItem = TodoItem.objects.create(
#             item_Title=request.POST.get('item_Title'),
#             description=request.POST.get('description'),
#             itemCreated= request.POST.get('itemCreated'),
#             todo=todo,
#         )
#         todoItem.save()
#         return redirect('base')
#     context = {
#         'todos': todos,
#         'user': user,
#         'filter': filter,
#     }
#     return render(request, 'todo.html', context)

@login_required(login_url='login')
def create(request):
    user = request.user
    form = TodoForm(request.POST)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
            return redirect('base')
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

# create todo item function
@login_required(login_url='login')
def createTodoItem(request, id):
    user = request.user
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('item_Title')
        description = request.POST.get('description')
        itemCreated = request.POST.get('itemCreated')
        item = TodoItem.objects.create(
            item_Title=title,
            description=description,
            itemCreated= itemCreated,
            todo=todo,
        )
        item.save()
        return redirect('base')
    context = {
        
    }
    return render(request, 'createitem.html', context)


@login_required(login_url='login')
def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('base')
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)


@login_required(login_url='login')
def updateTodoItem(request, id):
    todoItem = TodoItem.objects.get(id=id)
    form = TodoItemForm(instance=todoItem)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todoItem)
        if form.is_valid():
            form.save()
            return redirect('base')
    context = {
        'form': form,
    }
    return render(request, 'updateTodoItem.html', context)


@login_required(login_url='login')
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('base')


@login_required(login_url='login')
def deleteTodoItem(request, id):
    todoItem = TodoItem.objects.get(id=id)
    todoItem.delete()
    return redirect('base')


@login_required(login_url='login')
def detailed(request, id):
    todoItems = TodoItem.objects.get(id=id)
    context = {
        'todoItems': todoItems,
    }
    return render(request, 'detailed.html', context)

#################################### Register Function #############################
@user_passes_test(lambda u: u.is_anonymous, login_url='base')
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

@user_passes_test(lambda u: u.is_anonymous, login_url='base')
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('login')
    context = {}
    return render(request, 'login.html', context)

def userLogout(request):
    logout(request)
    return redirect('login')

########################## End of Registration Function ############################

