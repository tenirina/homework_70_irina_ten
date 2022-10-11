from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Issue, Status, Type


def max_length_validator(string):
    if len(string) < 4:
        raise ValidationError("The number of characters must be more than 3!")
    return string


class IssueForm(forms.ModelForm):
    summary = forms.CharField(max_length=200, required=True, label="Summary", validators=(max_length_validator, ))
    description = forms.CharField(max_length=1000, required=True, label="Description", widget=widgets.Textarea, validators=(max_length_validator, ))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Status")
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label="Type")

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']
