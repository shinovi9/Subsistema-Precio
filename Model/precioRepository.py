#!/usr/bin/env python3
from interfaces import IPrecioProvider
from productoID import ProductoID
from producto import Producto
from precio import Precio
from pathlib import Path
import json

class PrecioRepository(IPrecioProvider):
    
    __lista_precios : list[Precio]
    __counter_obj = 0
    
    def __init__(self):
        if PrecioRepository.__counter_obj == 0:
            PrecioRepository.__lista_precios = PrecioRepository.__cargar_precios()
            PrecioRepository.__counter_obj += 1
    
    @staticmethod
    def new_precio(producto : ProductoID ,precio : float)-> Precio:
        pass
    
    @classmethod
    def incluir_precio(cls,precio : Precio):
        pass
    
    @classmethod
    def buscar_por_id(cls,producto_id : ProductoID)-> tuple[Precio]:
        pass
    @staticmethod
    def __cargar_Data() -> list:
        pass
    
    @staticmethod
    def __cargar_precios() -> list:
        pass
    
    @classmethod
    def guardar_cambios(cls):
        pass
    
    def get_precio():
        pass