from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
    confirm_password = forms.CharField(widget=forms.TextInput())

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('confirm_password')
        
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('No coincide con la contraseña anterior')
