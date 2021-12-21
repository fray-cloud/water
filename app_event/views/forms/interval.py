from django import forms
from ...models import IntervalControl, interval_choice

class IntervalForm(forms.ModelForm):
    color_interval = forms.ChoiceField(choices=interval_choice, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    line_interval  = forms.ChoiceField(choices=interval_choice, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    text_interval  = forms.ChoiceField(choices=interval_choice, widget=forms.Select(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = IntervalControl
        fields = ['line_interval', 'color_interval', 'text_interval']