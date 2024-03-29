from django.contrib.auth.models import User
from django.forms import (
    ModelForm,
    fields,
    widgets,
    ModelChoiceField
)
from task.models import Task, Status, Comment


class CreateTask(ModelForm):
    title = fields.CharField(max_length=30)
    description = fields.CharField(max_length=100)
    creator = ModelChoiceField(queryset=User.objects.all())
    status = ModelChoiceField(queryset=Status.objects.all())
    date_started = fields.DateField(
        widget=widgets.DateInput(attrs={'type': 'date'}))
    deadline = fields.DateField(
        widget=widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
            'deadline'
        )


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'title',
            'creator'
        ]


class CommentUpdateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title',]
