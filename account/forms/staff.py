import datetime
from django import forms
from django.contrib.auth.models import User, Group, Permission
from ..models import Profile, ProfileType


class StaffUserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'type': 'password', 'name': 'password', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'type': 'password', 'name': 'password2', 'placeholder': 'Repeat Password'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    is_active = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_superuser = forms.BooleanField(required=False)
    date_joined = forms.DateField(initial=datetime.date.today, required=False, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control form-control-user', 'type': 'hidden', 'placeholder': 'Select a Date of Registration', 'name': 'date_joined'}))

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StaffUserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'username', 'placeholder': 'User Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'aria-describedby': 'emailHelp', 'name': 'email', 'placeholder': 'Email Address'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'first_name', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'last_name', 'placeholder': 'Last Name'})

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']


class StaffUserUpdateForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)
    is_active = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_superuser = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'groups', 'is_active', 'is_staff', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super(StaffUserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'username', 'placeholder': 'User Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'aria-describedby': 'emailHelp', 'name': 'email', 'placeholder': 'Email Address'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'first_name', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'last_name', 'placeholder': 'Last Name'})
        self.fields['groups'].empty_label = None


class StaffProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control form-control-user', 'type': 'date', 'placeholder': 'Select a Date of Birth', 'name': 'date_of_birth'}))

    class Meta:
        model = Profile
        fields = ['country', 'city', 'address', 'gender', 'phone', 'degree', 'profileType', 'date_of_birth', 'photo']

    def __init__(self, *args, **kwargs):
        super(StaffProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'country', 'placeholder': 'Country'})
        self.fields['city'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'city', 'placeholder': 'City'})
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'address', 'placeholder': 'Address'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'gender', 'placeholder': 'Gender'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'phone', 'placeholder': 'Phone number'})
        self.fields['degree'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'degree', 'placeholder': 'Degree'})
        self.fields['gender'].empty_label = None
        self.fields['degree'].empty_label = None
        self.fields['profileType'].empty_label = None
