from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', required=True)
    password = forms.CharField(label='Password', required=True)
    next = forms.CharField(required=False, widget=forms.HiddenInput)


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password confirm', strip=False, required=True, widget=forms.PasswordInput)
    email = forms.CharField(label='Email', required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Incorrect password')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not (first_name or last_name):
            raise ValidationError('You must enter the first_name or last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
