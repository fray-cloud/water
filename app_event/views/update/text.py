from django.views.generic import UpdateView
from django.shortcuts import resolve_url
from django.shortcuts import get_object_or_404
from ...models import TextROIControl

class TextROIControlUpdateView(UpdateView):
    from ..forms.text import TextROIControlForm
    model = TextROIControl
    context_object_name = 'text'
    form_class = TextROIControlForm
    template_name = 'app_event/forms/roi_form_text.html'
    
    def get_object(self):
        object = get_object_or_404(TextROIControl, camera_id=self.kwargs['camera_id'])
        return object

    def get_success_url(self):
        return resolve_url('app_camera:camera_detail', self.kwargs['camera_id'])

    def get_context_data(self, **kwargs):
        from app_camera.models import CameraCapture
        context = super(TextROIControlUpdateView, self).get_context_data(**kwargs)
        context['title'] = '문자 영역 정보'
        context['info'] = '문자 영역 정보를 수정 합니다.'
        context['media'] = get_object_or_404(CameraCapture, pk=self.kwargs['camera_id'])
        return context