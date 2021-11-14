"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import Login, Signup, activate
from dj_rest_auth.views import PasswordResetConfirmView
from api.views import GreetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('article.urls')),

    path('login/', Login.as_view(), name='login'),
    path('',include('django.contrib.auth.urls')),

    path('signup/', Signup.as_view(), name='signup'),
    path('activate/<uidb64>/<token>',activate, name='activate'),

    path('account/',include('user.urls')),

    path('comment/', include('comment.urls')),

    path('ratings', include('star_ratings.urls', namespace='ratings')),

    path('api/', include('api.urls')),

    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uid64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('account-confirm-email/<key>', GreetView.as_view(),name='account_confirm_email'
    ),
    

]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

