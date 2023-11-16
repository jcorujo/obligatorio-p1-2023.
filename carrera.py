from campeonato import Campeonato
from entities.piloto import Piloto
from entities.equipo import Equipo
from exceptions.ArgumentoInvalido import ArgumentoInvalido
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste
from exceptions.EquipoNoExiste import EquipoNoExiste
from gestor_equipos import Gestor_Equipos
import random

class Carrera():
    def __init__(self, equipos_participantes):
        self._equipos_participantes = []
        for equipo in equipos_participantes:
            if Gestor_Equipos(equipos_participantes).puede_participar(equipo):
                self._equipos_participantes.append(equipo)
        self._pilotos = []
        for equipo in self._equipos_participantes:
            for piloto in equipo.habilitados_para_correr():
                self._pilotos.append(piloto)
        self._abandonaron = []
        self._posiciones = {}

    @property
    def equipos_participantes(self):
        return self._equipos_participantes
    @property 
    def pilotos(self):
        return self._pilotos
    @property
    def posiciones(self):
        return self._posiciones
    @property
    def abandonaron(self):
        return self._abandonaron
    
    def buscar_piloto(self, nro_auto):
        if not isinstance(nro_auto, int):
            raise ArgumentoInvalido(420, "El argumento ingresado es inválido")
        piloto_encontrado = None
        for piloto in self.pilotos:
            if piloto.nro_auto == nro_auto:
                 piloto_encontrado = piloto
        if piloto_encontrado == None:
            raise EmpleadoNoExiste(410, "El empleado ingresado no forma parte de esta carrera")  
        return piloto_encontrado
    
    def registrar_imprevisto(self, nro_auto, tipo_imprevisto:int):
        piloto = self.buscar_piloto(nro_auto)                
        if tipo_imprevisto == 0:
            piloto.esta_lesionado == True
            self.pilotos.remove(piloto)
        elif tipo_imprevisto == 1:
            self.abandonaron.append(piloto)               
        elif tipo_imprevisto == 2:
            piloto._puntaje_carrera -= 5
        elif tipo_imprevisto == 3:
            piloto._puntaje_carrera -= 8
        else:
            raise ArgumentoInvalido(420, "El tipo de imprevisto ingresado es incorrecto: \n- Para indicar el abandono del piloto ingrese '0' \n- Para indicar un error en pits ingrese '1' \n- Para indicar una penalidad por infrigir una norma ingrese '2'")
    
    def obtener_plantel(self, piloto):
        plantel = []
        piloto = self.buscar_piloto(piloto.nro_auto)
        plantel.append(piloto)
        equipo = piloto.equipo
        mecanicos = equipo.obtener_mecanicos()
        for mecanico in mecanicos:
            plantel.append(mecanico)
        return plantel
    
    def adjudicar_puntaje(self):
        #aÑadir excepcion para piloto que abandono
        for piloto in self._pilotos:
            equipo = self.obtener_plantel(piloto)#funciona
            piloto.puntaje_carrera = 0 #funciona

            for participante in equipo:
                    piloto.agregar_puntaje_carrera(participante.score)#funciona
            
            if piloto.puntaje_carrera < 0:
                piloto.puntaje_carrera = 0 #que mierda pasa aca!!
            
            if piloto in self.abandonaron:
                piloto.puntaje_carrera = 0
    
    def resetear_atributos(self):
        for piloto in self._pilotos:
            piloto.puntaje_carrera = 0
            piloto.esta_lesionado = False
        
    def determinar_posiciones(self):
        #correr adjudicar puntaje
        self.adjudicar_puntaje()
        orden_puntaje = sorted(self._pilotos, key=lambda x: x.puntaje_carrera, reverse=True)
        for posicion, piloto in enumerate(orden_puntaje):
            if posicion < 10:
                if posicion == 0:
                    piloto._puntaje_campeonato += 25
                elif posicion == 1:
                    piloto._puntaje_campeonato += 18
                elif posicion == 2:
                    piloto._puntaje_campeonato += 15
                elif posicion == 3:
                    piloto._puntaje_campeonato += 12
                elif posicion == 4:
                    piloto._puntaje_campeonato += 10
                elif posicion == 5:
                    piloto._puntaje_campeonato += 8
                elif posicion == 6:
                    piloto._puntaje_campeonato += 6
                elif posicion == 7:
                    piloto._puntaje_campeonato += 4
                elif posicion == 8:
                    piloto._puntaje_campeonato += 2
                elif posicion == 9:
                    piloto._puntaje_campeonato += 1  
            self._posiciones[posicion + 1] = piloto
        self.resetear_atributos()                   
    #posicion carrera por piloto en el dictionary

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
print(ferrari.empleados)
print(gestor.puede_participar(ferrari)) #ESTO DEBERIA DAR TRUE
print(gestor.tiene_capacidad(ferrari, 1)) #ESTO DEBERIA DAR FALSE
print(gestor.tiene_capacidad(ferrari, 3))  #ESTO DEBERIA DAR FALSE
carrera1 = Carrera([ferrari, mercedes, red_bull])
print(carrera1.equipos_participantes)
print(len(ferrari.empleados))
for piloto in ferrari.obtener_pilotos():
    print(piloto.es_titular)
gestor.agregar_piloto(ferrari, "Antonio Giovinazzi", 55555, "19/01/1997", "italia", 500, 112, 70, False)
for piloto in ferrari.obtener_pilotos():
    print(piloto.es_titular)
print("Ferrari tiene capacidad de reserva:", gestor.tiene_capacidad(ferrari, 2))  #ESTO DEBERIA DAR FALSE
p = carrera1.buscar_piloto(332)
print("Los pilotos en la carrera son:", [piloto.nombre for piloto in carrera1.pilotos])
carrera1.registrar_imprevisto(332, 2)
print(p.puntaje_carrera)
carrera1.adjudicar_puntaje()
print(carrera1.posiciones)
print(p.puntaje_campeonato)
print("El score del plantel ferrari es:", [empleado.score for empleado in carrera1.obtener_plantel(p)])