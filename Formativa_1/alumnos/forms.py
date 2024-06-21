from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django import forms


    

class SignUpForm(UserCreationForm):
    confirmarcorreo = forms.EmailField(label='confirmar correo')
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'email','confirmarcorreo']
        
    
    pass
    

class UserProfileForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['email','password']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user