#!/usr/bin/env python3
from productoRepository import ProductoRepository
from interfaces import IPrecioProvider
from productoID import ProductoID
from precio import Precio
from pathlib import Path
import json

class PrecioRepository(IPrecioProvider):
    
    # Ruta del archivo JSON (sube un nivel y entra a Data/)
    __directorio_actual = Path(__file__).parent
    __ruta = __directorio_actual.parent / "Data" / "Precios" / "PreciosDB.json"
    
    __lista_precios : list[Precio]
    __counter_obj = 0
    
    def __init__(self):
        """### Inicializa el repositorio de precios cargando los datos desde el archivo JSON.

        Si es la primera instancia creada, se cargan los precios en memoria
        y se incrementa el contador de inicialización.
        """
        if PrecioRepository.__counter_obj == 0:
            PrecioRepository.__lista_precios = PrecioRepository.__cargar_precios()
            PrecioRepository.__counter_obj += 1
    
    @staticmethod
    def new_precio(producto : ProductoID ,valor : float)-> Precio:
        """### Crea un nuevo objeto Precio asociado a un ProductoID existente.

        Raises:
            ValueError: Se lanza si el ProductoID indicado no existe en el repositorio de productos.
        Returns:
            Precio: El nuevo objeto Precio creado con el ProductoID y valor proporcionados.
        """
        if ProductoRepository.existe(producto):
            return Precio(producto, valor)
        raise ValueError("Producto inexistente")
    
    @classmethod
    def incluir_precio(cls,precio : Precio):
        """### Incluye un nuevo precio en la lista interna de precios y guarda los cambios en el archivo JSON.
        """
        cls.__lista_precios.append(precio)
        cls.__guardar_cambios()
    
    @classmethod
    def buscar_por_id(cls, id : ProductoID)-> list[Precio]:
        """### Busca y devuelve todos los precios asociados a un producto mediante su ProductoID.

        Raises:
            OverflowError: Se lanza si no existen precios registrados para el ProductoID indicado.
        Returns:
            list[Precio]: Lista de objetos Precio correspondientes al ProductoID solicitado.
        """
        coincidencias = [p for p in cls.__lista_precios if p.producto__id == id]
        if coincidencias:
            return coincidencias
        raise OverflowError(f"No hay precios actualmente de este producto {id}")
    
    @classmethod
    def __cargar_Data(cls) -> list:
        """## Carga la base de datos de productos desde PreciosDB.json

        Raises:
            ValueError: Si el JSON no contiene una lista de precios
            ValueError: Error al decodificar JSON
        Returns:
            list: Una lista de precios en forma de dict en caso de que no este vacía
        """
        if not cls.__ruta.exists():
            cls.__ruta.parent.mkdir(parents=True, exist_ok=True)  # Crear carpeta si no existe
            cls.__ruta.write_text("[]", encoding="utf-8")
            return []
        
        # Si existe pero está vacío, escribir lista vacía
        if cls.__ruta.stat().st_size == 0:
            cls.__ruta.write_text("[]", encoding="utf-8")
            return []
        
        try:
            # Cargar contenido
            data = json.loads(cls.__ruta.read_text(encoding="utf-8"))
            # Validar que sea lista
            if not isinstance(data, list):
                raise ValueError("El JSON no contiene una lista de precios.")
            return data
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}")
    
    @staticmethod
    def __cargar_precios() -> list:
        """### Carga los precios desde la fuente de datos JSON y los convierte en objetos Precios.
    
        Returns:
            list: Lista de objetos Precios construidos a partir de los datos cargados.
        """
        lista_dict_Precios = PrecioRepository.__cargar_Data()
        lista_precios: list = []
        
        for precio_dict in lista_dict_Precios:
            id_obj = ProductoID(precio_dict["producto"])
            valor = precio_dict["valor"]
            precio = Precio(id_obj, valor)
            lista_precios.append(precio)
        return lista_precios
    
    @classmethod
    def __guardar_cambios(cls):
        """
        Guarda los cambios realizados en la lista interna de precios
        sobrescribiendo el archivo JSON correspondiente.
        """
        with cls.__ruta.open("w", encoding="utf-8") as f:
            json.dump(
                [precio.a_dict() for precio in cls.__lista_precios],
                f,
                ensure_ascii=False,
                indent=4
            )

    @classmethod
    def get_precio(cls, id_producto : ProductoID) -> tuple:
        """### Obtiene todos los precios asociados a un producto mediante su ProductoID.

        Raises:
            ValueError: Se lanza si el producto indicado no existe en el repositorio.
        Returns:
            tuple: Una tupla con los objetos Precio correspondientes al ProductoID solicitado.
        """
        if ProductoRepository.existe(id_producto):
            return tuple(cls.buscar_por_id(id_producto))
        raise ValueError("Precios inexistente") 
    
    @classmethod
    def eliminar_precio(cls, producto_id: ProductoID, valor: float):
        """#### Elimina un precio específico de la lista interna de precios, identificado por su ProductoID y valor.
        Raises:
            ValueError: Se lanza si no se encuentra un precio con el ProductoID y valor indicados.
        """
        # Buscar el precio exacto
        precio_obj = next(
            (p for p in cls.__lista_precios if p.producto__id == producto_id and p.valor == valor),
            None
        )
        if precio_obj:
            cls.__lista_precios.remove(precio_obj)
            cls.__guardar_cambios()
            return
        raise ValueError(f"No existe un precio con ProductoID={producto_id} y valor={valor}")
