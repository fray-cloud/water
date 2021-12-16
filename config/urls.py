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
from app_dashboard.views import dashboard
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('settings/', include('app_camera.urls')),
    path('', dashboard, name='dashboard'),
    # TODO update list
    # path('settings/', include('app_event.urls')),
    # path('detect/', include('app_color.urls')),
    # path('detect/', include('app_line.urls')),
    # path('detect/', include('app_pattren.urls')),
    # path('detect/', include('app_text.urls')),
]
