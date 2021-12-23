from django.db import models
# 초기 defalut 설정은 임의 설정

interval_choice = [
    (10.0, "10sec"),
    (30.0, "30sec"),
    (60.0, "60sec")
]

color_choice = [
    ('red', '빨강'),
    ('blue', '파랑'),
    ('green', '초록'),
]

ksize_choice = [
    (3, '3'),
    (5, '5'),
    (7, '7'),
]

# Create your models here.
class IntervalControl(models.Model):
    camera         = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    color_interval = models.FloatField(choices=interval_choice, default=interval_choice[0][0])
    line_interval  = models.FloatField(choices=interval_choice, default=interval_choice[0][0])
    text_interval  = models.FloatField(choices=interval_choice, default=interval_choice[0][0])
 
class ColorROIControl(models.Model):
    camera       = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    color_select = models.TextField(choices=color_choice)
    color_x      = models.IntegerField(default=0)
    color_y      = models.IntegerField(default=0)
    color_w      = models.IntegerField(default=200)
    color_h      = models.IntegerField(default=200)

class LineParamControl(models.Model):
    camera                   = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    line_gaussian_ksize      = models.IntegerField(default=ksize_choice[0][0], choices=ksize_choice)
    line_gaussian_sigmaX     = models.IntegerField(default=0)
    line_canny_threashold1   = models.IntegerField(default=50)
    line_canny_threashold2   = models.IntegerField(default=100)
    line_theta               = models.IntegerField(default=0)
    line_hough_threshold     = models.IntegerField(default=50)
    line_hough_minLineLength = models.IntegerField(default=2)

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