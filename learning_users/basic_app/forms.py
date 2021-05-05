from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfoForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),max_length=20)

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfoForm
        fields = ('portfolio_site','profile_pic')
