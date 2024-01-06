from django.urls import path
from apps.news.views import (
    greeting,
    # home_page
)

urlpatterns = [
    path('', greeting),
    # path('about/', home_page),
]
