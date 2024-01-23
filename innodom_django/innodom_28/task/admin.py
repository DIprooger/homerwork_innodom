from django.contrib import admin
from task.models import Task, Comment, Status


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'creator', 'status')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
