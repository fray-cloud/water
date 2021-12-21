from django.http.response import Http404
from django.shortcuts import get_object_or_404
from ..models import LineROIControl, LineParamControl

from ninja import Router, ModelSchema


router = Router()

class LineROIControlIn(ModelSchema):
    class Config:
        model = LineROIControl
        model_fields = [
            'id',
            'camera',
            'line_x',
            'line_y',
            'line_w',
            'line_h',
        ]

class LineROIControlOut(ModelSchema):
    class Config:
        model = LineROIControl
        model_fields = [
            'camera',
            'line_x',
            'line_y',
            'line_w',
            'line_h',
        ]

@router.get('roi/{camera_id}', tags=['roi', 'line'], response=LineROIControlOut, url_name='line_roi')
def get_line_roi_control(request, camera_id:int):
    query = get_object_or_404(LineROIControl, camera_id=camera_id)
    return query

@router.put('roi/{camera_id}', tags=['roi', 'line'])
def update_line_roi_control(request, camera_id:int, payload: LineROIControlIn):
    query = get_object_or_404(LineROIControl, camera_id=camera_id)
    for attr, value in payload.dict().items():
        setattr(query, attr, value)
    query.save()
    return {'success' : True}

# @router.post('roi/{camera_id}', tags=['roi', 'line'])
# def post_line_roi_control(request, camera_id:int):
#     pass


class LineParamControlIn(ModelSchema):
    class Config:
        model = LineParamControl
        model_fields = [
            'id',
            'camera', 
            'line_gaussian_ksize',
            'line_gaussian_sigmaX',
            'line_canny_threashold1',
            'line_canny_threashold2',
            'line_theta',
            'line_hough_threshold',
            'line_hough_minLineLength',
            ]

class LineParamControlOut(ModelSchema):
    class Config:
        model = LineParamControl
        model_fields = [
            'camera', 
            'line_gaussian_ksize',
            'line_gaussian_sigmaX',
            'line_canny_threashold1',
            'line_canny_threashold2',
            'line_theta',
            'line_hough_threshold',
            'line_hough_minLineLength',
            ]

@router.get('param/{camera_id}', tags=['parameter', 'line'], response=LineParamControlOut)
def get_line_param_control(request, camera_id:int):
    query = get_object_or_404(LineParamControl, camera_id=camera_id)
    return query

@router.put('param/{camera_id}', tags=['parameter', 'line'])
def update_line_param_control(request, camera_id:int, payload: LineParamControlIn):
    query = get_object_or_404(LineParamControl, camera_id=camera_id)
    for attr, value in payload.dict().items():
        setattr(query, attr, value)
    query.save()
    return {'success' : True}

# @router.post('param/{camera_id}', tags=['roi', 'line'])
# def post_line_param_control(request, camera_id:int):
#     pass