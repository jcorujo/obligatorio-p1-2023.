from entities.empleado import Empleado

class Mecanico(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self._score = score
        self._equipo = None
        
    @property
    def score(self):
        return self._score
    @property
    def equipo(self):
        return self._equipo
    
    @score.setter
    def score(self, new_score):
        self._score = new_score
    @equipo.setter
    def equipo(self, equipo):
        self._equipo = equipo
    