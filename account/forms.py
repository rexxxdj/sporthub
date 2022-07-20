from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-user',
            'type':'username',
            'name':'username',
            'placeholder':'Enter UserName...'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control form-control-user',
            'type':'password',
            'name':'password',
            'placeholder':'Password'
        }
    ))
