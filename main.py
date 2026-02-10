#!/usr/bin/env python3
from Model import ProductoRepository, PrecioRepository, ProductoID

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
"""### ejemplo de uso 
```
______________________________________________________________________
    repo = ProductoRepository()          # carga datos la primera vez
    nuevo = repo.new_producto(ProductoID(1))
    nuevo.set_name("ejemplo")
    repo.incluir_producto(nuevo)         # persiste en JSON
______________________________________________________________________
```
"""