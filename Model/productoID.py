#!/usr/bin/env python3

class ProductoID:
    
    def __init__(self, id : int):
        
        if self.__validate(id):  
            self.__valor = id
        else:
            raise ValueError()
    
    @property
    def valor(self) -> int:
        pass
    
    def __validate(valor : int) -> bool:
        pass
    
    def __eq__(self, value) -> bool:
        pass
    
    def __str__(self) -> str:
        pass