#!/usr/bin/env python3
from interfaces import IPrecioProvider
from productoID import ProductoID


class Producto(IPrecioProvider):
    def __init__(self, id : ProductoID):
        super().__init__()
        self.__ID = id
        self.__name : str
    
    def set_name(self,new_name : str):
        pass
    
    @property
    def id(self) -> ProductoID:
        return self.__ID
    
    @property
    def name(self) -> str:
        return self.__name
    
    def get_precio(self):
        pass
    
    def __eq__(self, value) -> bool:
        pass
    
    def __str__(self) -> str:
        pass