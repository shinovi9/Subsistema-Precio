#!/usr/bin/env python3
from interfaces import IPrecioProvider
from productoID import ProductoID


class Producto(IPrecioProvider):
    def __init__(self, id : ProductoID):
        super().__init__()
        self.__ID = id
        self.__name : str  = ""
    
    def set_name(self,new_name : str):
        self.__name = new_name.capitalize()
    
    @property
    def id(self) -> ProductoID:
        return self.__ID
    
    @property
    def name(self) -> str:
        return self.__name
    
    def get_precio(self):
        pass
    
    def __eq__(self, other) -> bool:
        if other.name == self.name and\
            other.id == self.id:
                return True
        return False
    
    def __str__(self) -> str:
        return f"Precio {self.id} {self.name}"