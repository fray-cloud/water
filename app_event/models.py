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
    camera_interval_id = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    color_interval = models.FloatField(choices=interval_choice)
    line_interval = models.FloatField(choices=interval_choice)
    text_interval = models.FloatField(choices=interval_choice)

class ROIControl(models.Model):
    camera = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    roi_x = models.IntegerField()
    roi_y = models.IntegerField()
    roi_w = models.IntegerField()
    roi_h = models.IntegerField()
 
class ColorROIControl(models.Model):
    roi = models.ForeignKey('ROIControl', on_delete=models.CASCADE, verbose_name='ROI 아이디')
    color_select = models.TextField(choices=color_choice)
    color_x = models.IntegerField()
    color_y = models.IntegerField()
    color_w = models.IntegerField()
    color_h = models.IntegerField()

class LineROIControl(models.Model):
    roi = models.ForeignKey('ROIControl', on_delete=models.CASCADE, verbose_name='ROI 아이디')
    line_x = models.IntegerField()
    line_y = models.IntegerField()
    line_w = models.IntegerField()
    line_h = models.IntegerField()

class TextROIControl(models.Model):
    roi = models.ForeignKey('ROIControl', on_delete=models.CASCADE, verbose_name='ROI 아이디')
    text_x = models.IntegerField()
    text_y = models.IntegerField()
    text_w = models.IntegerField()
    text_h = models.IntegerField()