from django.shortcuts import get_object_or_404
from ..models import TextROIControl

from ninja import Router, ModelSchema

router = Router()

class TextROIControlIn(ModelSchema):
    class Config:
        model = TextROIControl
        model_fields = [
            'id',
            'camera',
            'text_x',
            'text_y',
            'text_w',
            'text_h',
        ]

class TextROIControlOut(ModelSchema):
    class Config:
        model = TextROIControl
        model_fields = [
            'camera',
            'text_x',
            'text_y',
            'text_w',
            'text_h',
        ]

@router.get('roi/{camera_id}', tags=['roi', 'text'], response=TextROIControlOut, url_name='text_roi')
def get_text_roi_control(request, camera_id:int):
    query = get_object_or_404(TextROIControl, camera_id=camera_id)
    return query

@router.put('roi/{camera_id}', tags=['roi', 'text'])
def update_text_roi_control(request, camera_id:int, payload: TextROIControlIn):
    query = get_object_or_404(TextROIControl, camera_id=camera_id)
    for attr, value in payload.dict().items():
        setattr(query, attr, value)
    query.save()
    return {'success' : True}

# @router.post('roi/{camera_id}', tags=['roi', 'text'])
# def post_text_roi_control(request, camera_id:int):
#     pass