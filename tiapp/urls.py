from django.urls import path
from tiapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.home, name="home"),
 
    
    path('tiendae/',views.tiendae, name="tiendae"),
   
    path('inicio/',views.inicio, name="inicio"),

    
    path('retorno/',views.retorno, name="retorno"),
   

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)