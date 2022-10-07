from django import forms
from django.forms import widgets

from webapp.models import Issue, Status, Type


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label="Summary")
    description = forms.CharField(max_length=1000, required=True, label="Descroption", widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Status")
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label="Type")


