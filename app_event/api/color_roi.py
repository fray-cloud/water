from django.shortcuts import get_object_or_404
from ..models import ColorROIControl

from ninja import Router, ModelSchema


router = Router()

class ColorROIControlIn(ModelSchema):
    class Config:
        model = ColorROIControl
        model_fields = [
            'id',
            'camera',
            'color_x',
            'color_y',
            'color_w',
            'color_h',
        ]

class ColorROIControlOut(ModelSchema):
    class Config:
        model = ColorROIControl
        model_fields = [
            'camera',
            'color_x',
            'color_y',
            'color_w',
            'color_h',
        ]

@router.get('roi/{camera_id}/{color}', tags=['roi', 'color'], response=ColorROIControlOut)
def get_color_roi_control(request, camera_id:int, color:str):
    query = get_object_or_404(ColorROIControl, camera_id=camera_id, color_select=color)
    return query


# TODO ValueError: Cannot assign "1": "ColorROIControl.camera" must be a "CameraSetting" instance.
@router.put('roi/{camera_id}/{color}', tags=['roi', 'color'])
def update_color_roi_control(request, camera_id:int,color:str, payload: ColorROIControlIn):
    query = get_object_or_404(ColorROIControl, camera_id=camera_id, color_select=color)
    for attr, value in payload.dict().items():
        setattr(query, attr, value)
    query.save()
    return {'success' : True}
