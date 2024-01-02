from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('web_app/', include('web_app.urls')),
    path('admin/', admin.site.urls),
]
handler404 = 'web_app.views.custom_404'
