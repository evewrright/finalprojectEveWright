from django import forms
from .models import Appointment
from datetime import date
from django.forms.widgets import SplitDateTimeWidget
from django.forms.widgets import DateInput, TimeInput
from django.utils.html import format_html


class DateTimeSplitWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            DateInput(attrs={'class': 'form-control datepicker'}),
            TimeInput(attrs={'class': 'form-control timepicker'}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.date(), value.time()]
        return [None, None]

    def format_output(self, rendered_widgets):
        return format_html('<div class="datetime-split-widget">{}</div>', '<br>'.join(rendered_widgets))


class ApptsForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['student', 'topic', 'note', 'occurred']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'topic': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
            'occurred': DateTimeSplitWidget()
        }
