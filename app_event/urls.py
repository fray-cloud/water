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

from .views.update.interval import IntervalUpdateView
from .views.update.text import TextROIControlUpdateView
from .views.update.line import LineROIControlUpdateView

app_name = 'app_event'

urlpatterns = [
    path('interval/<int:camera_id>', IntervalUpdateView.as_view(), name='event_interval'),
    path('text/<int:camera_id>', TextROIControlUpdateView.as_view(), name='event_text'),
    path('line/<int:camera_id>', LineROIControlUpdateView.as_view(), name='event_line'),
]
