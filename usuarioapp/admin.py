from django.contrib import admin
from .models import usuarios, monedero
# Register your models here.
class usuariosAdmin(admin.ModelAdmin):
    readonly_fields=()
  
class monederoAdmin(admin.ModelAdmin):
    readonly_fields=()

admin.site.register(usuarios, usuariosAdmin)
admin.site.register(monedero, monederoAdmin)