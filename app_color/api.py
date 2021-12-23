from ninja import Router
from app_camera.models import CameraSetting
from app_event.models import ColorROIControl
from .util.detect import Color

router = Router()
color = Color()


@router.get('/result/{camera_id}', tags=['color', 'detect'])
def get_color_result(request, camera_id:int):
    from app_camera.apps import AppCameraConfig
    try:
        cam_name = CameraSetting.objects.get(id=camera_id).camera_name
    except:
        return {'is_saved' : False}
    
    try:
        roi_object = ColorROIControl.objects
        roi_control = roi_object.filter(camera_id=camera_id)
        if len(roi_control) == 0:
            raise f'query empty {roi_control}'
    except:
        roi_object.create(camera_id=camera_id, color_select='red')
        roi_object.create(camera_id=camera_id, color_select='green')
        roi_object.create(camera_id=camera_id, color_select='blue')
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
    roi_list = list()
    for roi in roi_control:
        roi_list.append((roi.color_x, roi.color_y, roi.color_w, roi.color_h))
    
    JSON = color.color(image, roi_list)

    # log save
    from app_log.models import ColorLog
    log = ColorLog.objects
    log.create(
        camera_id = camera_id,
        red = JSON['color']['red'],
        green = JSON['color']['green'],
        blue = JSON['color']['blue'],
    )

    return JSON

