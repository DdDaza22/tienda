from django.contrib import admin


from auxapp.models import subcategoria, categoria, productos 

# Register your models here.
#para que en admin se vea la fecha de modificación y poder ordenar por esa fecha
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('updated',)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=()
class SubcategoriaAdmin(admin.ModelAdmin):
    readonly_fields=()
admin.site.register(subcategoria, SubcategoriaAdmin)
admin.site.register(categoria, CategoriaAdmin)
admin.site.register(productos, ServicioAdmin)