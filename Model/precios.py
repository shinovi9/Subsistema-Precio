#!/usr/bin/env python3
import json
from pathlib import Path

class Precios:
    """Gestiona los Precios de los productos"""
    __precios: dict
    
    @staticmethod
    def __cargar_data() -> dict:
        """## Carga los Precios desde el archivo JSON
        
        Returns:
            dict: Diccionario con los Precios {nombre_producto: Precios}
        
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
        print(f"Error al cargar Precios: {e}")
        __precios = {}
    
    @staticmethod
    def getPriceFor(nombre_producto: str) -> float:
        """## Obtiene el Precios de un producto dado su nombre
        
        Args:
            nombre_producto (str): Nombre del producto (ej: 'leche')
        
        Returns:
            float: Precios del producto
        
        Raises:
            ValueError: Si el producto no existe
        """
        if not Precios.__precios:
            raise ValueError("No hay datos de Precios cargados")
        
        if nombre_producto not in Precios.__precios:
            raise ValueError(f"Producto '{nombre_producto}' no encontrado")
        
        return Precios.__precios[nombre_producto]
    
    @staticmethod
    def productos() -> tuple:
        """## Obtiene todos los nombres de productos disponibles
        
        Returns:
            tuple: Todos los nombres de productos
        """
        return tuple(Precios.__precios.keys())
    
    @staticmethod
    def update(nombre_producto: str, Precios: float):
        """## Actualiza o agrega un Precios de producto
        
        Args:
            nombre_producto (str): Nombre del producto
            Precios (float): Nuevo Precios del producto
        
        Raises:
            ValueError: Si el Precios no es un número positivo
        """
        if not isinstance(Precios, (int, float)) or Precios <= 0:
            raise ValueError(f"El Precios debe ser un número positivo. Se recibió: {Precios}")
        
        # Actualizar el diccionario interno
        Precios.__precios[nombre_producto] = float(Precios)
        print(f"✓ Precio actualizado: {nombre_producto} = {Precios}")
    
    @staticmethod
    def save():
        """## Guarda los Precios actualizados en el archivo JSON
        
        Este método sobrescribe el archivo Precios.json con los valores actuales
        """
        try:
            # Obtener la ruta al archivo JSON
            ruta = Path("./Data/precios.json")
            
            # Asegurarse de que el directorio existe
            ruta.parent.mkdir(parents=True, exist_ok=True)
            
            # Guardar con formato legible 
            ruta.write_text(
                json.dumps(Precios.__precios, indent=2, ensure_ascii=False), 
                encoding="utf-8"
            )
            print("✓ Archivo precios.json guardado exitosamente")
            
        except Exception as e:
            raise IOError(f"No se pudo guardar el archivo: {e}")
    
    @staticmethod
    def mostrarPrecios():
        """## Muestra todos los Precios en formato clave: valor
        
        Imprime el diccionario completo de Precios 
        """
        if not Precios.__precios:
            print("No hay Precios cargados")
            return
        
        print("\nLISTA DE Precios")
        for producto, Precios in Precios.__precios.items():
            print(f"{producto}: ${Precios:.2f}")
        print(f"Total: {len(Precios.__precios)} productos")
    
    @staticmethod
    def delete(nombre_producto: str):
        """## Elimina un producto de la lista de Precios
        
        Args:
            nombre_producto (str): Nombre del producto a eliminar
        
        Raises:
            ValueError: Si el producto no existe
        """
        if not Precios.__precios:
            raise ValueError("No hay datos de Precios cargados")
        
        if nombre_producto not in Precios.__precios:
            raise ValueError(f"Producto '{nombre_producto}' no encontrado")
        
        # Eliminar el producto del diccionario
        del Precios.__precios[nombre_producto]
        print(f"✓ Producto '{nombre_producto}' eliminado exitosamente")

