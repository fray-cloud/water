from django.shortcuts import render
from app_camera.models import CameraSetting

# Create your views here.
def dashboard(request):
    camera = CameraSetting.objects.all()
    if camera.count() == 0:
        is_exsist_camera = False
    else:
        is_exsist_camera = True
    context = {
        'camera' : camera,
        'is_exsist_camera' : is_exsist_camera,
    }
    return render(request=request, template_name='app_dashboard/dashboard.html', context=context)