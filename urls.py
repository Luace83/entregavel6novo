from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),  # Adicionando a URL do app hello
]
