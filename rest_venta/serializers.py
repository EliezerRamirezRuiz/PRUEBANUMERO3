from rest_framework import serializers
from core.models import Venta, DetalleVenta, MedioPago

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields =['id_venta','monto','medioPago','fecha','cliente']

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['id_detalle_venta','producto','venta']

class MedioPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioPago
        fields = ['id_medio_pago','nombre']