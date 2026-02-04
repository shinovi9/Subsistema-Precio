"""Esta clase contiene los productos y los precios, también permite acceder a los precios de los productos a través de el id"""
class Precios:
    def __init__(self):
        self._precios = {}
        self._productos = {}
    
    def agregar_producto(self, producto, precio):
        self._productos[producto.id] = producto
        self._precios[producto.id] = precio
	
    def getPriceFrom(self, producto_id):
        return self._precios.get(producto_id)
    
    def listar_productos(self):
        return list(self._productos.values())
    
    def actualizar_precio(self, producto_id, nuevo_precio):
        if producto_id in self._precios:
            self._precios[producto_id] = nuevo_precio
            return True
        return False
