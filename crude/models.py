from django.db import models
# Create your models here.

class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=20)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    
   
    

class producto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.TextField(max_length=20, null=False)
    stock=models.IntegerField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.CharField(max_length=100)
    