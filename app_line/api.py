from ninja import Router
from app_camera.models import CameraSetting
from app_event.models import LineROIControl, LineParamControl
from .util.detect import Line

router = Router()

@router.get('/result/{camera_id}', tags=['line', 'detect'])
def get_line_result(request, camera_id:int):
    from app_camera.apps import AppCameraConfig
    try:
        cam_name = CameraSetting.objects.get(id=camera_id).camera_name
    except:
        return {'is_saved' : False}

    try:
        roi_object = LineROIControl.objects
        roi_control = roi_object.filter(camera_id=camera_id)
        if len(roi_control) == 0:
            raise f'query empty {roi_control}'
    except:
        roi_object.create(camera_id=camera_id)
        roi_control = roi_object.filter(camera_id=camera_id)

    try:
        param_object = LineParamControl.objects
        param = param_object.filter(camera_id=camera_id)
        if len(param) == 0:
            raise f'query empty {param}'
    except:
        param_object.create(camera_id=camera_id)
        param = param_object.filter(camera_id=camera_id)

    data = dict()

    for cam, rtsp, name in AppCameraConfig.camera_list:
        if name == cam_name:
            data = cam.q.get()
        
    if len(data) == 0:
        print('color data missing')
        print(AppCameraConfig.camera_list)
        return {'is_saved' : False}

    is_alive = data['is_alive']    
    if not is_alive:
        print(f'is_alive : {is_alive}')
        return {'is_saved' : False}

    image = data['image']
    roi_control = roi_control[0]
    roi = roi_control.line_x, roi_control.line_y, roi_control.line_w, roi_control.line_h
    param = param[0]
    JSON = Line.main(image, roi, (param.line_gaussian_ksize, param.line_gaussian_ksize), param.line_gaussian_sigmaX, param.line_canny_threashold1, param.line_canny_threashold2, param.line_theta, param.line_hough_threshold, param.line_hough_minLineLength) 

    # log save
    from app_log.models import LineLog
    log = LineLog.objects
    log.create(
        camera_id = camera_id,
        length = JSON['LENGTH'],
    )

    return JSON