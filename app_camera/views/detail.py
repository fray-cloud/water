from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from ..models import CameraSetting, CameraCapture

class CameraDetailView(DetailView):
    model = CameraSetting
    context_object_name = 'camera'
    template_name = 'app_camera/detail.html'

    def get(self, request, *args, **kwargs):
        from ..api import get_frame
        json = get_frame(request, self.kwargs['pk'])
        print(json)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(CameraDetailView, self).get_context_data(**kwargs)
        context['media'] = get_object_or_404(CameraCapture, pk=self.kwargs['pk'])
        # context['roi'] = get_object_or_404(ROIControl, pk=self.kwargs['pk'])
        # context['interval'] = get_object_or_404(IntervalControl, pk=self.kwargs['pk'])
        return context