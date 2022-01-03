from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.models import ModelForm
from .models import *


class CreateUserForm(UserCreationForm):
    """
    This class is used to create the registration page.
    :param request: it's a form request from user.
    """
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']

class SupportForm(ModelForm):
    """
    This class is used to create the contact us form.
    :param request: it's a form request from user.
    """
    class Meta:
        model= Support
        fields= ['first_name', 'last_name', 'email', 'message']

class PostForm(ModelForm):
    """
    This class is used to create the Post form.
    :param request: it's a form request from user.
    """
    class Meta:
        model= Post
        fields= "__all__"

        labels = {
            'poster': 'Your Name',
            'title': 'Post Title'
        }
    