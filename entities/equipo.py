class Equipo:
    def __init__(self, nombre:str, pais:str, creacion,auto):
        self._nombre = nombre
        self._pais = pais
        self._creacion = creacion
        self._auto = auto
        self._empleados = []
    
    @property
    def nombre(self) -> str:
        return self._nombre 
    @property
    def pais(self) -> str:
        return self._pais
    #FECHAS
    @property
    def creacion(self) -> int:
        return self._creacion
    @property
    def empleados(self):
        return self._empleados
    @property
    def auto(self):
        return self._auto

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    @auto.setter
    def auto(self, nuevo_auto):
        self._auto = nuevo_auto
    @pais.setter
    def pais(self, nuevo_pais):
        self._pais = nuevo_pais
   
    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)
