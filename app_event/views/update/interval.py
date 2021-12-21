from django.views.generic import UpdateView
from django.shortcuts import resolve_url
from django.shortcuts import get_object_or_404
from ...models import IntervalControl

class IntervalUpdateView(UpdateView):
    from ..forms.interval import IntervalForm
    
    model = IntervalControl
    context_object_name = 'interval'
    form_class = IntervalForm
    template_name = 'app_camera/form.html'
    
    def get_object(self):
        object = get_object_or_404(IntervalControl, camera_id=self.kwargs['camera_id'])
        return object

    def get_success_url(self):
        return resolve_url('app_camera:camera_detail', self.kwargs['camera_id'])

    def get_context_data(self, **kwargs):        
        context = super(IntervalUpdateView, self).get_context_data(**kwargs)
        context['title'] = '이벤트 정보'
        context['info'] = '이벤트 정보를 수정 합니다.'

        return context