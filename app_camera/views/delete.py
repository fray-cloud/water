from django.views.generic import View
from django.shortcuts import resolve_url

class CameraDeleteView(View):
    def get(self, request, pk):
        from ..models import CameraSetting
        camera = CameraSetting.objects
        get_camera = camera.filter(id=pk)
        get_camera.delete()
        
        return resolve_url('dashboard')