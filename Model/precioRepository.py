#!/usr/bin/env python3
from interfaces import IPrecioProvider
from producto import Producto
from productoID import ProductoID
from precio import Precio


class PrecioRepository(IPrecioProvider):
    
    __lista_precios : list[Precio]
    
    def __init__(self):
        PrecioRepository.cargar_precios()
    
    @staticmethod
    def new_precio(producto : ProductoID ,precio : float)-> Precio:
        pass
    
    @classmethod
    def incluir_precio(cls,precio : Precio):
        pass
    
    @classmethod
    def buscar_por_id(cls,producto_id : ProductoID)-> tuple[Precio]:
        pass
    
    @classmethod
    def cargar_precios(cls):
        pass
    
    @classmethod
    def guardar_cambios(cls):
        pass
    
    def get_precio():
        pass