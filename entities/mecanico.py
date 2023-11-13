from entities.empleado import Empleado
class Mecanico(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self._score = score
        self._puntaje_campeonato = 0
    
    @property
    def score(self):
        return self._score
    @property
    def puntaje_campeonato(self) -> int:
        return self._puntaje_campeonato
    @score.setter
    def score(self, new_score):
        self._score = new_score