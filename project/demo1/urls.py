from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='base'),
    
    path('<str:id>', home, name='base'),
    
    # Create page
    path('create/', create, name='create'),
    
    # createTodoItem
    path('createitem/<int:id>/', createTodoItem, name='createTodoItem'),
    
    # Update page
    path('update/<int:id>/', update, name='update'),
    
    # updateTodoItem page
    path('updateTodoItem/<int:id>/', updateTodoItem, name='updateTodoItem'),
    
    # Delete page
    path('delete/<int:id>/', delete, name='delete'),
    
    # deleteTodoItem page
    path('deleteTodoItem/<int:id>/', deleteTodoItem, name='deleteTodoItem'),
    
    # Register page
    path('register/', register, name='register'),
    
    # login page
    path('login/', userLogin, name='login'),
    
    # Logout page
    path('logout/', userLogout, name='logout'),
    
    # Detailed page
    path('detailed/<int:id>/', detailed, name='detailed'),
    
]
