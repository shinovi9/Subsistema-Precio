#!/usr/bin/env python3
import json
from pathlib import Path

class Precio:
    """Gestiona los precios de los productos"""
    __precios: dict
    
    @staticmethod
    def __cargar_data() -> dict:
        """## Carga los precios desde el archivo JSON
        
        Returns:
            dict: Diccionario con los precios {nombre_producto: precio}
        
        Raises:
            FileNotFoundError: Si el archivo no existe
        """
        ruta = Path("./Data/precios.json")
        
        if not ruta.exists():
            raise FileNotFoundError("Archivo no encontrado")
        
        # Si el archivo existe, cargarlo
        try:
            datos = json.loads(ruta.read_text(encoding="utf-8"))
            return datos
        except json.JSONDecodeError:
            raise ValueError(f"Error al leer el archivo JSON: {ruta}")
        except StopIteration:
            raise ValueError(f"El archivo JSON está vacío: {ruta}")
    
    # Carga los datos al definir la clase
    try:
        __precios = __cargar_data()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        __precios = {}
    except Exception as e:
        print(f"Error al cargar precios: {e}")
        __precios = {}
    
    @staticmethod
    def getPriceFor(nombre_producto: str) -> float:
        """## Obtiene el precio de un producto dado su nombre
        
        Args:
            nombre_producto (str): Nombre del producto (ej: 'leche')
        
        Returns:
            float: Precio del producto
        
        Raises:
            ValueError: Si el producto no existe
        """
        if not Precio.__precios:
            raise ValueError("No hay datos de precios cargados")
        
        if nombre_producto not in Precio.__precios:
            raise ValueError(f"Producto '{nombre_producto}' no encontrado")
        
        return Precio.__precios[nombre_producto]
    
    @staticmethod
    def productos() -> tuple:
        """## Obtiene todos los nombres de productos disponibles
        
        Returns:
            tuple: Todos los nombres de productos
        """
        return tuple(Precio.__precios.keys())
    
    @staticmethod
    def update(nombre_producto: str, precio: float):
        """## Actualiza o agrega un precio de producto
        
        Args:
            nombre_producto (str): Nombre del producto
            precio (float): Nuevo precio del producto
        
        Raises:
            ValueError: Si el precio no es un número positivo
        """
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError(f"El precio debe ser un número positivo. Se recibió: {precio}")
        
        # Actualizar el diccionario interno
        Precio.__precios[nombre_producto] = float(precio)
        print(f"✓ Precio actualizado: {nombre_producto} = {precio}")
    
    @staticmethod
    def save():
        """## Guarda los precios actualizados en el archivo JSON
        
        Este método sobrescribe el archivo precios.json con los valores actuales
        """
        try:
            # Obtener la ruta al archivo JSON
            ruta = Path("./Data/precios.json")
            
            # Asegurarse de que el directorio existe
            ruta.parent.mkdir(parents=True, exist_ok=True)
            
            # Guardar con formato legible 
            ruta.write_text(
                json.dumps(Precio.__precios, indent=2, ensure_ascii=False), 
                encoding="utf-8"
            )
            print("✓ Archivo precios.json guardado exitosamente")
            
        except Exception as e:
            raise IOError(f"No se pudo guardar el archivo: {e}")
    
    @staticmethod
    def mostrarPrecios():
        """## Muestra todos los precios en formato clave: valor
        
        Imprime el diccionario completo de precios 
        """
        if not Precio.__precios:
            print("No hay precios cargados")
            return
        
        print("\nLISTA DE PRECIOS")
        for producto, precio in Precio.__precios.items():
            print(f"{producto}: ${precio:.2f}")
        print(f"Total: {len(Precio.__precios)} productos")
    
    @staticmethod
    def delete(nombre_producto: str):
        """## Elimina un producto de la lista de precios
        
        Args:
            nombre_producto (str): Nombre del producto a eliminar
        
        Raises:
            ValueError: Si el producto no existe
        """
        if not Precio.__precios:
            raise ValueError("No hay datos de precios cargados")
        
        if nombre_producto not in Precio.__precios:
            raise ValueError(f"Producto '{nombre_producto}' no encontrado")
        
        # Eliminar el producto del diccionario
        del Precio.__precios[nombre_producto]
        print(f"✓ Producto '{nombre_producto}' eliminado exitosamente")

