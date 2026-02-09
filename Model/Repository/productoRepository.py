#!/usr/bin/env python3
from Model.Repository.precioRepository import PrecioRepository
from Model.ValueObject.productoID import ProductoID
from Model.EntityObject.producto import Producto
from interfaces import IPrecioProvider
from pathlib import Path
import json

class ProductoRepository(IPrecioProvider):
    """### ejemplo de uso 
    ```
    ______________________________________________________________________
        repo = ProductoRepository()          # carga datos la primera vez
        nuevo = repo.new_producto(ProductoID(1))
        nuevo.set_name("ejemplo")
        repo.incluir_producto(nuevo)         # persiste en JSON
        p = repo.get_precio(nuevo.id)        # obtiene precios (tupla)
    ______________________________________________________________________
    ```
    """
    # Ruta del archivo JSON (sube un nivel y entra a Data/)
    __directorio_actual = Path(__file__).parent.parent
    __ruta = __directorio_actual.parent / "Data" / "Productos" / "ProductosDB.json"

    __lista_producto: list[Producto]
    __counter_obj = 0

    def __init__(self, precio_repo: PrecioRepository = None):
        """### Inicializa el repositorio de productos.
        Si es la primera instancia creada, carga los productos en memoria.
        Recibe opcionalmente una instancia de PrecioRepository para consultas de precios.
        """
        # inicialización compartida de la lista (comportamiento original)
        if ProductoRepository.__counter_obj == 0:
            ProductoRepository.__lista_producto = ProductoRepository.__cargar_productos()
            ProductoRepository.__counter_obj += 1

        # repositorio de precios asociado (instancia)
        self._precio_repo = precio_repo or PrecioRepository()

    def existe(self, id: ProductoID) -> bool:
        """### Verifica si un producto con el ProductoID indicado existe en la lista interna.

        Returns:
            bool: True si el producto existe en la lista, False en caso contrario.
        """
        return any(p.id == id for p in self.__class__.__lista_producto)

    def new_producto(self, producto_id: ProductoID) -> Producto:
        """### Crea un nuevo objeto Producto validando la secuencia de IDs.

        Raises:
            ValueError: Si el ID no es consecutivo al último ID existente.

        Returns:
            Producto: Nuevo objeto Producto.
        """
        lista = self.__class__.__lista_producto
        if not lista:
            return Producto(producto_id)

        max_id = max(lista, key=lambda p: p.id.valor).id.valor
        if producto_id.valor == (max_id + 1):
            return Producto(producto_id)

        raise ValueError(
            f"El ID de producto ({producto_id.valor}) debe ser mayor en 1, que el máximo existente ({max_id})."
        )

    def de_list_Producto(self, producto_id: ProductoID) -> Producto:
        """### Busca y devuelve un producto de la lista interna a partir de su ProductoID.

        Raises:
            ValueError: Si el producto no existe.
        """
        resultado = next((p for p in self.__class__.__lista_producto if p.id == producto_id), None)
        if resultado:
            return resultado
        raise ValueError("Producto inexistente")

    def incluir_producto(self, producto: Producto):
        """### Incluye un nuevo producto en la lista de productos y persiste los cambios.

        Raises:
            ValueError: Si el producto ya existe.
        """
        if self.existe(producto.id):
            raise ValueError(f"Producto ya esta presente en la lista\n{producto}")
        self.__class__.__lista_producto.append(producto)
        self.guardar_cambios()

    def ultimo_incluido(self) -> ProductoID:
        """### Devuelve el último ProductoID incluido en la lista.

        Raises:
            OverflowError: Si no hay productos.
        """
        lista = self.__class__.__lista_producto
        if len(lista) == 0:
            raise OverflowError("No hay productos actualmente")
        return lista[-1].id

    @staticmethod
    def __cargar_Data() -> list:
        """### Carga la base de datos de productos desde ProductosDB.json.
        Crea el archivo/carpeta si no existen y devuelve la lista de dicts.
        """
        ruta = ProductoRepository.__ruta
        if not ruta.exists():
            ruta.parent.mkdir(parents=True, exist_ok=True)
            ruta.write_text("[]", encoding="utf-8")
            return []

        if ruta.stat().st_size == 0:
            ruta.write_text("[]", encoding="utf-8")
            return []

        try:
            data = json.loads(ruta.read_text(encoding="utf-8"))
            if not isinstance(data, list):
                raise ValueError("El JSON no contiene una lista de productos.")
            return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}")

    @staticmethod
    def __cargar_productos() -> list:
        """### Convierte la lista de dicts cargada desde JSON en objetos Producto.
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

    def guardar_cambios(self):
        """### Guarda los cambios realizados en la lista interna sobrescribiendo el JSON.
        """
        with self.__class__.__ruta.open("w", encoding="utf-8") as f:
            json.dump(
                [producto.a_dict() for producto in self.__class__.__lista_producto],
                f,
                ensure_ascii=False,
                indent=4
            )

    def get_precio(self, id: ProductoID) -> tuple:
        """### Obtiene los precios asociados a un producto mediante su ProductoID.

        Ahora delega la consulta a la instancia de PrecioRepository asociada
        (self._precio_repo) para ser compatible con la versión por instancia.

        Raises:
            ValueError: Si el producto no existe.
        Returns:
            tuple: Tupla con objetos Precio.
        """
        if self.existe(id):
            return self._precio_repo.get_precio(id)
        raise ValueError("Precios inexistente")