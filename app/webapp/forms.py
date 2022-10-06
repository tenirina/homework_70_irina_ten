from django import forms

from webapp.models import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'status', 'type')
