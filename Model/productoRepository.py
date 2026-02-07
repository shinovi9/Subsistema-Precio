#!/usr/bin/env python3
from interfaces import IPrecioProvider
from productoID import ProductoID
from producto import Producto
from precio import Precio
from pathlib import Path
import json

class ProductoRepository(IPrecioProvider):
    __lista_producto : list[Producto]
    __counter_obj = 0
    
    def __init__(self):
        if ProductoRepository.__counter_obj == 0:
            ProductoRepository.__lista_producto = ProductoRepository.__cargar_productos()
            ProductoRepository.__counter_obj += 1
    
        
    @classmethod
    def existe(cls, id : ProductoID) -> bool:
        # Verificar si existe
        existe = any(p.id == id for p in ProductoRepository.__lista_producto)
        return existe
    
    @classmethod
    def new_producto(cls, producto_id: ProductoID) -> Producto:
        # Si no hay productos, cualquier ID es válido
        if not ProductoRepository._ProductoRepository__lista_producto:
            return Producto(producto_id)
    
        max_id = max(
            ProductoRepository._ProductoRepository__lista_producto,
            key=lambda p: p.id.valor
        ).id.valor
    
        if producto_id.valor == (max_id + 1):
            return Producto(producto_id)
    
        raise ValueError(
            f"El ID de producto ({producto_id.valor}) debe ser mayor en 1, que el máximo existente ({max_id})."
        )
    
    @classmethod
    def de_list_Producto(cls,producto_id : ProductoID) -> Producto :
        pass
    
    @classmethod
    def incluir_producto(cls,producto : Producto):
        pass
    
    @classmethod
    def ultimo_incluido(cls) -> ProductoID:
        pass
    
    @staticmethod
    def __cargar_Data() -> list:
        """## Carga la base de datos de productos desde ProductosDB.json

        Raises:
            ValueError: Si el JSON no contiene una lista de productos
            ValueError: Error al decodificar JSON

        Returns:
            list: Una lista de producto en forma de dict en caso de que no este vacía
        """
        # Ruta del archivo JSON (sube un nivel y entra a Data/)
        directorio_actual = Path(__file__).parent
        ruta = directorio_actual.parent / "Data" / "ProductosDB.json"
        
        if not ruta.exists():
            ruta.parent.mkdir(parents=True, exist_ok=True)  # Crear carpeta si no existe
            ruta.write_text("[]", encoding="utf-8")
            return []
        
        # Si existe pero está vacío, escribir lista vacía
        if ruta.stat().st_size == 0:
            ruta.write_text("[]", encoding="utf-8")
            return []
        
        try:
            # Cargar contenido
            data = json.loads(ruta.read_text(encoding="utf-8"))
            # Validar que sea lista
            if not isinstance(data, list):
                raise ValueError("El JSON no contiene una lista de productos.")
            return data
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}")
        
        
    @staticmethod
    def __cargar_productos() -> list:
        lista_dict_Productos = ProductoRepository.__cargar_Data()
        lista_productos: list = []
        for product_dict in lista_dict_Productos:
            id_obj = ProductoID(product_dict["ID"])
            name = product_dict["nombre"]
            producto = Producto(id_obj)
            producto.set_name(name)
            lista_productos.append(producto)
        return lista_productos
    
    @classmethod
    def guardar_cambios(cls):
        pass
    
    @classmethod
    def get_precio(cls,id : ProductoID)-> Precio:
        pass