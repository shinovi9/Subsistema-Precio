#!/usr/bin/env python3

class ProductoID:
    
    def __init__(self, id: int):
        """### Inicializa un objeto ProductoID con un valor entero.

        Args:
            id (int): Identificador numérico del producto.
        Raises:
            ValueError: Se lanza si el identificador es menor o igual a 0.
        """
        if id > 0 :  
            self.__valor = id
        else:
            raise ValueError()

    @property
    def valor(self) -> int:
        """### Obtiene el valor entero del identificador del producto.

        Returns:
            int: El valor del identificador.
        """
        return self.__valor

    def __eq__(self, other) -> bool:
        """### Compara dos objetos ProductoID para verificar si son iguales.

        Args:
            other (ProductoID): Otro identificador a comparar.
        Returns:
            bool: True si ambos identificadores tienen el mismo valor, False en caso contrario.
        """
        if not isinstance(other, ProductoID):
            return NotImplemented
        return other.valor == self.valor

    def __str__(self) -> str:
        """### Devuelve una representación en cadena del identificador.

        Returns:
            str: Texto con el valor del identificador.
        """
        return str(self.valor)