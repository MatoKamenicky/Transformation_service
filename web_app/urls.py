from django.urls import path
from .views import web_transform, result

urlpatterns = [
    path('transformation_service/', web_transform, name='web_transform'),
    path('result/', result, name='result'),
]
