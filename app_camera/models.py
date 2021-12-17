from django.db import models

# Create your models here.
class CameraSetting(models.Model):
    id = models.AutoField(primary_key=True)
    camera_name = models.TextField(default='', max_length=255, verbose_name='카메라 이름')
    camera_id = models.TextField(default='', max_length=255, verbose_name='카메라 아이디')
    camera_pw = models.TextField(default='', max_length=255, verbose_name='카메라 비밀번호')
    camera_ip = models.TextField(max_length=255, verbose_name='카메라 아이피')
    camera_port = models.TextField(default='', max_length=255, verbose_name='카메라 포트')
    camera_url = models.TextField(default='', max_length=255, verbose_name='RTSP URL')
    camera_alive = models.BooleanField(default=False)
    
    def __str__(self):
        if self.camera_port == '':
            return f'rtsp://{self.camera_id}:{self.camera_pw}@{self.camera_ip}/{self.camera_url}'
        elif self.camera_id == '' or self.camera_pw == '':
            return f'rtsp://{self.camera_ip}:{self.camera_port}/{self.camera_url}'
        elif self.camera_port == '' and (self.camera_id == '' or self.camera_pw == ''):
            return f'rtsp://{self.camera_ip}/{self.camera_url}'
        return f'rtsp://{self.camera_id}:{self.camera_pw}@{self.camera_ip}:{self.camera_port}/{self.camera_url}'

class CameraCapture(models.Model):
    camera = models.ForeignKey('app_camera.CameraSetting', on_delete=models.CASCADE, verbose_name='카메라 아이디')
    camera_capture = models.ImageField(null=True, verbose_name='카메라 캡쳐', upload_to='capture/')