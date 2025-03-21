from django.urls import path
from .views import create, list, update, read

urlpatterns = [
    path('create/', create.view, name='create'),
    path('', list.view  , name='list'),
    path('update/<int:id>', update.view, name='blog-update'),
    path('<int:id>', read.view, name='blog-read'),
]