from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    confirmarcorreo = forms.EmailField(label='confirmar correo')
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'email','confirmarcorreo']
        
    
    pass
    

   