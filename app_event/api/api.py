from django.http.response import Http404
from django.shortcuts import get_object_or_404

from ninja import Router, ModelSchema
from ..models import IntervalControl
from .color_roi import router as color_roi_router
from .line_roi import router as line_roi_router
from .text_roi import router as text_roi_router

router = Router()
router.add_router('color/', color_roi_router)
router.add_router('line/', line_roi_router)
router.add_router('text/', text_roi_router)

class IntervalControlIn(ModelSchema):
    class Config:
        model = IntervalControl
        model_fields = [
            'id',
            'camera',
            'color_interval',
            'line_interval',
            'text_interval',
        ]

class IntervalControlOut(ModelSchema):
    class Config:
        model = IntervalControl
        model_fields = [
            'camera',
            'color_interval',
            'line_interval',
            'text_interval',
        ]

@router.get('interval/{camera_id}', tags=['setting'], response=IntervalControlOut)
def get_interval_control(request, camera_id:int):
    try:
        query = get_object_or_404(IntervalControl, camera_id=camera_id)
    except Http404:
        print('not query')
        IntervalControl.objects.create(
            camera_id=camera_id,
        )
        query = get_object_or_404(IntervalControl, camera_id=camera_id)
    return query

@router.put('interval/{camera_id}', tags=['setting'])
def post_interval_control(request, camera_id:int, payload:IntervalControlIn):
    query = get_object_or_404(IntervalControl, camera_id=camera_id)
    for attr, value in payload.dict().items():
        setattr(query, attr, value)
    query.save()
    return {'success' : True}

