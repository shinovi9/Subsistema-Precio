#!/usr/bin/env python3
from Model.ValueObject.productoID import ProductoID


class Producto:

    def __init__(self, id: ProductoID):
        """### Inicializa un objeto Producto con su identificador único.

        Args:
            id (ProductoID): Identificador del producto.
        """
        self.__ID = id
        self.__name: str = ""

    def set_name(self, new_name: str):
        """### Asigna un nombre al producto, aplicando formato:
        - Elimina espacios al inicio y final.
        - Capitaliza la primera letra.
        - Reemplaza espacios internos por guiones bajos.

        Args:
            new_name (str): Nombre a asignar.
        """
        new_name = new_name.strip().capitalize().replace(" ", "_")
        self.__name = new_name

    @property
    def id(self) -> ProductoID:
        """### Obtiene el identificador único del producto.

        Returns:
            ProductoID: El identificador del producto.
        """
        return self.__ID

    @property
    def name(self) -> str:
        """### Obtiene el nombre del producto.

        Returns:
            str: El nombre del producto.
        """
        return self.__name

    def a_dict(self) -> dict:
        """### Convierte el objeto Producto en un diccionario.

        Returns:
            dict: Representación del producto con las claves 'ID' y 'nombre'.
        """
        return {"ID": self.__ID.valor, "nombre": self.name}

    def __eq__(self, other) -> bool:
        """### Compara dos objetos Producto para verificar si son iguales.

        Returns:
            bool: True si ambos productos tienen el mismo ID y nombre, False en caso contrario.
        """
        if not isinstance(other, Producto):
            return NotImplemented
        return other.name == self.name and other.id == self.id

    def __str__(self) -> str:
        """## Devuelve una representación en cadena del objeto Producto.

        Returns:
            str: Texto descriptivo con el ID y el nombre del producto.
        """
        return f"Precio {self.id} {self.name}"
    