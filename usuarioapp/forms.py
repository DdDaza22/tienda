from django import forms
from django.contrib.auth.models import User
from .models import usuarios

class registroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        
class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = ['direction', 'phone']



class identForm(forms.Form):
    username=forms.CharField(max_length=48)
    password=forms.CharField(max_length=48)    
    