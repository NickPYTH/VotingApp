from django import forms

class PasswordForm(forms.Form):
    password    = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Пароль"
        }))
    