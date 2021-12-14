from django.db.models.fields import NullBooleanField
from .util.buffer import Camera
from ninja import Router
from .models import CameraCapture, CameraSetting
from django.conf import settings
import os

router = Router()
cam = Camera()

def get_camera_info(pk):
    cam_info = dict()
    try:
        obj = CameraSetting.objects.all()
        obj = obj.filter(id=pk)
        cam_info['camera_name'] = obj.camera_name
        cam_info['rtsp'] = str(obj)
        return cam_info
    except:
        print('not query')
        return

@router.get('/frame/{camera_id}')
def get_frame(request, camera_id :int):
    info = get_camera_info(camera_id)
    if info is None:
        return {'is_saved' : False}

    else:
        is_alive = cam.start(info['rtsp'], info['camera_name'])
        
        if not is_alive:
            return {'is_saved' : False}

        image = cam.get_frame()
        path = os.path.join(settings.MEDIA_ROOT, 'capture', f'capture_{info["camera_name"]}.jpg')
        cam.save(path, image)

        try:
            obj = CameraCapture.objects
            obj = obj.filter(camera_id=camera_id)
            obj.update(
                camera_capture = path
            )
            
        except:
            obj.create(
                camera_id = camera_id,
                camera_capture = path,
            )

        info['is_saved'] = True
        path = os.path.join(settings.MEDIA_URL, 'capture', f'capture_{info["camera_name"]}.jpg')
        info['path'] = path
        return info

