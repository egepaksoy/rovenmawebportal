from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
  first_name = forms.CharField(max_length=80, help_text="Kullanıcı Adı Soyadı")

  class Meta:
    model = User
    fields = ["first_name", 'username', 'password1', 'password2']
