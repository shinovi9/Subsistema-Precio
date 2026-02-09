#!/usr/bin/env python3
from Model.Repository.productoRepository import ProductoRepository
from Model.ValueObject.productoID import ProductoID
from Model.ValueObject.precio import Precio
from interfaces import IPrecioProvider
from pathlib import Path
import json

class PrecioRepository(IPrecioProvider):
    """### ejemplo de uso
    ```
    ______________________________________________________________________________________________
        # crear repositorios (precio_repo recibe opcionalmente producto_repo)
        producto_repo = ProductoRepository()                 # carga productos desde JSON
        precio_repo = PrecioRepository(producto_repo)        # carga precios desde JSON

        # crear un nuevo precio para un producto existente
        pid = ProductoID(2)
        nuevo_precio = precio_repo.new_precio(pid, 1009.0)   # valida que el producto exista
        precio_repo.incluir_precio(nuevo_precio)             # añade y persiste en JSON

        # obtener todos los precios de un producto (tupla)
        precios = precio_repo.get_precio(pid)

        # eliminar un precio específico (producto_id, valor)
        precio_repo.eliminar_precio(pid, 1009.0)

        # comprobar que se eliminó (buscar_por_id lanzará OverflowError si no hay precios)
        try:
            precios = precio_repo.buscar_por_id(pid)
        except OverflowError:
            print("No hay precios para el producto", pid)
    ____________________________________________________________________________________________
    ```
    """
    # Ruta del archivo JSON (sube un nivel y entra a Data/)
    __directorio_actual = Path(__file__).parent.parent
    __ruta = __directorio_actual.parent / "Data" / "Precios" / "PreciosDB.json"

    def __init__(self, producto_repo=None):
        """
        Inicializa el repositorio de precios.
        Carga los precios desde el JSON y guarda la lista en self._lista_precios.
        Recibe opcionalmente una instancia de ProductoRepository para validaciones.
        """
        self._producto_repo = producto_repo or ProductoRepository()
        self._lista_precios = self.__cargar_precios()

    def new_precio(self, producto, valor):
        """
        Crea un nuevo objeto Precio asociado a un ProductoID existente.

        Raises:
            ValueError: Si el ProductoID indicado no existe en el repositorio de productos.
        Returns:
            Precio: El nuevo objeto Precio creado.
        """
        if self._producto_repo.existe(producto):
            return Precio(producto, valor)
        raise ValueError("Producto inexistente")

    def incluir_precio(self, precio):
        """
        Incluye un nuevo precio en la lista de la instancia y guarda los cambios.
        """
        self._lista_precios.append(precio)
        self.guardar_cambios()

    def buscar_por_id(self, id):
        """
        Busca y devuelve todos los precios asociados a un producto mediante su ProductoID.

        Raises:
            OverflowError: Si no existen precios registrados para el ProductoID indicado.
        Returns:
            list: Lista de objetos Precio correspondientes al ProductoID solicitado.
        """
        coincidencias = [p for p in self._lista_precios if p.producto__id == id]
        if coincidencias:
            return coincidencias
        raise OverflowError(f"No hay precios actualmente de este producto {id}")

    @staticmethod
    def __cargar_Data():
        """
        Carga la base de datos de precios desde PreciosDB.json.
        Crea el archivo/carpeta si no existen y devuelve la lista de dicts.
        """
        ruta = PrecioRepository.__ruta
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
                raise ValueError("El JSON no contiene una lista de precios.")
            return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}")

    @staticmethod
    def __cargar_precios():
        """
        Carga los precios desde la fuente de datos JSON y los convierte en objetos Precio.
        """
        lista_dict_Precios = PrecioRepository.__cargar_Data()
        lista_precios = []

        for precio_dict in lista_dict_Precios:
            id_obj = ProductoID(precio_dict["producto"])
            valor = precio_dict["valor"]
            precio = Precio(id_obj, valor)
            lista_precios.append(precio)
        return lista_precios

    def guardar_cambios(self):
        """
        Guarda los cambios realizados en la lista de la instancia sobrescribiendo el JSON.
        """
        with self.__class__.__ruta.open("w", encoding="utf-8") as f:
            json.dump(
                [precio.a_dict() for precio in self._lista_precios],
                f,
                ensure_ascii=False,
                indent=4
            )

    def get_precio(self, id_producto):
        """
        Obtiene todos los precios asociados a un producto mediante su ProductoID.

        Raises:
            ValueError: Si el producto indicado no existe en el repositorio de productos.
        Returns:
            tuple: Una tupla con los objetos Precio correspondientes al ProductoID solicitado.
        """
        if self._producto_repo.existe(id_producto):
            return tuple(self.buscar_por_id(id_producto))
        raise ValueError("Precios inexistente")

    def eliminar_precio(self, producto_id, valor):
        """
        Elimina un precio específico de la lista de la instancia, identificado por su ProductoID y valor.

        Raises:
            ValueError: Si no se encuentra un precio con el ProductoID y valor indicados.
        """
        precio_obj = next(
            (p for p in self._lista_precios if p.producto__id == producto_id and p.valor == valor),
            None
        )
        if precio_obj:
            self._lista_precios.remove(precio_obj)
            self.guardar_cambios()
            return
        raise ValueError(f"No existe un precio con ProductoID={producto_id} y valor={valor}")