#!/usr/bin/env python3
from productoID import ProductoID

class Precio:
    
    def __init__(self, productoID: ProductoID, valor: float):
        """### Inicializa un objeto Precio con un ProductoID y un valor.

        Raises:
            ValueError: Se lanza si el valor es negativo.
        """
        if self.__validate(valor):  
            self.__valor = valor
        else:
            raise ValueError()
        self.__producto__id = productoID

    def __validate(valor: float) -> bool:
        """### Valida que el valor del precio sea mayor o igual a 0.
        Returns:
            bool: True si el valor es válido, False en caso contrario.
        """
        return True if valor >= 0.0 else False

    @property
    def producto__id(self) -> ProductoID:
        """### Obtiene el identificador del producto asociado al precio.
        Returns:
            ProductoID: El identificador del producto.
        """
        return self.__producto__id

    @property
    def valor(self) -> float:
        """### Obtiene el valor numérico del precio.
        Returns:
            float: El valor del precio.
        """
        return self.__valor

    def __eq__(self, other) -> bool:
        """### Compara dos objetos Precio para verificar si son iguales.
        Returns:
            bool: True si ambos precios tienen el mismo ProductoID y valor, False en caso contrario.
        """
        if not isinstance(other, Precio):
            return NotImplemented
        if other.valor == self.valor and other.producto__id == self.producto__id:
            return True
        return False

    def a_dict(self) -> dict:
        """### Convierte el objeto Precio en un diccionario.
        Returns:
            dict: Representación del precio con las claves 'producto' y 'valor'.
        """
        return {"producto": self.__producto__id.valor, "valor": self.valor}

    def __str__(self) -> str:
        """### Devuelve una representación en cadena del objeto Precio.
        Returns:
            str: Texto descriptivo con el ProductoID y el valor del precio.
        """
        return f"Precio {self.producto__id} {self.valor}"