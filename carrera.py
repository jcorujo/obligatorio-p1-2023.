from campeonato import Campeonato
from entities.equipo import Equipo
from exceptions.ArgumentoInvalido import ArgumentoInvalido
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste
from exceptions.EquipoNoExiste import EquipoNoExiste
from gestor_equipos import Gestor_Equipos
from gestor_personal import Gestor_Personal
import random

class Carrera():
    def __init__(self, equipos_participantes):
        self._equipos_participantes = []
        for equipo in equipos_participantes:
            if Gestor_Equipos(equipos_participantes).puede_participar(equipo):
                self._equipos_participantes.append(equipo)
        self._posiciones = []

    @property
    def equipos_participantes(self):
        return self._equipos_participantes

    def registrar_imprevisto(self, id_piloto, tipo_imprevisto:int):
        for equipo in self._equipos_participantes:
            personal = Gestor_Personal(equipo)
            if personal.buscar_empleado(id_piloto) 
        if tipo_imprevisto == 0:
            pass
        if tipo_imprevisto == 1:
            pass
        if tipo_imprevisto == 2:
            pass
        else:
            raise ArgumentoInvalido(420, "El tipo de imprevisto ingresado es incorrecto: \n- Para indicar el abandono del piloto ingrese '0' \n- Para indicar un error en pits ingrese '1' \n- Para indicar una penalidad por infrigir una norma ingrese '2'")
    
    def determinar_posiciones(self):
        pass
    def adjudicar_puntos(self):
        pass

ferrari = Equipo("Ferrari", "Italia", '01-01-1950', "SF-23")
mercedes = Equipo("Mercedes", "Alemania", '01-01-1970', "W14")
red_bull = Equipo("Red Bull", "Austria", "01-01-1997", "RB14" )
gestor = Gestor_Equipos([ferrari, mercedes, red_bull])
gestor.agregar_director(ferrari, "Enrico Cardile", 1234, "19-04-1970", "italia", 5000 )
gestor.agregar_piloto(ferrari, "Charles Leclerc", 1235, "16-10-1997", "monaco", 10000, 332, 80, True )
gestor.agregar_piloto(ferrari, "Carlos Sainz", 1236, "01-09-1994", "españa", 10000, 331, 85, True )
gestor.agregar_mecanico(ferrari, "Mec1", 1237, "X", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec2", 1238, "X", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec3", 1211, "X", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec4", 12125, "X", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec5", 123777, "X", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec6", 12371231, "X", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec7", 123711, "X", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec8", 1237123, "X", "italia", 1000, random.randint(50, 100))
gestor.agregar_director(ferrari, "Enrico Cardile", 1234, "19-04-1970", "italia", 5000 )
print(ferrari.empleados)
print(gestor.puede_participar(ferrari)) #ESTO DEBERIA DAR TRUE
print(gestor.tiene_capacidad(ferrari, 1)) #ESTO DEBERIA DAR FALSE
print(gestor.tiene_capacidad(ferrari, 3))  #ESTO DEBERIA DAR FALSE
gestor.agregar_piloto(ferrari, "Carlos Sainz", 1236, "01-09-1994", "españa", 10000, 331, 85, True )
carrera1 = Carrera([ferrari, mercedes, red_bull])
print(carrera1.equipos_participantes)
personal = Gestor_Personal(ferrari)
print(personal.obtener_pilotos())#SI SE RECONOCEN LOS PILOTOS POR LO QUE ESTA MAL EL METODO TIENE_CAPACIDAD
