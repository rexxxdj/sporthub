from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-user',
            'type': 'username',
            'name': 'username',
            'placeholder': 'Enter UserName...'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'type': 'password',
            'name': 'password',
            'placeholder': 'Password'
        }
    ))


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        error_messages={'required': 'Enter Your UserName'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'username',
                'placeholder': 'User Name'
            }
        ))
    email = forms.CharField(
        error_messages={'required': 'Enter Your Email'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'aria-describedby': 'emailHelp',
                'name': 'email',
                'placeholder': 'Email Address'
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'type': 'password',
            'name': 'password',
            'placeholder': 'Password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'type': 'password',
            'name': 'password2',
            'placeholder': 'Repeat Password'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']


class UserEditFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditeFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
