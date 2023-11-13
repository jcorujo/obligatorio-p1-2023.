from gestor_personal import Gestor_Personal
from entities.equipo import Equipo
from entities.piloto import Piloto
from datetime import datetime
from exceptions.EquipoNoExiste import EquipoNoExiste
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste
from exceptions.ArgumentoInvalido import ArgumentoInvalido
from exceptions.EmpleadoEnOtroEquipo import EmpleadoEnOtroEquipo
from exceptions.EquipoSinCapacidad import EquipoSinCapacidad

#SACAR IMPORTACIONES INNECESARIAS (datetime) AL TERMINAR PRUEBAS

class Gestor_Equipos:
    def __init__(self, equipos:list):
        #¿cuales son los argumentos, los nombres de los equipos o los nombres de las instancias?
        self._equipos = equipos
    
    @property
    def equipos(self):
        return self._equipos
    
    def buscar_equipo(self, nombre_equipo):
        equipo_encontrado = None
        for equipo in self._equipos:
            if ((equipo.nombre).lower() == nombre_equipo or isinstance(nombre_equipo, Equipo)):
                equipo_encontrado = equipo
        return equipo_encontrado
     
    def tiene_capacidad(self, equipo, tipo_empleado):
        equipo = Gestor_Equipos.buscar_equipo(self, equipo)
        personal = Gestor_Personal(equipo)
        match tipo_empleado:
            case 1:
                pilotos = personal.obtener_pilotos()
                titulares = 0
                for piloto in pilotos:
                    if piloto.es_titular:
                        titulares += 1
                if titulares == 2:
                    raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de pilotos titulares")
                return True
            case 2:
                pilotos = personal.obtener_pilotos()
                for piloto in pilotos:
                    if not piloto.es_titular:
                        raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de pilotos de reserva")
                return True
            case 3:
                for empleado in personal._empleados:
                    if personal.es_director(empleado.id):
                        raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de directores")
                return True
            case _:
                raise ArgumentoInvalido(420, "El tipo de empleado ingresado es inválido")


    def agregar_piloto(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular):
        #VERIFICAR EXISTENCIA EQUIPO
        equipo_ingreso = Gestor_Equipos.buscar_equipo(self, equipo)
        if equipo_ingreso == None:
            raise EquipoNoExiste(415, "El equipo ingresado no existe")
        #VERIFICAR CAPACIDAD
        if es_titular:
            self.tiene_capacidad(equipo, 1)
        elif not es_titular:
            self.tiene_capacidad(equipo, 2)
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for team in self._equipos:
            personal = Gestor_Personal(team)
            if personal.buscar_empleado(id) != None:
                raise EmpleadoEnOtroEquipo(411, f"Ese piloto ya forma parte de un equipo: {equipo.nombre}")
        personal = Gestor_Personal(equipo)
        personal.agregar_piloto(nombre, id, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular)
    
    def agregar_mecanico(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario, score):
        #VERIFICAR EXISTENCIA EQUIPO
        equipo_ingreso = Gestor_Equipos.buscar_equipo(self, equipo)
        if equipo_ingreso == None:
            raise EquipoNoExiste(415, "El equipo ingresado no existe")
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for team in self._equipos:
            personal = Gestor_Personal(team)
            if personal.buscar_empleado(id) != None:
                raise EmpleadoEnOtroEquipo(411, "Ese mecánico ya forma parte de un equipo")
        personal = Gestor_Personal(equipo)
        personal.agregar_mecanico(nombre, id, fecha_nacimiento, nacionalidad, salario, score) 
    
    def agregar_director(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario):
        #VERIFICAR EXISTENCIA EQUIPO
        equipo_ingreso= Gestor_Equipos.buscar_equipo(self, equipo)
        if equipo_ingreso == None:
            raise EquipoNoExiste(415, "El equipo ingresado no existe")
        #VERIFICAR CAPACIDAD
        Gestor_Equipos.tiene_capacidad(self, equipo, 3)
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for team in self._equipos:
            personal = Gestor_Personal(team)
            if personal.buscar_empleado(id) != None:
                raise EmpleadoEnOtroEquipo(411, "Ese director ya forma parte de un equipo")
        personal = Gestor_Personal(equipo)
        personal.agregar_director(nombre, id, fecha_nacimiento, nacionalidad, salario)
    
    def puede_participar(self, equipo):
        personal = Gestor_Personal(equipo)
        if len(personal.habilitados_para_correr()) > 0:
            mecanicos = personal.obtener_mecanicos()
            if len(mecanicos) > 7:
                for empleado in personal._empleados:
                    if personal.es_director(empleado.id):
                        return True
        return False
    
    def encontrar_empleado(self, id_empleado):
        for equipo in self._equipos:
            personal = Gestor_Personal(equipo)
            empleado = personal.verificar_empleado(id_empleado)
            if empleado != None:
                return empleado
        raise EmpleadoNoExiste(410, "El empleado ingresado no existe, ingrese un id válido") 