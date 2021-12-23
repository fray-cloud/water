import threading
from django.apps import AppConfig


class AppCameraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_camera'
    
    camera_list = list()
    main_break_point = True
    check_time = 2
    ping = dict()

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
        """
        장고 내부에 앱이 실행되기 전 프로세스를 설정하기 위해 ready 함수를 오버라이드 하여 
        Striming 클래스를 통해 버퍼 스트림 프로세스 실행 시킴
        """
        from .util.buffer_process import Streaming
        from threading import Thread
        import time
    
        def main():
            camera_count = 0
            # main 반복 -> 버퍼 실행 및 rtsp 통신 이상으로 인해 끊기는 경우 재시작 하기 위해 반복
            # check time 통해 반복 시간 설정 가능

            while self.main_break_point:
                # cameraSetting 내부 정보 출력 / while 문 돌리면서 최신 정보 받아옴
                camera_dict = self.get_camera_info()

                # 카메라 정보 없거나 카메라 설정한 경우
                if camera_count == 0 or len(camera_dict) != camera_count:
                    self.camera_list.clear()
                    camera_count = len(camera_dict)

                    for obj in camera_dict.values():

                        name = obj['name']
                        rtsp = obj['rtsp']
                        self.camera_list.append((Streaming(), rtsp, name))

                # 정보가 있고, 새로 설정되지 않은 경우
                else:
                    for cam, rtsp, name  in self.camera_list:

                        if not cam.is_start:
                            cam.start(rtsp, name)
                        
                        self.ping[name] = cam.is_start
                        
                # cooltime : defalut 2sec
                time.sleep(self.check_time)

            # 반복문 break 된 경우 
            for cam, _, _ in self.camera_list:
                cam.end()

        # main thread 실행
        main_thread = Thread(target=main, args=())
        main_thread.daemon = True
        main_thread.start()

        return super().ready()