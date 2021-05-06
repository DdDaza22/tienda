from django.shortcuts import render, HttpResponse, redirect
from auxapp.models import categoria, productos
from tiapp.forms import buscarForm


# Create your views here.

def home(request):
        identificado=False
        form = buscarForm()
        if request.method == "POST":
                form = buscarForm(request.POST)
                
                if form.is_valid():
                        form_data = form.cleaned_data
                        buscar = form_data.get("buscar")
                        aux = '/tienda/busqueda/' + str(buscar) + '/1/'
                        return redirect(aux)
        
        productosaux=productos.objects.all().order_by('-sold')[0:2]
        categoriaaux=categoria.objects.all()[0:3]
        if request.user.is_authenticated:
                identificado=True

        return render(request, "tiapp/home.html", {"identificado":identificado, "productosaux":productosaux, "categoriaaux":categoriaaux, "form":form})


          

def tiendae(request):

          return render(request, "tiapp/tiendae.html")
          


          



def retorno(request):

          return render(request, "tiapp/retorno.html")

def inicio(request):

          return render(request, "tiapp/inicio.html")

def aux(request):
        return render(request, "tiapp/aux.html")