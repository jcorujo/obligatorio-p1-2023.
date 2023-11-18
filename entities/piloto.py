from entities.empleado import Empleado


class Piloto(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular: bool):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self._nro_auto = nro_auto 
        self._esta_lesionado = False
        self._es_titular = es_titular
        self._score = score
        self._puntaje_campeonato = 0
        self._puntaje_carrera = 0
        self._equipo = None
    
    @property
    def nro_auto(self) -> int:
        return self._nro_auto
    
    @property
    def score(self) -> int:
        return self._score
    
    @property
    def esta_lesionado(self) -> bool:
        return self._esta_lesionado
    
    @property
    def es_titular(self) -> bool:
        return self._es_titular
    
    @property
    def puntaje_campeonato(self) -> int:
        return self._puntaje_campeonato
    
    @property
    def puntaje_carrera(self) -> int:
            return self._puntaje_carrera
    
    @property
    def equipo(self):
        return self._equipo
    
    @nro_auto.setter
    def nro_auto(self, nro_nuevo:int):
        self._nro_auto = nro_nuevo
    
    @esta_lesionado.setter
    def esta_lesionado(self, estado:bool):
        self._esta_lesionado = estado
    
    @es_titular.setter
    def es_titular(self, es_titular:bool):
        self._es_titular = es_titular
    
    @equipo.setter
    def equipo(self, equipo):
        self._equipo = equipo
    
    @puntaje_carrera.setter
    def puntaje_carrera(self, puntaje):
        self._puntaje_carrera = puntaje
    
    @puntaje_campeonato.setter
    def puntaje_campeonato(self, puntaje):
        self._puntaje_campeonato = puntaje
    
    def agregar_puntaje_carrera(self, puntaje):
        self.puntaje_carrera += puntaje
    
    def agregar_puntaje_campeonato(self, puntaje):
        self._puntaje_campeonato += puntaje
    
