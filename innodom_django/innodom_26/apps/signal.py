from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from apps.models import Project


@receiver(post_delete, sender=Project)
def post_delet_projact(sender, instance, **kwargs):
    print(f"Project {instance} delete")


@receiver(post_save, sender=User)
def post_save_superuser(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        print("Superuser created")
