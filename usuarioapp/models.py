from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.
#aquí se crea la clase productos
class usuarios(models.Model):
    #id = models.AutoField(primary_key=True)
    name=models.OneToOneField(User, on_delete=models.CASCADE)
    
     
    direction=models.CharField(max_length=48, null=True, blank=True)
    phone=models.IntegerField(null=True, blank=True)
    


    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'

    def __str__(self):
        return self.name.username

class monedero(models.Model):
   
    useremail=models.EmailField(primary_key=True, max_length=48)
    balance=models.IntegerField(default=0)

    def __str__(self):
        return self.useremail

class ident(models.Model):
    email=models.EmailField(max_length=48)
    password=models.CharField(max_length=48) 