import threading
from django.apps import AppConfig


class AppCameraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_camera'
    
    camera_list = list()
    main_break_point = True
    check_time = 2

    def get_camera_info(self):
        from .models import CameraSetting
        get_dict = dict()

        get = CameraSetting.objects.all()
        for cam in get:
            name = cam.camera_name
            rtsp = str(cam)

            dic = {
                'name' : name,
                'rtsp' : rtsp,
            }

            get_dict[f'{cam.id}'] = dic

        return get_dict

    def ready(self):
        from .util.buffer_process import Streaming
        from threading import Thread
        import time
    
        def main():
            camera_count = 0
            
            while self.main_break_point:
                camera_dict = self.get_camera_info()
                if camera_count == 0 or len(camera_dict) != camera_count:
                    self.camera_list.clear()
                    camera_count = len(camera_dict)

                    for obj in camera_dict.values():

                        name = obj['name']
                        rtsp = obj['rtsp']
                        self.camera_list.append((Streaming(), rtsp, name))

                else:
                    for cam, rtsp, name  in self.camera_list:
                        if not cam.is_start:
                            cam.start(rtsp, name)
                        
                time.sleep(self.check_time)

            for cam, _, _ in self.camera_list:
                cam.end()

        main_thread = Thread(target=main, args=())
        main_thread.daemon = True
        main_thread.start()

        return super().ready()