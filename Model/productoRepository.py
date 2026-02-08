#!/usr/bin/env python3
from precioRepository import PrecioRepository
from interfaces import IPrecioProvider
from productoID import ProductoID
from producto import Producto
from precio import Precio
from pathlib import Path
import json

class ProductoRepository(IPrecioProvider):
    
    # Ruta del archivo JSON (sube un nivel y entra a Data/)
    __directorio_actual = Path(__file__).parent
    __ruta = __directorio_actual.parent / "Data" / "Productos" / "ProductosDB.json"
    
    __lista_producto : list[Producto]
    __counter_obj = 0
    
    def __init__(self):
        """### Inicializa el repositorio de productos cargando los datos desde el archivo JSON.

        Si es la primera instancia creada, se cargan los productos en memoria
        y se incrementa el contador de inicialización.
        """
        if ProductoRepository.__counter_obj == 0:
            ProductoRepository.__lista_producto = ProductoRepository.__cargar_productos()
            ProductoRepository.__counter_obj += 1
        
    @classmethod
    def existe(cls, id : ProductoID) -> bool:
        """### Verifica si un producto con el ProductoID indicado existe en la lista interna.

        Returns:
            bool: True si el producto existe en la lista, False en caso contrario.
        """
        # Verificar si existe
        existe = any(p.id == id for p in cls.__lista_producto)
        return existe
    
    @classmethod
    def new_producto(cls, producto_id: ProductoID) -> Producto:
        """### Crea un nuevo objeto Producto validando la secuencia de IDs.

        Raises:
            ValueError: Se lanza si el ID proporcionado no es consecutivo al último ID existente.
        Returns:
            Producto: El nuevo objeto Producto creado con el ProductoID indicado.
        """
        # Si no hay productos, cualquier ID es válido
        if not cls.__lista_producto:
            return Producto(producto_id)
    
        max_id = max(
            cls.__lista_producto,
            key=lambda p: p.id.valor
        ).id.valor
    
        if producto_id.valor == (max_id + 1):
            return Producto(producto_id)
    
        raise ValueError(
            f"El ID de producto ({producto_id.valor}) debe ser mayor en 1, que el máximo existente ({max_id})."
        )
    
    @classmethod
    def de_list_Producto(cls,producto_id : ProductoID) -> Producto :
        """### Busca y devuelve un producto de la lista interna a partir de su ProductoID.

            Raises:
            ValueError: Se lanza si el producto con el ID indicado no existe en la lista.
            Returns:
            Producto: El objeto Producto correspondiente al ProductoID solicitado.
        """
        resultado = next((p for p in cls.__lista_producto if p.id == producto_id), None)
        if resultado: 
            return resultado
        raise ValueError("Producto inexistente") 
    
    @classmethod
    def incluir_producto(cls,producto : Producto):
        """### Incluye un nuevo producto en la lista de productos.

        Raises:
            ValueError: Se lanza si el producto ya existe en la lista.
        """
        if cls.existe(producto.id):
            raise ValueError(f"Producto ya esta presente en la lista\n{producto}")
        cls.__lista_producto.append(producto)
        cls.__guardar_cambios()
        
    @classmethod
    def ultimo_incluido(cls) -> ProductoID:
        """ ### Devuelve el último ProductoID incluido en la lista de productos.
    
        Raises:
            OverflowError: Se lanza cuando no existen productos en la lista.
        Returns:
            ProductoID: El identificador del último producto agregado.
        """
        if len(cls.__lista_producto) == 0:
            raise OverflowError("No hay productos actualmente")
        return cls.__lista_producto[-1] .id   
    
    @classmethod
    def __cargar_Data(cls) -> list:
        """## Carga la base de datos de productos desde ProductosDB.json

        Raises:
            ValueError: Si el JSON no contiene una lista de productos
            ValueError: Error al decodificar JSON
        Returns:
            list: Una lista de producto en forma de dict en caso de que no este vacía
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
                raise ValueError("El JSON no contiene una lista de productos.")
            return data
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}")
        
    @staticmethod
    def __cargar_productos() -> list:
        """### Carga los productos desde la fuente de datos JSON y los convierte en objetos Producto.
        Returns:
            list: Lista de objetos Producto construidos a partir de los datos cargados.
        """
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
        """### Guarda los cambios realizados en la lista interna de productos sobrescribiendo el archivo JSON correspondiente.
        """
        with cls.__ruta.open("w", encoding="utf-8") as f:
            json.dump(
                [producto.a_dict() for producto in cls.__lista_producto],
                f,
                ensure_ascii=False,
                indent=4
            )
    
    @classmethod
    def get_precio(cls,id : ProductoID) -> tuple:
        """### Obtiene los precios asociados a un producto mediante su ProductoID.

        Raises:
            ValueError: Se lanza si no existen precios para el ProductoID indicado.
        Returns:
            tuple: Una tupla con los objetos Precio correspondientes al ProductoID solicitado.
        """
        if cls.existe(id):
            return tuple(PrecioRepository.buscar_por_id(id))
        raise ValueError("Precios inexistente") 