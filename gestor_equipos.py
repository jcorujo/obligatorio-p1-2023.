
from entities.equipo import Equipo
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.director import Director
from exceptions.EquipoNoExiste import EquipoNoExiste
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste
from exceptions.ArgumentoInvalido import ArgumentoInvalido
from exceptions.EmpleadoEnOtroEquipo import EmpleadoEnOtroEquipo
from exceptions.EquipoSinCapacidad import EquipoSinCapacidad

#LLEVAR METODOS A CLASE EQUIPO
class Gestor_Equipos:
    def __init__(self, equipos:list):
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
    
    def buscar_empleado(self, id):
              empleado_encontrado = None
              for empleado in self._empleados: 
                     if empleado.id == id:
                            empleado_encontrado = empleado
              return empleado_encontrado   
       
    def agregar_piloto(self, equipo,nombre,id,fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular):
        #VERIFICAR EXISTENCIA EQUIPO
        if self.buscar_equipo(equipo) == None:
            raise EquipoNoExiste(415, "El equipo ingresado no existe")
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for eq in self._equipos:
                if eq.buscar_empleado(id) != None:
                    raise EmpleadoEnOtroEquipo(411, f"Ese piloto ya forma parte de un equipo: {equipo.nombre}")
        #VERIFICAR QUE EQUIPO TENGA CAPACIDAD
        if es_titular:
            if not self.tiene_capacidad(equipo, 1):
                raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de pilotos titulares")
        elif not es_titular:
            if self.tiene_capacidad(equipo, 2) == False:
                raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de pilotos de reserva")
        piloto = Piloto(id, nombre, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular)
        equipo.agregar_empleado(piloto)
        piloto.equipo = equipo
       
    def agregar_mecanico(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario, score):
        if self.buscar_equipo(equipo) == None:
            raise EquipoNoExiste(415, "El equipo ingresado no existe")
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for eq in self._equipos:
                if eq.buscar_empleado(id) != None:
                    raise EmpleadoEnOtroEquipo(411, f"Ese mecánico ya forma parte de un equipo: {equipo.nombre}")
        mecanico = Mecanico(id, nombre, fecha_nacimiento, nacionalidad, salario, score)
        equipo.agregar_empleado(mecanico)
        mecanico.equipo = equipo
       
    def agregar_director(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario):   
        #VERIFICAR EXISTENCIA EQUIPO
        if self.buscar_equipo(equipo) == None:
            raise EquipoNoExiste(415, "El equipo ingresado no existe")
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for eq in self._equipos:
                if eq.buscar_empleado(id) != None:
                    raise EmpleadoEnOtroEquipo(411, f"Ese director ya forma parte de un equipo: {equipo.nombre}")       
        #VERIFICAR CAPACIDAD
        if not Gestor_Equipos.tiene_capacidad(self, equipo, 3):
             raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de directores")
        director = Director(id, nombre, fecha_nacimiento, nacionalidad, salario)
        equipo.agregar_empleado(director)
        director.equipo = equipo

    def tiene_capacidad(self, equipo, tipo_empleado):
        equipo = self.buscar_equipo(equipo)
        match tipo_empleado:
        
            case 1:
                pilotos = equipo.obtener_pilotos()
                titulares = 0
                for piloto in pilotos:
                    if piloto.es_titular:
                        titulares += 1
                if titulares == 2:
                    return False
                return True
            case 2:
                pilotos = equipo.obtener_pilotos()
                for piloto in pilotos:
                    print("paso 1")
                    es_titular = piloto.es_titular
                    if not es_titular:
                        return False
                
            case 3:
                for empleado in equipo._empleados:
                    if equipo.es_director(empleado.id):
                        return False
                return True
            case _:
                raise ArgumentoInvalido(420, "El tipo de empleado ingresado es inválido")

    def puede_participar(self, equipo):
        if len(equipo.habilitados_para_correr()) > 0:
            mecanicos = equipo.obtener_mecanicos()
            if len(mecanicos) > 7:
                for empleado in equipo.empleados:
                    if equipo.es_director(empleado.id):
                        return True
        return False
    
    #def encontrar_empleado(self, id_empleado):
        for equipo in self._equipos:
            personal = Gestor_Personal(equipo)
            empleado = personal.verificar_empleado(id_empleado)
            if empleado != None:
                return empleado
        raise EmpleadoNoExiste(410, "El empleado ingresado no existe, ingrese un id válido") 