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
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'first_name'
            }
        ))
    last_name = forms.CharField(
        required=False,
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
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'country'
            }
        ))
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'city'
            }
        ))
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'address'
            }
        ))
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'phone'
            }
        ))
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control form-control-user',
                'type': 'date',
                'placeholder': 'Select a Date of Birth',
                'name': 'date_of_birth'
            }
        ))
    gender = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=Profile.GENDER_CHOICES,
            attrs={
                'class': 'form-control form-control-user',
                'type': 'text',
                'name': 'gender'
            }
        ))
    photo = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'btn btn-primary btn-sm',
                'accept': 'image/',
                'title': ' '
            }
        ))

    class Meta:
        model = Profile
        fields = ('country', 'city', 'address', 'gender', 'date_of_birth', 'phone', 'photo')
