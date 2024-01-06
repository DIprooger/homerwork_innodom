from django.contrib import admin
from apps.models import Project, Task, Status


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'status', 'created_at')
    list_filter = ('priority', 'status', 'created_at')
    search_fields = ('name',)


admin.site.register(Status)
# Register your models here.
