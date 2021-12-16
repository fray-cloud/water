from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from ..models import CameraSetting, CameraCapture

class CameraDetailView(DetailView):
    model = CameraSetting
    context_object_name = 'camera'
    template_name = 'app_camera/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CameraDetailView, self).get_context_data(**kwargs)
        context['media'] = get_object_or_404(CameraCapture, pk=self.kwargs['pk'])
        # context['roi'] = get_object_or_404(ROIControl, pk=self.kwargs['pk'])
        # context['interval'] = get_object_or_404(IntervalControl, pk=self.kwargs['pk'])
        return context