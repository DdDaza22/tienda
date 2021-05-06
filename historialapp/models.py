from django.db import models
from django.contrib.auth.models import User
from usuarioapp.models import usuarios, monedero
from auxapp.models import productos
# Create your models here.

class pedidos(models.Model):
    #id = models.AutoField(primary_key=True)
    #name=models.CharField(max_length=23)
    ESTADOS_CHOICES = (
        ('IN', 'iniciado'),
        ('EP', 'enProceso'),
        ('EN', 'enviado'),
        ('CM', 'completado'),
        ('CL', 'cancelado'),
    )
    prod=models.ForeignKey(productos, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    points= models.IntegerField()
    estate = models.CharField(max_length=24, choices=ESTADOS_CHOICES, default="IN")

    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'

    def __str__(self):
        return self.user.username