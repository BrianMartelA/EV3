from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class cliente(models.Model):
    user = models.CharField(primary_key=True,max_length =10)
    password = models.CharField(blank=False, null=False, max_length=20)
    confirmpassword =models.CharField(blank=False, null=False, max_length=20, default='ExamplePassword')
    mail = models.CharField(blank=False, null=False, max_length=20)
    confirmmail = models.CharField(blank=False, null=False, max_length=20, default='default@example.com')
    def __str__(self):
        return self.user
    
class Registro_cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
    def __str__(self):
        return self.user.username