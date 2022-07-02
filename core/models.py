from pickle import TRUE
from tkinter import CASCADE
from django.db import models

# Create your models here.
# modelo para cliente
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name='Id de cliente')
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre del cliente')
    apellidos = models.CharField(max_length=150, null=False, verbose_name='Apellido del cliente')
    correo = models.CharField(max_length=200, null=False, verbose_name='Correo del cliente')
    direccion = models.CharField(max_length=200, verbose_name='Dirección del cliente')
    
    def __str__(self):
        return self.nombre

# Modelo para MedioPago
class MedioPago(models.Model):
    id_medio_pago = models.AutoField(primary_key=True,verbose_name='Identificador del medio de pago')
    nombre = models.CharField(max_length=25, null=False, verbose_name='Nombre del medio de pago')

    def __str__(self):
        return self.nombre

# Modelo para Producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name='Identificador del producto')
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=250, verbose_name='Descripcion del producto')
    precio = models.IntegerField(null=False, verbose_name='Precio del producto')

    def __str__(self):
        return self.nombre

#Modelo para venta
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True, verbose_name='Identificador de la venta')
    monto = models.IntegerField(null=False, verbose_name='Monto Total')
    medioPago = models.ForeignKey(MedioPago, on_delete=models.CASCADE, verbose_name='Medio de pago')
    fecha = models.CharField(null=False, max_length=10, verbose_name='Fecha de la venta')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Identificador del cliente')

    def __str__(self):
        return str(self.id_venta)
        
# Modelo Detalle Venta
class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True, verbose_name='Identificador del detalle de venta')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Identificador del producto')
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name='Identificador de la venta')

    def __str__(self):
        return str(self.id_detalle_venta)+' '+str(self.producto)+' '+str(self.venta)


