from django.db import models
from django.contrib.auth.admin import User


class Task(models.Model):
    title = models.CharField(max_length=30, default='Enter title: ')
    description = models.TextField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=[
        (1, 'В ожидании'),
        (2, 'В процессе'),
        (3, 'Завершено')
    ])
    date_started = models.DateField(help_text="День, когда задача должна начаться")
    deadline = models.DateField(help_text="День, когда задача должна быть выполнена")
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def str(self):
        return f"{self.title[:10]}..."

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Comment(models.Model):
    title = models.CharField(max_length=50, default='Enter title: ')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def str(self):
        return f"{self.title[:10]}..."

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'