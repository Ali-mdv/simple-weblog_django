from django.urls import path,include
from rest_framework import routers
from .views import (
                    # ArticleListView,
                    # ArticleDetailView,
                    # UserListView,
                    # UserDetailView,
                    # CustomAuthToken,
                    # RevokeView,

                    ArticleViewSet,
                    UserViewSet,
                    AuthorView,
                    )

app_name = 'api'

router = routers.SimpleRouter()
router.register('articles',ArticleViewSet,basename='article')
router.register('users',UserViewSet)


urlpatterns = [
    # path('articles/',ArticleListView.as_view()),
    # path('articles/<slug:slug>',ArticleDetailView.as_view()),

    # path('users/',UserListView.as_view()),
    # path('users/<int:pk>',UserDetailView.as_view()),

    path('',include(router.urls)),

    path('authors/<int:pk>',AuthorView.as_view(),name='authors'),


    # path('token/', CustomAuthToken.as_view()),
    # path('token/revoke/', RevokeView.as_view()),
    ]