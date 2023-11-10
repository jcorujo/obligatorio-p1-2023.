from exceptions.EquipoNoExiste import EquipoNoExiste
from entities.equipo import Equipo


class Gestor_Equipos:
    def __init__(self, equipos:list):
        #¿cuales son los argumentos, los nombres de los equipos o los nombres de las instancias?
        self._equipos = equipos
    
    @property
    def equipos(self):
        return self._equipos
    
    def buscar_equipo(self, equipo):
        equipo_encontrado = None
        for equipo in self._equipos:
            if (equipo.nombre() == equipo) or (isinstance(equipo, Equipo)):
                equipo_encontrado = equipo
        if equipo == None:
            raise EquipoNoExiste(415, "El equipo ingresado no existe")
        return equipo_encontrado
     
    def agregar_equipo(self, equipo):
        #Verificar que equipo no exista
        pass
    
    def agregar_piloto(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario, nro_auto):
        equipo = Gestor_Equipos.buscar_equipo(equipo)
              
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
    
Equipo1 = Equipo("Equipo1", "Uruguay", 1990, 80, "Ferrari122" )
Gestor = Gestor_Equipos([Equipo1])
print(Gestor.equipos)
Gestor.agregar_piloto("Equipo2")