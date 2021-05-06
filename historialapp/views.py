from django.shortcuts import render, HttpResponse, redirect
from .models import pedidos, monedero, productos
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import pedidosForm
# Create your views here.
def historial(request):
    identificado=False
    puntosuser=0
    if request.user.is_authenticated:
        identificado=True
        current_user=request.user
        pedidosaux=pedidos.objects.filter(user=current_user).order_by('-id')
        productosaux=productos.objects.all()
        monederoaux=monedero.objects.get(useremail=current_user.email)
        puntosuser = monederoaux.balance
    return render(request, "historialapp/historial.html", {"identificado":identificado, "productosaux":productosaux, "pedidosaux":pedidosaux, "puntosuser":puntosuser})

def comprado(request, produc):
    identificado=False
    comprado=False
    puntosuser=0
    if request.user.is_authenticated:
        identificado=True
        productosaux=productos.objects.get(id=produc)
        current_user=request.user
        email=current_user.email
        mon=monedero.objects.get(useremail=email)
       
        
        puntosuser = mon.balance
        if productosaux.points < mon.balance:
            comprado=True
            mon.balance = mon.balance - productosaux.points
            mon.save()
            pedido = pedidos(user=current_user,prod=productosaux,points=productosaux.points)
            pedido.save()
            productosaux.sold=productosaux.sold + 1
            productosaux.save()

    return render(request, "historialapp/comprado.html",{"identificado":identificado, "comprado":comprado,"puntosuser":puntosuser})

def cancelar(request, pedi):
    identificado=False
    controlaux=False
    current_user=request.user
    pedidoaux=pedidos.objects.get(id=pedi)
    email=current_user.email
    mon=monedero.objects.get(useremail=email)
    
    if request.user.is_authenticated:
        identificado=True
        
        puntosuser = mon.balance
        
        if current_user == pedidoaux.user:
            
            controlaux=True
            mon.balance = mon.balance + pedidoaux.points
            mon.save()
            pedidoaux.estate="CL"
            pedidoaux.save()
            
    return render(request, "historialapp/cancelar.html",{"identificado":identificado, "controlaux":controlaux,"puntosuser":puntosuser})         

