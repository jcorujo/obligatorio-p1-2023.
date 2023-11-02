from abc import ABC, abstractmethod

class Empleados(ABC):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        self._id = id
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._nacionalidad = nacionalidad
        self._salario = salario

    @property
    def id(self):
        return self._id
    @property
    def nombre(self):
        return self._nombre
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    @property
    def nacionalidad(self):
        return self._nacionalidad
    @property
    def salario(self):
        return self._salario
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        self._nacionalidad = nueva_nacionalidad
    @salario.setter
    def salario(self, nuevo_salario):
        self._salario = nuevo_salario
    