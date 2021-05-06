
from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import login_required, logout_then_login
from django.conf.urls.static import static
from django.conf import settings
from usuarioapp import views
urlpatterns = [

    path('',views.ident, name="ident"),
 
    
    path('ampliacion/<var>',views.ampliacion, name="ampliacion"),
    path('postr/<var>/',views.postr, name="postr"),
    path('registro/',views.registro, name="registro"),
   path('logout/',views.logout_view, name="logout"),
    

   

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)