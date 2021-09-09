from django.urls import path
from django.contrib.auth import views
from .views import (Home, CreateArticle, UpdateArticle, DeleteArticle,
                     Profile ,Login ,Signup ,activate)

app_name = 'account'
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('create/',CreateArticle.as_view(),name='create'),
    path('update/<int:pk>',UpdateArticle.as_view(),name='update'),
    path('delete/<int:pk>',DeleteArticle.as_view(),name='delete'),
    path('profile/',Profile.as_view(),name='profile'),
]


