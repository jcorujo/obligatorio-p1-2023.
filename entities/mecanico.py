from entities.empleado import Empleado
class Mecanico(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init___(id, nombre, fecha_nacimiento, nacionalidad, salario, score)
        self._score = score
    
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, new_score):
        self._score = new_score