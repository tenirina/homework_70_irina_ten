from django import forms
from django.forms import widgets

from webapp.models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']
