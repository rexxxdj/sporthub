from django import forms
from django.contrib.admin.widgets import AdminDateWidget
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
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'username'
            }
        ))
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'email'
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'first_name'
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'last_name'
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileEditFrom(forms.ModelForm):
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'required': '',
                'name': 'country'
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'required': '',
                'name': 'city'
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'required': '',
                'name': 'address'
            }
        ))
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'required': '',
                'name': 'phone'
            }
        ))
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control form-control-user',
                'type': 'date',
                'placeholder': 'Select a Date of Birth',
                'required': '',
                'name': 'date_of_birth'
            }
        ))
    gender = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'required': '',
                'name': 'gender'
            }
        ))
    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'btn btn-primary btn-sm',
                'required': '',
                'accept': 'image/'
            }
        ))

    class Meta:
        model = Profile
        fields = ('country', 'city', 'address', 'gender', 'date_of_birth', 'phone', 'photo')
