from entities.empleado import Empleado
class Director(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
