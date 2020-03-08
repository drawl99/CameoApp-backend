from django.db import models
from django.contrib.auth.models import User





class UserClient(models.Model):
    userClient = models.OneToOneField(User, on_delete=models.CASCADE)
    
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    
    
    
    biografia = models.CharField(max_length=500, blank= True, null= True)
    avatar = models.CharField(max_length=200, blank= True, null= True)
    user_twitter = models.CharField(max_length=30, blank= True, null= True)
    favoritos = models.ManyToManyField('talentos.Talent', blank = True)
    

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        #ordering=['id']


    def __str__(self):
        return str(self.userClient)
