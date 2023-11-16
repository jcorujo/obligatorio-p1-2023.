from entities.empleado import Empleado
class Director(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self._equipo = None

    @property
    def equipo(self):
        return self._equipo
    
    @equipo.setter
    def equipo(self, equipo):
        self._equipo = equipo