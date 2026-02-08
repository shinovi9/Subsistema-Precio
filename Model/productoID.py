#!/usr/bin/env python3

class ProductoID:
    
    def __init__(self, id: int):
        """### Inicializa un objeto ProductoID con un valor entero.

        Args:
            id (int): Identificador numérico del producto.
        Raises:
            ValueError: Se lanza si el identificador es menor o igual a 0.
        """
        if self.__validate(id):  
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

    def __validate(valor: int) -> bool:
        """### Valida que el identificador sea mayor que 0.

        Args:
            valor (int): Valor entero a validar.
        Returns:
            bool: True si el valor es válido, False en caso contrario.
        """
        return True if valor > 0 else False

    def __eq__(self, other) -> bool:
        """### Compara dos objetos ProductoID para verificar si son iguales.

        Args:
            other (ProductoID): Otro identificador a comparar.
        Returns:
            bool: True si ambos identificadores tienen el mismo valor, False en caso contrario.
        """
        if not isinstance(other, ProductoID):
            return NotImplemented
        return True if other.valor == self.valor else False

    def __str__(self) -> str:
        """### Devuelve una representación en cadena del identificador.

        Returns:
            str: Texto con el valor del identificador.
        """
        return str(self.valor)