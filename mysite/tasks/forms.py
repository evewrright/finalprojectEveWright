from django import forms
from .models import Task


class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'student']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
        }
