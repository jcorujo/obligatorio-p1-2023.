from exceptions.EquipoNoExiste import EquipoNoExiste
from entities.equipo import Equipo
from datetime import datetime


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
    
    def agregar_piloto(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario, nro_auto):
        equipo = Gestor_Equipos.buscar_equipo(self, equipo)
              
              #VERIFICAR EXISTENCIA EQUIPO
              #VERIFICAR CAPACIDAD EQUIPO
              #VERIFICAR QUE NO EXISTA PILOTO CON MISMO ID, EN EL EQUIPO U OTROS EQUIPOS
              #CREAR PILOTO
        pass
      
    def cambiar_nombre(self, equipo, nuevo_nombre):
        pass
   

    def habilitados_para_correr(self):
        for equipo in self._equipos:
            empleados = equipo.empleados
            
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