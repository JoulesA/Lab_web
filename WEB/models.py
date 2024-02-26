from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    foto = models.FileField(upload_to='Img_Perfil/')
    bio = models.TextField()

    
# Catalogos
class Voluntario(models.Model):
    GENDER_CHOICES = [
        ('H','Hombre'),
        ('M','Mujer'),
        ('I','Prefiere no especificar')
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Genero')
    observaciones = models.TextField(max_length=100, blank=True, verbose_name='Observaciones')

    def delete(self, using=None, kepp_parents=False):
        super().delete()

    def __str__(self):
        texto = self.apellido + ' ' + self.nombre 
        return(texto)

class SignalType(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Tipo de señal')

    def delete(self, using=None, kepp_parents=False):
        super().delete()

    def __str__(self):
        texto = str(self.nombre)
        return(texto)

# Entidades
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    nombre = models.CharField(max_length=50,verbose_name='Nombre del Proyecto')
    descripcion = models.TextField(max_length=400, verbose_name='Descripcion del Proyecto')
    
    
    # Datos de envio a sp
    sampleRate = models.FloatField(verbose_name='Frecuencia de muestreo (Hz)')
    ganancia = models.IntegerField(verbose_name='Ganancia')
    time = models.FloatField(verbose_name='Tiempo (seg)')
    signalType = models.ForeignKey(SignalType, on_delete=models.CASCADE, verbose_name='Tipo de señal')
    
    complete = models.BooleanField(verbose_name='Proyecto Finalizado')
    # Archivos para web
    rarFile = models.FileField(upload_to='RAR_Files/', blank=True, verbose_name='Archivo RAR')
    article = models.FileField(upload_to='Articles/',blank=True,verbose_name='Articulo PDF')
    
    def delete(self, using=None, kepp_parents=False):
        super().delete()
    
    def __str__(self):
        texto = str(self.nombre)
        return(texto)

class Prueba(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la prueba')
    descripcion = models.TextField(max_length=400, verbose_name='Descripcion')
    complete = models.BooleanField()
    rarFile = models.FileField(upload_to='RAR_Files/', blank = True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, verbose_name='Proyecto')
    voluntarios = models.ManyToManyField(Voluntario, through='Muestra')

    def delete(self, using=None, kepp_parents=False):
        super().delete()

    def __str__(self):
        texto = str(self.nombre)
        return(texto)

class Muestra(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    archivo = models.FileField(upload_to='Signal_Files/')
    
    def delete(self, using=None, kepp_parents=False):
        super().delete()

class Buffer(models.Model):
    id = models.AutoField(primary_key=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    ocupado = models.BooleanField()

    # Datos de identificacion de muestra en el bufer
    proyecto = models.IntegerField(blank=True)
    prueba = models.IntegerField(blank=True)
    voluntario = models.IntegerField(blank=True)
    fecha = models.DateField(blank=True)
    archivo = models.FileField(upload_to='Buffer_Files/')

    # Canales de recepción 24
    ch0 = models.FloatField(blank=True)
    ch1 = models.FloatField(blank=True)
    ch2 = models.FloatField(blank=True)
    ch3 = models.FloatField(blank=True)
    ch4 = models.FloatField(blank=True)
    ch5 = models.FloatField(blank=True)
    ch6 = models.FloatField(blank=True)
    ch7 = models.FloatField(blank=True)
    ch8 = models.FloatField(blank=True)
    ch9 = models.FloatField(blank=True)
    ch10 = models.FloatField(blank=True)
    ch11 = models.FloatField(blank=True)
    ch12 = models.FloatField(blank=True)
    ch13 = models.FloatField(blank=True)
    ch14 = models.FloatField(blank=True)
    ch15 = models.FloatField(blank=True)
    ch16 = models.FloatField(blank=True)
    ch17 = models.FloatField(blank=True)
    ch18 = models.FloatField(blank=True)
    ch19 = models.FloatField(blank=True)
    ch20 = models.FloatField(blank=True)
    ch21 = models.FloatField(blank=True)
    ch22 = models.FloatField(blank=True)
    ch23 = models.FloatField(blank=True)

    
    def delete(self, using=None, kepp_parents=False):
        super().delete()