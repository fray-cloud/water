from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from ..models import CameraSetting, CameraCapture
from app_event.models import IntervalControl, ColorROIControl, LineROIControl, TextROIControl

class CameraDetailView(DetailView):
    model = CameraSetting
    context_object_name = 'camera'
    template_name = 'app_camera/detail.html'

    def get(self, request, *args, **kwargs):
        from ..api import get_frame
        json = get_frame(request, self.kwargs['pk'])
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(CameraDetailView, self).get_context_data(**kwargs)
        context['media'] = get_object_or_404(CameraCapture, pk=self.kwargs['pk'])
        # context['color_roi'] = get_object_or_404(ColorROIControl, pk=self.kwargs['pk'])
        # context['line_roi'] = get_object_or_404(LineROIControl, pk=self.kwargs['pk'])
        # context['text_roi'] = get_object_or_404(TextROIControl, pk=self.kwargs['pk'])
        # context['interval'] = get_object_or_404(IntervalControl, pk=self.kwargs['pk'])
        return context