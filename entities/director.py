from entities.empleado import Empleado
class Director(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init___(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self._score = score

    @property
    def score(self):
        return self._score
