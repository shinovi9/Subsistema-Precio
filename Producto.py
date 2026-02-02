# Clase Producto, tiene los atributos nombre e id
class Producto:
    def __init__(self, id_producto, nombre):
        self._id = id_producto
        self._nombre = nombre
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
