from django.urls import path
from . import views

urlpatterns = [
    path('web_app/', views.web_transform, name='web_transform'),
]