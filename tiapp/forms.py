from django import forms





class buscarForm(forms.Form):

    buscar=forms.CharField(max_length=100)
   
    