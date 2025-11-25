from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=Profile.USER_ROLES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'company_name', 'bio']
