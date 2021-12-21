from django import forms
from ...models import TextROIControl

class TextROIControlForm(forms.ModelForm):
    text_x = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    text_y = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    text_w = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    text_h = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = TextROIControl
        fields = ['text_x', 'text_y', 'text_w', 'text_h']