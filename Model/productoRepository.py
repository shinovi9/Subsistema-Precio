#!/usr/bin/env python3
from interfaces import IPrecioProvider
from producto import Producto
from productoID import ProductoID
from precio import Precio

class ProductoRepository(IPrecioProvider):
    __lista_producto : list[dict[int,str]]
    
    @staticmethod
    def new_producto() -> Producto:
        pass
    
    @classmethod
    def de_list_Producto(cls,id : ProductoID) -> Producto :
        pass
    
    @classmethod
    def incluir_producto(cls,producto : Producto):
        pass
    
    @classmethod
    def ultimo_incluido(cls) -> ProductoID:
        pass
    
    @classmethod
    def cargar_productos(cls):
        pass
    
    @classmethod
    def guardar_cambios(cls):
        pass
    
    @classmethod
    def get_precio(cls,id : ProductoID)-> Precio:
        pass
    
    