from django.db import models


interval_choice = [
    ("10sec", 10000.0),
    ("30sec", 30000.0),
    ("60sec", 60000.0)
]

color_choice = [
    ('빨강', 'red'),
    ('파랑', 'blue'),
    ('초록', 'green'),
]

# Create your models here.
class IntervalControl(models.Model):
    camera = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    color_interval = models.FloatField(choices=interval_choice, default=interval_choice[0][1])
    line_interval = models.FloatField(choices=interval_choice, default=interval_choice[0][1])
    text_interval = models.FloatField(choices=interval_choice, default=interval_choice[0][1])
 
class ColorROIControl(models.Model):
    camera = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    color_select = models.TextField(choices=color_choice)
    color_x = models.IntegerField(default=0)
    color_y = models.IntegerField(default=0)
    color_w = models.IntegerField(default=200)
    color_h = models.IntegerField(default=200)

class LineROIControl(models.Model):
    camera = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    line_x = models.IntegerField(default=0)
    line_y = models.IntegerField(default=0)
    line_w = models.IntegerField(default=200)
    line_h = models.IntegerField(default=200)

class TextROIControl(models.Model):
    camera = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    text_x = models.IntegerField(default=0)
    text_y = models.IntegerField(default=0)
    text_w = models.IntegerField(default=200)
    text_h = models.IntegerField(default=200)