from django import forms
from ...models import LineROIControl, LineParamControl

class LineROIControlForm(forms.ModelForm):
    line_x = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    line_y = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    line_w = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    line_h = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = LineROIControl
        fields = ['line_x', 'line_y', 'line_w', 'line_h']


class LineParamControlForm(forms.ModelForm):
    line_gaussian_ksize      = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    line_gaussian_sigmaX     = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    line_canny_threashold1   = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    line_canny_threashold2   = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    line_theta               = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    line_hough_threshold     = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    line_hough_minLineLength = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = LineParamControl
        fields = [
            'line_gaussian_ksize', 
            'line_gaussian_sigmaX',
            'line_canny_threashold1', 
            'line_canny_threashold2',
            'line_theta', 
            'line_hough_threshold', 
            'line_hough_minLineLength'
        ]