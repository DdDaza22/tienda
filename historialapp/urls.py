from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from historialapp import views
urlpatterns = [

    path('',views.historial, name="historial"),
    path('comprado/<produc>/',views.comprado, name="comprado"),
    path('cancelar/<pedi>/',views.cancelar, name="cancelar"),
 

   

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)