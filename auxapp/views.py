from django.shortcuts import render, redirect
from django.db.models import Min, Max
# Create your views here.
from auxapp.models import productos, categoria, subcategoria
from usuarioapp.models import monedero, usuarios
# Create your views here.
#from auxapp.funciones import *
from .forms import rangoForm, categoriaForm

def tienda(request, orden, mini, maxi, pag):
        nextpag = pag + 1
        prepag = pag -1
        identificado=False
        puntosuser=0
        if request.user.is_authenticated:
                identificado=True
                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
        form = rangoForm()
        if request.method == "POST":
                form = rangoForm(request.POST)
                mini=0
                if form.is_valid():
                        form_data = form.cleaned_data
                        mini = form_data.get("mini")
                        maxi = form_data.get("maxi")
                        
                        aux ='/tienda/'+ str(orden) + '/' + str(mini) + '/' + str(maxi) +'/1/' 
                        return redirect(aux)
                else:
                        mini = 0
                        maxi = 99999
        
        nproc = (pag*2) - 2
        fproc = nproc + 2
        if orden == 1:
                productosaux=productos.objects.filter(points__range=(mini, maxi)).order_by('points')[nproc:fproc]
        else:
                if orden == 2:
                        productosaux=productos.objects.filter(points__range=(mini, maxi)).order_by('-sold')[nproc:fproc]
        if not productosaux:
                pag=pag-1
                aux ='/tienda/'+ str(orden) + '/' + str(mini) + '/'+ str(maxi) + '/'  + str(pag) + '/' 
                return redirect(aux)        
        

        return render(request, "auxapp/tienda.html", {"productosaux":productosaux, "form":form, "mini":mini, "maxi":maxi, "orden":orden, "pag":pag, "nextpag":nextpag, "prepag":prepag, "identificado":identificado, "puntosuser":puntosuser})

def tiendasimple(request, orden, pag):
        nextpag = pag + 1
        prepag = pag -1
        #nproc multiplica la página actual con el número de productos mostrados en cada página
        nproc = (pag*2) - 2
        #fproc situa el último producto de la página
        fproc = nproc + 2
        identificado=False
        puntosuser=0
        if request.user.is_authenticated:
                identificado=True
                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
        if orden == 1:
                productosaux=productos.objects.all().order_by('points')[nproc:fproc]
        else:
                if orden == 2:
                        productosaux=productos.objects.all().order_by('-sold')[nproc:fproc]
        if not productosaux:
                pag=pag-1
                aux ='/tienda/'+ str(orden) + '/'  + str(pag) + '/' 
                return redirect(aux)  
        return render(request, "auxapp/tiendasimple.html", {"productosaux":productosaux, "orden":orden, "pag":pag, "nextpag":nextpag, "prepag":prepag,"identificado":identificado,"puntosuser":puntosuser})

def compra(request, produc):

        productosaux=productos.objects.get(id=produc)
        aux=produc
        puntosuser = 0
        compra=False
        identificado=False
        
        if request.user.is_authenticated:
                identificado=True

                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
                usuarioaux=usuarios.objects.get(name=current_user)
                if puntosuser > productosaux.points:
                        compra=True
                if usuarioaux.direction == None or usuarioaux.phone == None:
                        
                        auxx ='/ident/ampliacion/'+ str(usuarioaux.id)
                        return redirect(auxx)
                
        return render(request, "auxapp/compra.html",{"productosaux":productosaux, "aux":aux, "compra":compra, "produc":produc, "identificado":identificado, "puntosuser":puntosuser})

def tiendacategoria(request):

        
        identificado=False
        puntosuser=0
        if request.user.is_authenticated:
                identificado=True
                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
        categoriaaux=categoria.objects.all()
        return render(request, "auxapp/tiendacategoria.html",{"identificado":identificado, "categoriaaux":categoriaaux,"puntosuser":puntosuser})


def tiendasubcategoria(request, categoria):

        
        identificado=False
        puntosuser=0
        if request.user.is_authenticated:
                identificado=True
                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
        subcategoriaaux=subcategoria.objects.filter(category=categoria)
        return render(request, "auxapp/tiendasubcategoria.html",{"identificado":identificado, "subcategoriaaux":subcategoriaaux,"puntosuser":puntosuser})

def productocategoriasimple(request, categoria, pag):
        nextpag = pag + 1
        prepag = pag -1
        #nproc multiplica la página actual con el número de productos mostrados en cada página
        nproc = (pag*2) - 2
        #fproc situa el último producto de la página
        fproc = nproc + 2
        identificado=False
        puntosuser=0
        if request.user.is_authenticated:
                identificado=True
                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
        productosaux=productos.objects.filter(category=categoria).order_by('points')[nproc:fproc]
        return render(request, "auxapp/tiendaproductoscategoriasimple.html",{"identificado":identificado, "productosaux":productosaux, "pag":pag, "nextpag":nextpag, "prepag":prepag, "categoria":categoria,"puntosuser":puntosuser})

