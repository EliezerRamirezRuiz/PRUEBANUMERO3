from django.contrib import admin
from .models import Cliente, Venta, DetalleVenta, MedioPago, Producto

admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(MedioPago)
admin.site.register(Producto)
