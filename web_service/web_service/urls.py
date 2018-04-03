"""web_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from views import views as learn_views
from login import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('', learn_views.index),  # new
    path('add/', learn_views.add , name ="add"),
    path('add2/<int:a>/<int:b>/', learn_views.add2 , name = "add2"),
    path('home/', learn_views.home , name = "home"),
    path("home2/", learn_views.home2 , name = "home2"),
    path("home3/", learn_views.home3 , name = "home3"),
    path("home4/", learn_views.home4 , name = "home4"),
    path("home5/" , learn_views.home5 , name = "home5"),
    path("index/" , learn_views.index , name = "index"),
#login_views
    path("login/" , login_views.login , name = "login"),
 #   path(r'^accounts/', learn_views('users.urls')),
]
