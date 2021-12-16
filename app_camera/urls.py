"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from .views.create import CameraCreateView
from .views.delete import CameraDeleteView
from .views.update import CameraUpdateView
from .views.detail import CameraDetailView

app_name = 'app_camera'

urlpatterns = [
    path('delete/<int:pk>', CameraDeleteView.as_view(), name='camera_delete'),
    path('detail/<int:pk>', CameraDetailView.as_view(), name='camera_detail'),
    path('update/<int:pk>', CameraUpdateView.as_view(), name='camera_update'),
    path('create/', CameraCreateView.as_view(), name='camera_create'),
]
