from productos import Productos
from ventas import Ventas
from proveedores import Proveedores
import db.py

opcion = input("elija que desea realizar:")
if opcion== "Crear":
    nombre= input("ingrese nombre: ")
    empresa= input("ingrese empresa: ")
    marca= input ("ingrese marca: ")
    manejoProveedores= input ("ingrese el manejo de proveedores:")
    proveedor = Proveedores(nombre, empresa, marca, manejoProveedores )
    proveedor.crear()
elif opcion== "Leer":
    proveedor = Proveedores(nombre, empresa, marca, manejoProveedores )
    proveedor.leer()
elif opcion== "Actualizar":
    proveedor = Proveedores(nombre, empresa, marca, manejoProveedores )
    proveedor.actualizar()
    proveedor = Proveedores(nombre, empresa, marca, manejoProveedores )
else: proveedor.eliminar()








        