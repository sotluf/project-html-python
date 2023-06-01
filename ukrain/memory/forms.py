from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('country','description','point')
        widgets = {'author': forms.HiddenInput()}