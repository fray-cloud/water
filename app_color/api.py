from ninja import Router
from util.detect import Color
from models import ColorSetting
from app_camera.models import CameraSetting

router = Router()

@router.get('result/{camera_id}')
def get_color_result(request, camera_id:int):
    from app_camera.apps import AppCameraConfig
    