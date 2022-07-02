from django.urls import path
from rest_venta.views import lista_ventas, lista_detalle_ventas, lista_medio_pagos, venta_detalle, detalle_venta, detalle_medio_pago

urlpatterns = [
    path('lista_ventas', lista_ventas, name="lista_ventas"),
    path('lista_detalle_ventas', lista_detalle_ventas, name="lista_detalle_ventas"),
    path('lista_medio_pagos', lista_medio_pagos, name="lista_medio_pagos"),
    path('venta_detalle/<id_venta>', venta_detalle, name="venta_detalle"),
    path('detalle_venta/<id_detalle_venta>', detalle_venta, name="detalle_venta"),
    path('detalle_medio_pago/<id_medio_pago>', detalle_medio_pago, name="detalle_medio_pago"),
]
