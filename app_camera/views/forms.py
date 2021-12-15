from django import forms

class CameraForm(forms.ModelForm):
    camera_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    camera_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    camera_pw = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    camera_ip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    camera_port = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    camera_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        from ..models import CameraSetting
        model = CameraSetting
        fields = ['camera_name', 'camera_id', 'camera_pw', 'camera_ip', 'camera_port', 'camera_url', ]