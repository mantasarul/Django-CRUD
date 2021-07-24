from django import forms
from django.forms import widgets
from app.models import Password

class PasswordForm(forms.ModelForm):

    class Meta:
        model = Password
        fields = '__all__'
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailField(attrs={'class': 'form-control'}),
        #     'password': forms.TextInput(attrs={'class': 'form-control'}),
        # }