from ninja import Router
from app_camera.models import CameraSetting
from app_event.models import TextROIControl
from .util.detect import Text


router = Router()
text = Text()

@router.get('/result/{camera_id}', tags=['text', 'detect'])
def get_text_result(request, camera_id:int):
    from app_camera.apps import AppCameraConfig
    try:
        cam_name = CameraSetting.objects.get(id=camera_id).camera_name
    except:
        return {'is_saved' : False}
    
    try:
        roi_object = TextROIControl.objects
        roi_control = roi_object.filter(camera_id=camera_id)
        if len(roi_control) == 0:
            raise f'query empty {roi_control}'
    except:
        roi_object.create(camera_id=camera_id)
        roi_control = roi_object.filter(camera_id=camera_id)
    data = dict()
    
    for cam, rtsp, name in AppCameraConfig.camera_list:
        if name == cam_name:
            data = cam.q.get()

    if len(data) == 0 :
        print('color data missing')
        print(AppCameraConfig.camera_list)
        return {'is_saved' : False}

    is_alive = data['is_alive']    
    if not is_alive:
        print(f'is_alive : {is_alive}')
        return {'is_saved' : False}

    image = data['image']
    roi_control = roi_control[0]
    roi = roi_control.text_x, roi_control.text_y, roi_control.text_w, roi_control.text_h

    JSON = text.text(image, roi)
    text_list = JSON['text_rec']
    text_str = ','.join(text_list)


    # log save
    from app_log.models import TextLog
    log = TextLog.objects
    log.create(
        camera_id = camera_id,
        texts = text_str
    )

    return JSON
