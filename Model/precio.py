#!/usr/bin/env python3
from productoID import ProductoID

class Precio:
    
    def __init__(self, productoID : ProductoID ,valor : float):
        if self.__validate(valor):  
            self.__valor = valor
        else:
            raise ValueError()
        self.__producto__id = productoID
        
    def __validate(valor : float) -> bool:
        pass
    @property
    def producto__id() -> ProductoID:
        pass
    
    @property
    def valor() -> float:
        pass
    
    def __eq__(self, value) -> bool:
        pass
    
    def __str__(self) -> str:
        pass