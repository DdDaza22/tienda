from django import forms
from .models import categoria, subcategoria

class categoriaForm(forms.ModelForm):
    class Meta:
        model = subcategoria
        fields = ['name', 'category']


class rangoForm(forms.Form):

    mini=forms.IntegerField()
    maxi=forms.IntegerField()    
    