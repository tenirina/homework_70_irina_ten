from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.forms import widgets

from webapp.models import Issue, Status, Type, Project


def max_length_validator(string):
    if len(string) < 4:
        raise ValidationError("The number of characters must be more than 3!")
    return string


class ControlDescription(BaseValidator):
    def __init__(self, limit_value=3, message="Enter more than 3 words in the task description."):
        super(ControlDescription, self).__init__(limit_value=limit_value, message=message)

    def compare(self, value, max_value):
        print(value, max_value)
        return value < max_value

    def clean(self, value):
        val = value.split(" ")
        x = len(val)
        return x


class IssueForm(forms.ModelForm):
    summary = forms.CharField(
        max_length=200,
        required=True,
        label="Summary",
        validators=(max_length_validator, ))
    description = forms.CharField(
        max_length=1000,
        required=True,
        label="Description",
        widget=widgets.Textarea,
        validators=(max_length_validator, ControlDescription()))
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label="Status")
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        label="Type")
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        label="Project"
    )

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type', 'project']


class SearchForm(forms.Form):
    search_value = forms.CharField(
        required=False,
        label='Search',
        max_length=100
    )


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        max_length=1000,
        required=True,
        label="Title",
        validators=(max_length_validator, ))
    description = forms.CharField(
        max_length=1000,
        required=False,
        label="Description",
        widget=widgets.Textarea,
        validators=(max_length_validator, ControlDescription()))
    started_at = forms.DateField(
        label="Date of started",
        required=True)
    finished_at = forms.DateField(
        label="Date of finished",
        required=False)

    class Meta:
        model = Project
        fields = ['title', 'description', 'started_at', 'finished_at']


class ProjectIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']
