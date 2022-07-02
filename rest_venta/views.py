from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Venta, DetalleVenta, MedioPago
from .serializers import DetalleVentaSerializer, MedioPagoSerializer, VentaSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#END POINT VENTA
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_ventas(request):
    """
    MUESTRA TODOS LAS VENTAS
    """
    if request.method == 'GET':
        venta = Venta.objects.all()
        serializer = VentaSerializer(venta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#EndPoint de Detalle de las ventas
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_detalle_ventas(request):
    """ 
    Lista todos los detalle de las ventas realizadas
    """
    if request.method == 'GET':
        detalle_venta = DetalleVenta.objects.all()
        serializer = DetalleVentaSerializer(detalle_venta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DetalleVentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#ENDPOINT LISTADO DE MEDIO DE PAGO
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_medio_pagos(request):
    """ 
    Lista todos los medios de pagos existetes
    """
    if request.method == 'GET':
        mediopago = MedioPago.objects.all()
        serializer = MedioPagoSerializer(mediopago, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MedioPagoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#ENDPOINT VENTAS POR ID
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def venta_detalle(request,id_venta):
    """ 
    Get, update o delete de una venta en especifico.
    Recibe el parametro <id_venta>
    """
    try:
        venta_detalle = Venta.objects.get(id_venta=id_venta)
    except Venta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VentaSerializer(venta_detalle)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(venta_detalle, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        venta_detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#ENDPOINT DETALLE DE VENTA POR ID 
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_venta(request,id_detalle_venta):
    """ 
    OBTENER DETALLE DE VENTA POR ID 
    """
    try:
        detalle_venta = DetalleVenta.objects.get(id_detalle_venta=id_detalle_venta)
    except DetalleVenta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DetalleVentaSerializer(detalle_venta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DetalleVentaSerializer(detalle_venta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        detalle_venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_medio_pago(request,id_medio_pago):
    """ 
    OBTENER O MODIFICAR DETALLE DE MEDIO DE PAGO
    """
    try:
        medio_pago = MedioPago.objects.get(id_medio_pago=id_medio_pago)
    except medio_pago.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MedioPagoSerializer(medio_pago)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MedioPagoSerializer(medio_pago, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        medio_pago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)