from django.db import models

# Create your models here.
#aquí se crea la clase productos
class categoria(models.Model):
    name=models.CharField(max_length=24)
    picture1=models.ImageField(upload_to='categoria')
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    def __str__(self):
        return self.name

class subcategoria(models.Model):
    name=models.CharField(max_length=24)
    category=models.ForeignKey(categoria, on_delete=models.CASCADE)
    class Meta:
        verbose_name='subcategoria'
        verbose_name_plural='subcategorias'
    def __str__(self):
        return self.name




class productos(models.Model):
    name=models.CharField(max_length=24)
    description=models.CharField(max_length=256)
    description2=models.CharField(max_length=4096)
    category=models.ForeignKey(categoria, on_delete=models.CASCADE)
    subcategory=models.ForeignKey(subcategoria, on_delete=models.CASCADE)
    picture1=models.ImageField(upload_to='productos')
    picture2=models.ImageField(upload_to='productos')
    picture3=models.ImageField(upload_to='productos')
    points=models.IntegerField()
    sold=models.IntegerField()
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.name



