from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import registroForm, usuarioForm, identForm
from .models import usuarios, monedero

# Create your views here.
def registro(request):
    form = registroForm()
    
    if request.method == "POST":
        form = registroForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            
            u = usuarios(name=post)
            u.save()
            p = monedero(useremail=post.email,balance=0)
            p.save()
            aux ='/ident/ampliacion/'+ str(u.id)
            
            return redirect(aux)

    return render(request, "usuarioapp/registro.html", {'form': form})

def ampliacion(request,var):
    aux = usuarios.objects.get(id=var)
    
    if request.method == "GET":
        form = usuarioForm(instance = aux)
    else:
        form = usuarioForm(request.POST, instance = aux)
        
        if form.is_valid():
            aux.save()
            return redirect('/')    
    

    return render(request, "usuarioapp/ampliacion.html", {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/') 

def ident(request):
    form = identForm()
    if request.method == "POST":
        form = identForm(request.POST)
        
        if form.is_valid():
            form_data = form.cleaned_data
            username = form_data.get("username")
            password = form_data.get("password")
            usuariosaux=User.objects.all()
            
               
            for usuario in usuariosaux:
                
                if usuario.username == username and usuario.password == password:
                    login(request, usuario)
                
                    return redirect('/')
            return redirect('/ident/')
    else:
        form = identForm()
    
    return render(request, "usuarioapp/ident.html", {'form': form})

def postr(request,var):

    p = monedero(useremail=var,balance=0)
    p.save()
    return render(request, "usuarioapp/postr.html",{"var":var})
