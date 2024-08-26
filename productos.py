from proveedores import Proveedores
class Productos:
    def __init__(self, _nombre , _vencimiento , _marca , _lote, _proveedores) -> None:
        self.nombre = _nombre
        self.vencimiento = _vencimiento
        self.marca = _marca
        self.lote = _lote
        self.proveedores = _proveedores
    def crear (self):
        print ("aca se crea {self.nombre}")
    def leer (self):
        print ()
    def actualizar (self):
        print ()
    def eliminar (self):
        print ()
     
     
    



producto = Productos ("coca", "" , "" , "", "")
producto.crear()


        