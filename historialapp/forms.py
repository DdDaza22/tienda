from django import forms

from .models import pedidos

class pedidosForm(forms.ModelForm):
    class Meta:
        model = pedidos
        fields = ['user', 'prod']