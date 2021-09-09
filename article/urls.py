from django.urls import path, re_path ,include
from .views import (home, json_content, detail, category,
                   Home, Detail, CategoryView, AuthorView,
                   Preview, SearchList)

app_name = 'article'
urlpatterns = [
    # path('',home,name='home'),
    # path('page/<int:page>',home,name='home'),
    path('',Home.as_view(),name='home'),
    path('page/<int:page>',Home.as_view(),name='home'),

    path('json_content/',json_content,name='home2'),

    # path('article/<slug:slug>',detail,name='detail'),
    path('article/<slug:slug>',Detail.as_view(),name='detail'),

    path('preview/<int:pk>',Preview.as_view(),name='preview'),

    # path('category/<slug:slug>',category,name='category'),
    # path('category/<slug:slug>/<int:page>',category,name='category'),
    path('category/<slug:slug>',CategoryView.as_view(),name='category'),
    path('category/<slug:slug>/page/<int:page>',CategoryView.as_view(),name='category'),

    path('author/<slug:username>',AuthorView.as_view(),name='author'),
    path('author/<slug:username>/page/<int:page>',AuthorView.as_view(),name='author'),

    path('search/',SearchList.as_view(),name='search'),
    path('search/page/<int:page>',SearchList.as_view(),name='search'),

]
