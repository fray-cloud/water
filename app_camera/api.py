import cv2

from ninja import Router
from .models import CameraCapture, CameraSetting
from django.conf import settings
import os

router = Router()

@router.get('/frame/{camera_id}', tags=['camera', 'setting'])
def get_frame(request, camera_id :int):
    from .apps import AppCameraConfig
    cam_name = CameraSetting.objects.get(id=camera_id).camera_name
    data = dict()
    
    for cam, rtsp, name in AppCameraConfig.camera_list:
        if name == cam_name:
            data = cam.q.get()
    if len(data) == 0 :
        print('camera data missing')
        return {'is_saved' : False}

    is_alive = data['is_alive']    
    if not is_alive:
        print(f'is_alive : {is_alive}')
        return {'is_saved' : False}
        
    image = data['image']
    path = os.path.join(settings.MEDIA_ROOT, 'capture', f'capture_{data["name"]}.jpg')
    cv2.imwrite(path, image)
    path = os.path.join(settings.MEDIA_URL, 'capture', f'capture_{data["name"]}.jpg')
    try:
        obj = CameraCapture.objects
        sub = obj.filter(camera_id=camera_id)
        if len(sub) == 0:
            raise 'empty query'
        sub.update(
            camera_capture = path
        )
    except:
        obj.create(
            camera_id = camera_id,
            camera_capture = path,
        )
    info = dict()
    info['is_saved'] = True
    
    info['path'] = path
    return info


@router.get('/check_time', tags=['camera', 'setting'])
def get_frame_check_time(request):
    from .apps import AppCameraConfig
    check_time = AppCameraConfig.check_time
    return {'check_time': check_time}

@router.post('/check_time/{check_time}', tags=['camera', 'setting'])
def set_frame_check_time(request, check_time:int):
    from .apps import AppCameraConfig
    AppCameraConfig.check_time = check_time

    return {'set_check_time' : 'success'}

@router.get('/ping/{camera_id}')
def get_ping(request, camera_id:int):
    from .apps import AppCameraConfig
    ping = AppCameraConfig.ping
    camera = CameraSetting.objects.get(id=camera_id)
    ping = ping[camera.camera_name]
    return {'ping': ping}