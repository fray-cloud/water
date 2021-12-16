from django.db import models

# Create your models here.
class ColorSetting(models.Model):
    camera = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    gaussian_ksize = models.IntegerField(default=5)
    thresh = models.IntegerField(default=92)
    maxval = models.IntegerField(default=255)
