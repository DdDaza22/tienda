from django.contrib import admin
from .models import pedidos
# Register your models here.
class pedidosAdmin(admin.ModelAdmin):
    readonly_fields=()
  

admin.site.register(pedidos, pedidosAdmin)