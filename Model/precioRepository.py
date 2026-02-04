#!/usr/bin/env python3
from interfaces import IPrecioProvider
from producto import Producto
from productoID import ProductoID
from precio import Precio


class PrecioRepository(IPrecioProvider):
    
    @staticmethod
    def new_precio(producto ,precio)-> dict[int,float]:
        pass
    
    @classmethod
    def incluir_precio(cls,producto : ProductoID, precio : Precio):
        pass
    
    @classmethod
    def de_list_precio(cls,producto_id : ProductoID)-> tuple[float]:
        pass
    
    @classmethod
    def cargar_precios(cls):
        pass
    
    @classmethod
    def guardar_cambios(cls):
        pass
    
    def get_precio():
        pass