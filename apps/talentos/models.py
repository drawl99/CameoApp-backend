from django.db import models
from apps.cameos.models import Cameo



class Category(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30, blank=False, null=False)

    objects = models.Manager()

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return str(self.nombre)





class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=100, blank=True, null=True)
    calificacion = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)
    cameo = models.OneToOneField(Cameo, on_delete= models.CASCADE)

    objects = models.Manager()

    class Meta:
        ordering = ["id"]
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'

    def __str__(self):
        return str(self.id) + ' - reseña en el cameo ' + str(self.cameo)
