"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from task.views import (
    home_page,
    get_all_task,
    create_new_task,
    update_task
)
from user.views import (
    us_login,
    register,
    us_info,
    us_logout
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('task/', get_all_task, name='all-task'),
    path('create/', create_new_task, name='create-task'),
    path('update-task/', update_task, name='update-task'),

]
urlpatterns += [
    path("login/", us_login, name='login'),
    path("register/", register, name='register'),
    path("info/", us_info, name='info'),
    path("log-out/", us_logout, name='log-out')
]


