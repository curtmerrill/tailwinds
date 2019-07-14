from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Pilot

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Pilot
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Pilot
        fields = ('username', 'email')
