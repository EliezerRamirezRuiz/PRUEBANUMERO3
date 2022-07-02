from django.urls import path
from rest_producto.views import lista_productos,detalle_producto

urlpatterns = [
    path('lista_productos', lista_productos, name="lista_productos"),
    path('detalle_producto/<id_producto>',detalle_producto, name="detalle_producto"),
]
