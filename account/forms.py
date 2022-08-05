import datetime
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User, Group, Permission
from .models import Profile, ProfileType


# Account forms
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


# Admin forms
class AdminUserRegistrationForm(forms.ModelForm):
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
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=False)
    is_active = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_superuser = forms.BooleanField(required=False)
    date_joined = forms.DateField(
        initial=datetime.date.today,
        required=False,
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control form-control-user',
                'type': 'hidden',
                'placeholder': 'Select a Date of Registration',
                'name': 'date_joined'
            }
        ))

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdminUserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-user',
                                                     'type': 'text',
                                                     'name': 'username',
                                                     'placeholder': 'User Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user',
                                                  'type': 'text',
                                                  'aria-describedby': 'emailHelp',
                                                  'name': 'email',
                                                  'placeholder': 'Email Address'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control form-control-user',
                                                       'type': 'text',
                                                       'name': 'first_name',
                                                       'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control form-control-user',
                                                       'type': 'text',
                                                       'name': 'last_name',
                                                       'placeholder': 'Last Name'})

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']


class AdminUserEditForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),
                                           required=False)
    is_active = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_superuser = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'groups', 'is_active', 'is_staff', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super(AdminUserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-user',
                                                     'type': 'text',
                                                     'name': 'username',
                                                     'placeholder': 'User Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user',
                                                  'type': 'text',
                                                  'aria-describedby': 'emailHelp',
                                                  'name': 'email',
                                                  'placeholder': 'Email Address'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control form-control-user',
                                                       'type': 'text',
                                                       'name': 'first_name',
                                                       'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control form-control-user',
                                                       'type': 'text',
                                                       'name': 'last_name',
                                                       'placeholder': 'Last Name'})
        self.fields['groups'].empty_label = None


class AdminProfileEditForm(forms.ModelForm):
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

    class Meta:
        model = Profile
        fields = ['country', 'city', 'address', 'gender', 'phone', 'degree', 'profileType', 'date_of_birth', 'photo']

    def __init__(self, *args, **kwargs):
        super(AdminProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget.attrs.update({'class': 'form-control form-control-user',
                                                     'type': 'text',
                                                     'name': 'country',
                                                     'placeholder': 'Country'})
        self.fields['city'].widget.attrs.update({'class': 'form-control form-control-user',
                                                     'type': 'text',
                                                     'name': 'city',
                                                     'placeholder': 'City'})
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-user',
                                                     'type': 'text',
                                                     'name': 'address',
                                                     'placeholder': 'Address'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control form-control-user',
                                                     'type': 'text',
                                                     'name': 'gender',
                                                     'placeholder': 'Gender'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control form-control-user',
                                                     'type': 'text',
                                                     'name': 'phone',
                                                     'placeholder': 'Phone number'})
        self.fields['degree'].widget.attrs.update({'class': 'form-control form-control-user',
                                                     'type': 'text',
                                                     'name': 'degree',
                                                     'placeholder': 'Degree'})
        self.fields['gender'].empty_label = None
        self.fields['degree'].empty_label = None
        self.fields['profileType'].empty_label = None
