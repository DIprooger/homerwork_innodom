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
    get_task_info_by_task_id,
    update_task,
    delete_task,
    get_comment_info,
    get_comment_info_by_id,
    update_comment,
    delete_comment,
    create_comment
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
    path("<int:task_id>/", get_task_info_by_task_id, name='task-info'),
    path("<int:task_id>/update/", update_task, name='update-task'),
    path("<int:task_id>.delete/", delete_task, name='delete-task'),

]
urlpatterns += [
    path("comment/", get_comment_info, name='all-comment'),
    path("comment/<int:comment_id>/", get_comment_info_by_id, name='comment-info'),
    path("comment/<int:comment_id>/update/", update_comment, name='update-comment'),
    path("comment/<int:comment_id>/delete", delete_comment, name='delete-comment'),
    path("comment/create/", create_comment, name='create-comment'),
]
urlpatterns += [
    path("login/", us_login, name='login'),
    path("register/", register, name='register'),
    path("info/", us_info, name='info'),
    path("log-out/", us_logout, name='log-out')
]
