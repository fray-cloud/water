from django import forms
from ...models import ColorROIControl, color_choice

class ColorROIControlForm(forms.ModelForm):
    color_choices = forms.ChoiceField(choices=color_choice, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    color_x       = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    color_y       = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    color_w       = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    color_h       = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = ColorROIControl
        fields = ['color_choices', 'color_x', 'color_y', 'color_w', 'color_h']