class Proveedores:
    def __init__(self, _nombre , _empresa , _marca, _manejoProveedores ) -> None:
        self.nombre = _nombre
        self.empresa = _empresa
        self.marca = _marca
        self.manejoProveedores= _manejoProveedores
    def crear (self):
        print ("aca se crea {self.nombre}")
    def leer (self):
        print ()
    def actualizar (self):
        print ()
    def eliminar (self):
        print()

proveer = Proveedores ("", "" , "" , "", "")
proveer.crear()
