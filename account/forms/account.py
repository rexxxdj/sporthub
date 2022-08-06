import datetime
from django import forms
from django.contrib.auth.models import User, Group, Permission
from ..models import Profile, ProfileType


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'type': 'password', 'name': 'password', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'type': 'password', 'name': 'password2', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'username', 'placeholder': 'User Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'aria-describedby': 'emailHelp', 'name': 'email', 'placeholder': 'Email Address'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'first_name', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'last_name', 'placeholder': 'Last Name'})

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']


class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'type': 'username', 'name': 'username', 'placeholder': 'Enter UserName...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'type': 'password', 'name': 'password', 'placeholder': 'Password'}))


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'username', 'placeholder': 'User Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'aria-describedby': 'emailHelp', 'name': 'email', 'placeholder': 'Email Address'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'first_name', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'last_name', 'placeholder': 'Last Name'})


class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control form-control-user', 'type': 'date', 'placeholder': 'Select a Date of Birth', 'name': 'date_of_birth'}))

    class Meta:
        model = Profile
        fields = ['country', 'city', 'address', 'gender', 'phone', 'degree', 'date_of_birth', 'photo']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'country', 'placeholder': 'Country'})
        self.fields['city'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'city', 'placeholder': 'City'})
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'address', 'placeholder': 'Address'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'gender', 'placeholder': 'Gender'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'phone', 'placeholder': 'Phone number'})
        self.fields['degree'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'degree', 'placeholder': 'Degree'})
        self.fields['gender'].empty_label = None
        self.fields['degree'].empty_label = None

