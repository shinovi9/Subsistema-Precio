#!/usr/bin/env python3
from interfaces import IPrecioProvider
from productoID import ProductoID
from producto import Producto
from precio import Precio
from pathlib import Path
import json

class PrecioRepository(IPrecioProvider):
    
    __lista_precios : list[Precio]
    __counter_obj = 0
    
    def __init__(self):
        if PrecioRepository.__counter_obj == 0:
            PrecioRepository.__lista_precios = PrecioRepository.__cargar_precios()
            PrecioRepository.__counter_obj += 1
    
    @staticmethod
    def new_precio(producto : ProductoID ,precio : float)-> Precio:
        pass
    
    @classmethod
    def incluir_precio(cls,precio : Precio):
        pass
    
    @classmethod
    def buscar_por_id(cls,producto_id : ProductoID)-> tuple[Precio]:
        pass
    
    @staticmethod
    def __cargar_Data() -> list:
        """## Carga la base de datos de productos desde PreciosDB.json

        Raises:
            ValueError: Si el JSON no contiene una lista de precios
            ValueError: Error al decodificar JSON

        Returns:
            list: Una lista de precios en forma de dict en caso de que no este vacía
        """
        # Ruta del archivo JSON (sube un nivel y entra a Data/)
        directorio_actual = Path(__file__).parent
        ruta = directorio_actual.parent / "Data" / "PreciosDB.json"
        
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
                raise ValueError("El JSON no contiene una lista de precios.")
            return data
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}")
    
    @staticmethod
    def __cargar_precios() -> list:
        pass
    
    @classmethod
    def guardar_cambios(cls):
        pass
    
    def get_precio():
        pass