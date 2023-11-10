from piloto import Piloto
from mecanico import Mecanico
from director import Director
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste

class Equipo:
    def __init__(self, nombre:str, pais:str, creacion, score, auto):
        self._nombre = nombre
        self._pais = pais
        self._creacion = creacion
        self._score = score
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
    @property
    def score(self):
        return self._score
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    @auto.setter
    def auto(self, nuevo_auto):
        self._auto = nuevo_auto
    @pais.setter
    def pais(self, nuevo_pais):
        self._pais = nuevo_pais
    @score.setter
    def score(self, nuevo_score):
        self._score = nuevo_score
    
    #def buscar_empleado(self, id):
        empleado_encontrado = None
        for empleado in self._empleados:
            if empleado.id == id:
                empleado_encontrado = empleado
        return empleado_encontrado
    
    #def es_piloto(self, id):
        empleado = Equipo.buscar_empleado(id)
        if empleado == None:
            raise EmpleadoNoExiste(410, "El empleado ingresado no forma parte del equipo")
        else:
            es_piloto = isinstance(empleado, Piloto)
        return es_piloto
    
    #def es_mecanico(self, id):
        empleado = Equipo.buscar_empleado(id)
        if empleado == None:
            raise EmpleadoNoExiste(410, "El empleado ingresado no forma parte del equipo")
        else:
            es_mecanico = isinstance(empleado, Mecanico)
        return es_mecanico
    
    #def es_director(self, id):
        empleado = Equipo.buscar_empleado(id)
        if empleado == None:
            raise EmpleadoNoExiste(410, "El empleado ingresado no forma parte del equipo")
        else:
            es_director = isinstance(empleado, Director)
        return es_director
