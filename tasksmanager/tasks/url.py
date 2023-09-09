from django.urls import path
from .views import createTask, updateTask, deleteTask
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('createTask/', createTask, name='createTask'),
    path('updateTask/<int:id>/', updateTask, name='updateTask'),
    path('deleteTask/<int:id>/', deleteTask, name='deleteTask'),

]