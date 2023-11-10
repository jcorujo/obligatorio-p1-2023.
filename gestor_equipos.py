from gestor_personal import Gestor_Personal
from entities.equipo import Equipo
from entities.piloto import Piloto
from datetime import datetime
from exceptions.EquipoNoExiste import EquipoNoExiste
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
            if (equipo.nombre == nombre_equipo or isinstance(nombre_equipo, Equipo)):
                equipo_encontrado = equipo
        if equipo_encontrado == None:
            raise EquipoNoExiste(415, "El equipo ingresado no existe")
        return equipo_encontrado
     
    def agregar_equipo(self, equipo):
        #Verificar que equipo no exista
        pass
    def tiene_capacidad(self, equipo, tipo_empleado):
        equipo = Gestor_Equipos.buscar_equipo(equipo)
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
                return None
            case 2:
                pilotos = personal.obtener_pilotos()
                for piloto in pilotos:
                    if not piloto.es_titular:
                        raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de pilotos de reserva")
                return None
            case 3:
                for empleado in personal._empleados:
                    if empleado.es_director:
                        raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de directores")
                return None
            case _:
                raise ArgumentoInvalido(420, "El tipo de empleado ingresado es inválido")


    def agregar_piloto(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular):
        #VERIFICAR EXISTENCIA EQUIPO
        equipo_piloto = Gestor_Equipos.buscar_equipo(self, equipo)
        #VERIFICAR CAPACIDAD
        if es_titular == True:
            Gestor_Equipos.tiene_capacidad(equipo, 1)
        else:
            Gestor_Equipos.tiene_capacidad(equipo, 2)
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for equipo in self._equipos:
            personal = Gestor_Personal(equipo)
            if personal.buscar_empleado(id) != None:
                raise EmpleadoEnOtroEquipo(411, "Ese piloto ya forma parte de un equipo")
        personal = Gestor_Personal(equipo)
        personal.agregar_piloto(nombre, id, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular)
            
    def agregar_mecanico(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario, score):
        #VERIFICAR EXISTENCIA EQUIPO
        equipo_piloto = Gestor_Equipos.buscar_equipo(self, equipo)
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for equipo in self._equipos:
            personal = Gestor_Personal(equipo)
            if personal.buscar_empleado(id) != None:
                raise EmpleadoEnOtroEquipo(411, "Ese mecánico ya forma parte de un equipo")
        personal = Gestor_Personal(equipo)
        personal.agregar_mecanico(nombre, id, fecha_nacimiento, nacionalidad, salario, score) 
    
    def agregar_director(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario):
        #VERIFICAR EXISTENCIA EQUIPO
        equipo_piloto = Gestor_Equipos.buscar_equipo(self, equipo)
        #VERIFICAR CAPACIDAD
        Gestor_Equipos.tiene_capacidad(equipo, 3)
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for equipo in self._equipos:
            personal = Gestor_Personal(equipo)
            if personal.buscar_empleado(id) != None:
                raise EmpleadoEnOtroEquipo(411, "Ese director ya forma parte de un equipo")
        personal = Gestor_Personal(equipo)
        personal.agregar_director(nombre, id, fecha_nacimiento, nacionalidad, salario)
  

    def habilitados_para_correr(self):
            
        #checkear capacidad pilotos
        #return pilotos que corren
        #return a list
        pass
    def puede_participar(self):
        pass
        #checkear que tiene al menos un piloto
        #checkear que tiene los mecanicos necesarios
        #checkear que no falta un director
    def obtener_puntajes_pilotos(self):
        pass
    
Equipo1 = Equipo("Equipo1", "Uruguay", 1990, 80, "ModeloY" )
Equipo2 = Equipo("Equipo2", "Uruguay",1990, 80, "ModeloX")
Gestor = Gestor_Equipos([Equipo1, Equipo2])
print(Gestor.equipos)
Gestor.agregar_piloto("Equipo3",5555555, "Julio", datetime(2003, 4, 17), "uruguayo", 2000, 312321)