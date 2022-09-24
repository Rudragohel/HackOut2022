"""ServeGoal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from ServeGoal_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index_page'),
    path('index', views.index, name='index_page'),
    path('login', views.login, name='login_page'),
    path('user_creation', views.verify_user, name='user_verify_page'),
    path('register', views.display_register, name='user_register_page'),
    path('user_register', views.create_user, name='user_creation_page'),

]
urlpatterns += staticfiles_urlpatterns()
