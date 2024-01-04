from django.urls import path
from .views import web_transform

urlpatterns = [
    path('transformation_service/', web_transform, name='web_transform'),
]
