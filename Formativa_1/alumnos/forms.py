from django import forms
from .models import cliente

class registroForm(forms.ModelForm):
  class Meta:
      model = cliente
      fields = ['user','mail','confirmmail','password','confirmpassword',]