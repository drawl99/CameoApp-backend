from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.models import Client
from phonenumber_field.modelfields import PhoneNumberField


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
    categorias = models.ManyToManyField(Category)

    objects = models.Manager()

    class Meta:
        # ordering = ["id"]
        verbose_name = 'Talento'
        verbose_name_plural = 'Talentos'

    def __str__(self):
        return str(self.user.username)


class Ocasion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15, blank=False, null=False)

    objects = models.Manager()

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Ocasion'
        verbose_name_plural = 'Ocasiones'

    def __str__(self):
        return str(self.nombre)


class Cameo(models.Model):
    ESTADO_CAMEO = (
        (1, 'Pendiente'),
        (2, 'Aceptado'),
        (3, 'Rechazado'),
        (4, 'Realizado'),
    )

    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    url_video = models.URLField()
    instrucciones = models.CharField(max_length=500, blank=False, null=False)
    delivery_email = models.EmailField(blank=False, null=False)
    delivery_phone = PhoneNumberField(null=False, blank=False, unique=False)
    privacy_state = models.BooleanField("Privado", default=True)
    from_person = models.CharField(max_length=30, null=False, blank=False)
    to_person = models.CharField(max_length=30, null=False, blank=False)
    ocasion = models.ForeignKey(Ocasion, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADO_CAMEO, default=1)

    objects = models.Manager()

    class Meta:
        ordering = ["id"]
        verbose_name = 'Cameo'
        verbose_name_plural = 'Cameos'

    def __str__(self):
        return str(self.id) + ' - realizado por ' + str(self.talent) + ' para ' + str(self.client) \
               + ' (de ' + str(self.from_person) + ', para ' + str(self.to_person) + ' )'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=250, blank=True, null=True)
    cameo = models.ForeignKey(Cameo, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)

    objects = models.Manager()

    class Meta:
        ordering = ["id"]
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return str(self.id) + ' - comentario por ' + str(self.client) + ' en el cameo ' + str(self.cameo)


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=100, blank=True, null=True)
    calificacion = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)
    cameo = models.ForeignKey(Cameo, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        ordering = ["id"]
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'

    def __str__(self):
        return str(self.id) + ' - reseña en el cameo ' + str(self.cameo)
