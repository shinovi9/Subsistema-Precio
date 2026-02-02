#!/usr/bin/env python3
import json
from pathlib import Path

class Precios(dict):
    """Gestiona los precios de los productos"""
    
    __ruta_archivo = Path("./Data/precios.json")
    
    def __init__(self):
        """Inicializa el diccionario cargando datos del archivo JSON"""
        super().__init__()
        self.__cargar_data()
    
    def __cargar_data(self):
        """## Carga los precios desde el archivo JSON
        
        Raises:
            FileNotFoundError: Si el archivo no existe
        """
        if not self.__ruta_archivo.exists():
            raise FileNotFoundError("Archivo no encontrado")
        
        # Si el archivo existe, cargarlo
        try:
            datos = json.loads(self.__ruta_archivo.read_text(encoding="utf-8"))
            self.clear()  
            self.update(datos)  
        except json.JSONDecodeError:
            raise ValueError(f"Error al leer el archivo JSON: {self.__ruta_archivo}")
    
    def __setitem__(self, key, value):
        """## Sobreescribe la asignación para validar que el precio sea positivo
        
        Args:
            key (str): Nombre del producto
            value (float): Precio del producto
        
        Raises:
            ValueError: Si el precio no es un número positivo
        """
        if not isinstance(value, (int, float)):
            raise ValueError(f"El precio debe ser un número. Se recibió: {value} ({type(value)})")
        
        if value <= 0:
            raise ValueError(f"El precio debe ser positivo. Se recibió: {value}")
        
        super().__setitem__(key, float(value))
    
    def update(self, other=None, **kwargs):
        """## Sobreescribe update para validar que todos los precios sean positivos
        
        Args:
            other (dict/iterable, optional): Diccionario o iterable de pares clave-valor
            **kwargs: Argumentos de palabra clave
        
        Raises:
            ValueError: Si algún precio no es positivo
        
        Examples:
            >>> precios.update({'prod1': 150.0, 'prod2': 200.0})
            >>> precios.update(prod1=150.0, prod2=200.0)
            >>> precios.update([('prod1', 150.0), ('prod2', 200.0)])
        """
        if other is not None:
            # Manejar diferentes tipos de entrada
            if hasattr(other, 'items'):
                # Diccionario o similar
                for key, value in other.items():
                    self.__setitem__(key, value)
            elif hasattr(other, '__iter__'):
                # Iterable de pares (clave, valor)
                for key, value in other:
                    self.__setitem__(key, value)
            else:
                raise TypeError(f"Tipo no soportado para update: {type(other)}")
        
        # Manejar argumentos de palabra clave
        for key, value in kwargs.items():
            self.__setitem__(key, value)
    
    def getPriceFor(self, nombre_producto: str) -> float:
        """## Obtiene el Precio de un producto dado su nombre
        
        Args:
            nombre_producto (str): Nombre del producto (ej: 'leche')
        
        Returns:
            float: Precio del producto
        
        Raises:
            ValueError: Si el producto no existe
        """
        if not self:
            raise ValueError("No hay datos de precios cargados")
        
        if nombre_producto not in self:
            raise ValueError(f"Producto '{nombre_producto}' no encontrado")
        
        return self[nombre_producto]
    
    def productos(self) -> tuple:
        """## Obtiene todos los nombres de productos disponibles
        
        Returns:
            tuple: Todos los nombres de productos
        """
        return tuple(self.keys())
    
    def save(self):
        """## Guarda los precios actualizados en el archivo JSON
        
        Este método sobrescribe el archivo Precios.json con los valores actuales
        """
        try:
            # Asegurarse de que el directorio existe
            self.__ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
            
            # Guardar con formato legible 
            self.__ruta_archivo.write_text(
                json.dumps(self, indent=2, ensure_ascii=False), 
                encoding="utf-8"
            )
            print("✓ Archivo precios.json guardado exitosamente")
            
        except Exception as e:
            raise IOError(f"No se pudo guardar el archivo: {e}")
    
    def mostrarPrecios(self):
        """## Muestra todos los Precios en formato clave: valor
        
        Imprime el diccionario completo de Precios 
        """
        if not self:
            print("No hay Precios cargados")
            return
        
        print("\nLISTA DE PRECIOS")
        for producto, precio in self.items():
            print(f"{producto}: ${precio:.2f}")
        print(f"Total: {len(self)} productos")

