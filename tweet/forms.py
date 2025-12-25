from django import forms 
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import CustomUser



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
        



class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # use your custom user model
        fields = ('username', 'email')  # include any fields you want
       



