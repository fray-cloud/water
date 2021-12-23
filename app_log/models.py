from django.db import models


# Create your models here.
class ColorLog(models.Model):
    camera  = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    red     = models.IntegerField()
    blue    = models.IntegerField()
    green   = models.IntegerField()
    date    = models.DateTimeField(auto_now=True)

class LineLog(models.Model):
    camera  = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    length  = models.IntegerField()
    date    = models.DateTimeField(auto_now=True)

class TextLog(models.Model):
    camera  = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    texts   = models.CharField(max_length=10000)
    date    = models.DateTimeField(auto_now=True)

