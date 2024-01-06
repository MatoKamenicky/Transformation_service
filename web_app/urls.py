from django.urls import path
from .views import home, result, transform_xy, transform_xyz, about_us

urlpatterns = [
    path('transform_xy/', transform_xy, name='transform_xy'),
    path('transform_xyz/', transform_xyz, name='transform_xyz'),
    path('home/', home, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('result/', result, name='result'),
]
