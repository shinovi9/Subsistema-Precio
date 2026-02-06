#!/usr/bin/env python3

class ProductoID:
    
    def __init__(self, id : int):
        if self.__validate(id):  
            self.__valor = id
        else:
            raise ValueError()
    
    @property
    def valor(self) -> int:
        return self.__valor
    
    def __validate(valor : int) -> bool:
        return True if valor > 0 else False
    
    def __eq__(self, other) -> bool:
        if type(other) != ProductoID:
            return False
        return True if other.valor == self.valor else False
    
    def __str__(self) -> str:
        return str(self.valor)