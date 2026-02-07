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
        return True if valor >= 0.0 else False
    
    @property
    def producto__id(self) -> ProductoID:
        return self.__producto__id
    
    @property
    def valor(self) -> float:
        return self.__valor
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Precio):
            return NotImplemented
        if other.valor == self.valor and \
            other.producto__id == self.producto__id:
                return True
        return False
    
    def a_dict(self) -> dict:
        return {"producto" : self.__producto__id.valor, "valor": self.valor}
    
    def __str__(self) -> str:
        return f"Precio {self.producto__id} {self.valor}"