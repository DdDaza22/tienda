from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:orden>/<int:pag>/',views.tiendasimple, name="tiendasimple"),
    path('<int:orden>/<int:mini>/<int:maxi>/<int:pag>/',views.tienda, name="tienda"),
    path('compra/<int:produc>/',views.compra, name="compra"),
    path('categoria/',views.tiendacategoria, name="categoria"),
    path('subcategoria/<categoria>/',views.tiendasubcategoria, name="subcategoria"),
    path('categoria/<categoria>/<int:pag>/',views.productocategoriasimple, name="productocategoriasimple"),
    path('categoria/<categoria>/<int:orden>/<int:mini>/<int:maxi>/<int:pag>/',views.productocategoria, name="productocategoria"),
    path('subcategoria/<categoria>/<int:pag>/',views.productosubcategoriasimple, name="productosubcategoriasimple"),
    path('subcategoria/<categoria>/<int:orden>/<int:mini>/<int:maxi>/<int:pag>/',views.productosubcategoria, name="productosubcategoria"),
    path('busqueda/<nombre>/<int:pag>/',views.tiendabusquedasimple, name="tiendabusquedasimple"),

]

