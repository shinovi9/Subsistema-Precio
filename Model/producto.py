#!/usr/bin/env python3
from interfaces import IPrecioProvider
from productoID import ProductoID
from productoName import ProductoName


class Producto(IPrecioProvider):
    def __init__(self, id : ProductoID):
        super().__init__()
        self.__ID = id
        self.__name = ProductoName()
    
    def set_name(self,new_name = ProductoName):
        pass
    
    @property
    def id(self) -> ProductoID:
        return self.__ID
    
    @property
    def name(self) -> ProductoName:
        return self.__name
    
    def get_precio():
        pass
    
    def __eq__(self, value) -> bool:
        pass
    
    def __str__(self) -> str:
        pass