def productocategoria(request, categoria, orden, mini, maxi, pag):
        nextpag = pag + 1
        prepag = pag -1
        identificado=False
        puntosuser=0
        if request.user.is_authenticated:
                identificado=True
                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
        form = rangoForm()
        if request.method == "POST":
                form = rangoForm(request.POST)
                mini=0
                if form.is_valid():
                        form_data = form.cleaned_data
                        mini = form_data.get("mini")
                        maxi = form_data.get("maxi")
                        
                        aux ='/tienda/'+ str(orden) + '/' + str(mini) + '/' + str(maxi) +'/1/' 
                        return redirect(aux)
                else:
                        mini = 0
                        maxi = 99999
        
        nproc = (pag*2) - 2
        fproc = nproc + 2
        if orden == 1:
                productosaux=productos.objects.filter(category=categoria, points__range=(mini, maxi)).order_by('points')[nproc:fproc]
        else:
                if orden == 2:
                        productosaux=productos.objects.filter(category=categoria, points__range=(mini, maxi)).order_by('-sold')[nproc:fproc]
                
        

        return render(request, "auxapp/productocategoria.html", {"productosaux":productosaux, "form":form, "mini":mini, "maxi":maxi, "orden":orden, "pag":pag, "nextpag":nextpag, "prepag":prepag,"puntosuser":puntosuser, "identificado":identificado, "categoria":categoria})

def productosubcategoriasimple(request, categoria, pag):
        nextpag = pag + 1
        prepag = pag -1
        #nproc multiplica la página actual con el número de productos mostrados en cada página
        nproc = (pag*2) - 2
        #fproc situa el último producto de la página
        fproc = nproc + 2
        identificado=False
        puntosuser=0
        if request.user.is_authenticated:
                identificado=True
                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
        productosaux=productos.objects.filter(subcategory=categoria).order_by('points')[nproc:fproc]
        return render(request, "auxapp/productossubcategoriasimple.html",{"identificado":identificado, "productosaux":productosaux, "pag":pag, "nextpag":nextpag, "prepag":prepag, "categoria":categoria,"puntosuser":puntosuser})


def productosubcategoria(request, categoria, orden, mini, maxi, pag):
        nextpag = pag + 1
        prepag = pag -1
        identificado=False
        puntosuser=0
        if request.user.is_authenticated:
                identificado=True
                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
        form = rangoForm()
        if request.method == "POST":
                form = rangoForm(request.POST)
                mini=0
                if form.is_valid():
                        form_data = form.cleaned_data
                        mini = form_data.get("mini")
                        maxi = form_data.get("maxi")
                        
                        aux ='/tienda/'+ str(orden) + '/' + str(mini) + '/' + str(maxi) +'/1/' 
                        return redirect(aux)
                else:
                        mini = 0
                        maxi = 99999
        
        nproc = (pag*2) - 2
        fproc = nproc + 2
        if orden == 1:
                productosaux=productos.objects.filter(subcategory=categoria, points__range=(mini, maxi)).order_by('points')[nproc:fproc]
        else:
                if orden == 2:
                        productosaux=productos.objects.filter(subcategory=categoria, points__range=(mini, maxi)).order_by('-sold')[nproc:fproc]
                
        

        return render(request, "auxapp/productosubcategoria.html", {"productosaux":productosaux, "form":form, "mini":mini, "maxi":maxi, "orden":orden, "pag":pag, "nextpag":nextpag, "prepag":prepag, "identificado":identificado, "categoria":categoria,"puntosuser":puntosuser})


def tiendabusquedasimple(request, nombre, pag):
        nextpag = pag + 1
        prepag = pag -1
        #nproc multiplica la página actual con el número de productos mostrados en cada página
        nproc = (pag*2) - 2
        #fproc situa el último producto de la página
        fproc = nproc + 2
        identificado=False
        puntosuser=0
        if request.user.is_authenticated:
                identificado=True
                current_user=request.user
                monederoaux=monedero.objects.get(useremail=current_user.email)
                puntosuser = monederoaux.balance
        productosaux=productos.objects.filter(name__icontains=nombre).order_by('points')[nproc:fproc]
        if not productosaux:
                pag=pag-1
                aux ='/tienda/busqueda/'+ str(nombre) + '/' + str(pag) + '/' 
                return redirect(aux)
        return render(request, "auxapp/tiendabusquedasimple.html",{"identificado":identificado, "productosaux":productosaux, "pag":pag, "nextpag":nextpag, "prepag":prepag, "categoria":nombre,"puntosuser":puntosuser})