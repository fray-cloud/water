from ninja import Router
from django.core import serializers

router = Router()

@router.get('/color/{camera_id}', tags=['color', 'log'])
def get_color_log(request, camera_id:int):
    """
    카메라 색상 인식결과 로그를 가져온다.
    - input : camera_id
    - output : color_log
    """
    from .models import ColorLog
    try:
        log = ColorLog.objects.get(camera_id=camera_id)
        log = serializers('json', log)
        log['is_saved'] = True
        return log
    except:
        return {'is_saved': False}

@router.get('/line/{camera_id}', tags=['line', 'log'])
def get_line_log(request, camera_id:int):
    """
    카메라 선 인식결과 로그를 가져온다.
    - input : camera_id
    - output : line_log
    """
    from .models import LineLog
    try:
        log = LineLog.objects.get(camera_id=camera_id)
        log = serializers('json', log)
        log['is_saved'] = True
        return log
    except:
        return {'is_saved': False}

@router.get('/text/{camera_id}', tags=['text', 'log'])
def get_text_log(request, camera_id:int):
    """
    카메라 문자 인식결과 로그를 가져온다.
    - input : camera_id
    - output : text_log
    """
    from .models import TextLog
    try:
        log = TextLog.objects.get(camera_id=camera_id)
        log = serializers('json', log)
        log['is_saved'] = True
        return log
    except:
        return {'is_saved': False}

