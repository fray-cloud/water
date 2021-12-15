from django.views.generic import CreateView
from django.shortcuts import resolve_url

class CameraCreateView(CreateView):
    from ..models import CameraSetting
    from .forms import CameraForm

    model = CameraSetting
    context_object_name = 'camera'
    form_class = CameraForm
    template_name = 'app_camera/camera_form.html'

    def get_success_url(self):
        return resolve_url('app_camera:detail', self.kwargs['pk'])