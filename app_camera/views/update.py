from django.views.generic import UpdateView
from django.shortcuts import resolve_url

class CameraUpdateView(UpdateView):
    from ..models import CameraSetting
    from .forms import CameraForm
    model = CameraSetting
    context_object_name = 'camera'
    form_class = CameraForm
    template_name = 'app_camera/form.html'
    
    def get_success_url(self):
        return resolve_url('app_camera:camera_detail', self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(CameraUpdateView, self).get_context_data(**kwargs)
        context['info'] = '카메라 정보를 수정 합니다.'

        return context