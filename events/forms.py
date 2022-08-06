from django.forms import ModelForm, DateInput
from events.models import Event
from django import forms


class EventCreateForm(forms.ModelForm):
    start_date = forms.DateField(required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control form-control-user', 'type': 'date', 'placeholder': 'Select a Date of Start Event', 'name': 'start_date'}))
    end_date = forms.DateField(required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control form-control-user', 'type': 'date', 'placeholder': 'Select a Date of End Event', 'name': 'end_date'}))
    subscribe_date = forms.DateField(required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control form-control-user', 'type': 'date', 'placeholder': 'Select a Date of Last Subscribe Date', 'name': 'subscribe_date'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'subscribe_date']

    def __init__(self, *args, **kwargs):
        super(EventCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'title', 'placeholder': 'Title'})
        self.fields['description'].widget.attrs.update({'style': 'height: 400px; border-radius: 2rem;', 'class': 'form-control form-control-user', 'type': 'text', 'name': 'description', 'placeholder': 'Description'})


class EventUpdateForm(forms.ModelForm):
    start_date = forms.DateField(required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control form-control-user', 'type': 'date', 'placeholder': 'Select a Date of Start Event', 'name': 'start_date'}))
    end_date = forms.DateField(required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control form-control-user', 'type': 'date', 'placeholder': 'Select a Date of End Event', 'name': 'end_date'}))
    subscribe_date = forms.DateField(required=True, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control form-control-user', 'type': 'date', 'placeholder': 'Select a Date of Last Subscribe Date', 'name': 'subscribe_date'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'subscribe_date']

    def __init__(self, *args, **kwargs):
        super(EventUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control form-control-user', 'type': 'text', 'name': 'title', 'placeholder': 'Title'})
        self.fields['description'].widget.attrs.update({'style': 'height: 400px; border-radius: 2rem;', 'class': 'form-control form-control-user', 'type': 'text', 'name': 'description', 'placeholder': 'Description'})
