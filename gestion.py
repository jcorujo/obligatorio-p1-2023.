from exceptions.Argumento_Invalido import ArgumentoInvalido
from exceptions.EmpleadoEnEquipo import EmpleadoEnEquipo
from exceptions.EquipoSinCapacidad import  EquipoSinCapacidad
from entities.equipo import Equipo
from entities.campeonato import Campeonato

class Gestion:
    def __init__(self):
        self._empleados = []
        self._autos = []
        self._equipos = []
        self._campeonato = Campeonato(self._equipos)
    
    @property
    def empleados(self):
        return self._empleados
    
    @property
    def autos(self):
        return self._autos
    
    @property
    def equipos(self):
        return self._equipos   
    
    @property
    def campeonato(self):
         return self._campeonato
    
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

    def agregar_piloto(self,equipo, piloto):
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for equipo in self._equipos:
                if equipo.buscar_empleado(piloto.id) != None:
                    raise EmpleadoEnEquipo(411, f"Ese piloto ya forma parte de un equipo: {equipo.nombre}")
        #VERIFICAR QUE EQUIPO TENGA CAPACIDAD
        if piloto.es_titular:
            if not self.tiene_capacidad(equipo, 1):
                raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de pilotos titulares")
        elif not piloto.es_titular:
            if self.tiene_capacidad(equipo, 2) == False:
                raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de pilotos de reserva")
        equipo.agregar_empleado(piloto)
        piloto.equipo = equipo
       
    def agregar_mecanico(self, equipo, mecanico):
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for equipo in self._equipos:
                if equipo.buscar_empleado(mecanico.id) != None:
                    raise EmpleadoEnEquipo(411, f"Ese mecánico ya forma parte de un equipo: {equipo.nombre}")
        equipo.agregar_empleado(mecanico)
        mecanico.equipo = equipo
       
    def agregar_director(self,equipo, director):   
        #VERIFICAR QUE EMPLEADO NO PERTENEZCA A UN EQUIPO
        for equipo in self._equipos:
                if equipo.buscar_empleado(director.id) != None:
                    raise EmpleadoEnEquipo(411, f"Ese director ya forma parte de un equipo: {equipo.nombre}")       
        #VERIFICAR CAPACIDAD
        if not self.tiene_capacidad(equipo, 3):
             raise EquipoSinCapacidad(422, "El equipo ha alcanzado el número máximo de directores")
        equipo.agregar_empleado(director)
        director.equipo = equipo

    def tiene_capacidad(self, equipo, tipo_empleado):
        self.buscar_equipo(equipo) #Para verificar existencia
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
                    es_titular = piloto.es_titular
                    if not es_titular:
                        return False
                return True
            case 3:
                for empleado in equipo._empleados:
                    if equipo.es_director(empleado.id):
                        return False
                return True
           