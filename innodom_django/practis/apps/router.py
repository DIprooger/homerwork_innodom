from django.urls import path, include
from apps.news.views import shou_user_info
# homerwor_programing_innodom.innodom_django.practis.apps.news.urls
urlpatterns = [
    path('news/', include('apps.news.urls')),
    path('', shou_user_info)
]
