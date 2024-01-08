from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    priority = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    status = models.ForeignKey(
        Status,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(
        Project,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Project)
def post_delet_projact(sender, instance, **kwargs):
    print(f"Project {instance} delete")


@receiver(post_save, sender=User)
def post_save_superuser(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        print("Superuser created")
