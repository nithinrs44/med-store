from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from .models import records

from django import forms

from django.forms.widgets import PasswordInput,TextInput


# - register/create a user

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
    
        model = User
        fields = ['username','password1','password2']
    
# - login a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    

# - Create a record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = records
        fields = ['medicine_name', 'medicine_des']


# - Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = records
        fields = ['medicine_name', 'medicine_des']
        
# - Search fn


class SearchForm(forms.Form):
    q = forms.CharField(label='q', max_length=100)

