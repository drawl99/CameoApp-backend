from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



class Talent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    biografia = models.CharField('Biografía', blank=True, null=True, default='', max_length=250)
    seguidores = models.IntegerField('Seguidores', blank=False, null=False)
    telefono = models.CharField('Teléfono', max_length=30, blank=False, null=False)
    precio = models.IntegerField('Precio')
    ocupacion = models.CharField('Ocupación', max_length=30, blank=True, null=True)
    tiempo_respuesta = models.IntegerField(null=False, blank=False)
    ausente = models.BooleanField("Ausente", default=False)
    categorias = models.ManyToManyField('talentos.Category')

    objects = models.Manager()

    class Meta:
        # ordering = ["id"]
        verbose_name = 'Talento'
        verbose_name_plural = 'Talentos'

    def __str__(self):
        return str(self.user.username)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    biografia = models.CharField(max_length=500, blank=True, null=True)
    avatar = models.CharField(max_length=200, blank=True, null=True)
    user_twitter = models.CharField(max_length=30, blank=True, null=True)
    favoritos = models.ManyToManyField(Talent, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        # ordering=['id']

    def __str__(self):
        return str(self.user.username)

