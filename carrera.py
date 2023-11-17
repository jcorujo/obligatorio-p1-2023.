from campeonato import Campeonato
from entities.equipo import Equipo
from entities.piloto import Piloto
from exceptions.ArgumentoInvalido import ArgumentoInvalido
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste
from exceptions.EquipoNoExiste import EquipoNoExiste
from gestor_equipos import Gestor_Equipos
import random

class Carrera():
    def __init__(self, campeonato):
        self._equipos_participantes = []
        for equipo in campeonato.participantes:
            if equipo.puede_participar():
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
    
    def explusar_piloto(self, piloto):
        if (isinstance(piloto, Piloto) and piloto in self.pilotos):
            self._pilotos.remove(piloto)
        else:
            raise ArgumentoInvalido(420, 'El piloto ingresado es invalido')

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
        for piloto in self._pilotos:
            equipo = self.obtener_plantel(piloto)
            piloto.puntaje_carrera = 0 

            for participante in equipo: 
                piloto.agregar_puntaje_carrera(participante.score)
            
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
            equipo = piloto.equipo
            if posicion == 0:
                piloto.agregar_puntaje_campeonato(25)
                equipo.agregar_puntaje_campeonato(25)
            elif posicion == 1:
                piloto.agregar_puntaje_campeonato(18)
                equipo.agregar_puntaje_campeonato(18)
            elif posicion == 2:
                piloto.agregar_puntaje_campeonato(15)
                equipo.agregar_puntaje_campeonato(15)
            elif posicion == 3:
                piloto.agregar_puntaje_campeonato(12)
                equipo.agregar_puntaje_campeonato(12)
            elif posicion == 4:
                piloto.agregar_puntaje_campeonato(10)
                equipo.agregar_puntaje_campeonato(10)
            elif posicion == 5:
                piloto.agregar_puntaje_campeonato(8)
                equipo.agregar_puntaje_campeonato(8)
            elif posicion == 6:
                piloto.agregar_puntaje_campeonato(6)
                equipo.agregar_puntaje_campeonato(6)
            elif posicion == 7:
                piloto.agregar_puntaje_campeonato(4)
                equipo.agregar_puntaje_campeonato(4)
            elif posicion == 8:
                piloto.agregar_puntaje_campeonato(2)
                equipo.agregar_puntaje_campeonato(2)
            elif posicion == 9:
                piloto.agregar_puntaje_campeonato(1)
                equipo.agregar_puntaje_campeonato(1) 
            self._posiciones[posicion + 1] = [piloto, piloto.puntaje_carrera]
        self.resetear_atributos()                   
    
    def resumen_posiciones (self):
        print ("Las posiciones de la carrera son: \n")
        for posicion, valor in self.posiciones.items():
            print (f"{posicion} - {valor[0].nombre}: {valor[1]}")
            
ferrari = Equipo("Ferrari", "Italia", '01-01-1950', "SF-23")
mercedes = Equipo("Mercedes", "Alemania", '01-01-1970', "W14")
red_bull = Equipo("Red Bull", "Austria", "01-01-1997", "RB14" )
gestor = Gestor_Equipos([ferrari, mercedes, red_bull])
campeonato = Campeonato([ferrari, mercedes, red_bull])
gestor.agregar_director(ferrari, "Enrico Cardile", 1234, "19/04/1970", "italy", 5000 )
gestor.agregar_piloto(ferrari, "Charles Leclerc", 1235, "16/10/1997", "monaco", 10000, 332, 80, True )
gestor.agregar_piloto(ferrari, "Carlos Sainz", 1236, "01/09/1994", "Spain", 10000, 331, 85, True )
gestor.agregar_mecanico(ferrari, "Mec1", 1237, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec2", 1238, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec3", 1211, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec4", 12125, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec5", 123777, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec6", 12371231, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec7", 123711, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(ferrari, "Mec8", 1237123, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_director(red_bull, "Christian Horner", 11111, "29/12/1970", "United Kingdom", 6000)
gestor.agregar_piloto(red_bull, "Max Verstappen", 22222, "30/09/1997", "Netherlands", 10000, 500, 95, True )
gestor.agregar_piloto(red_bull, "Sergio Perez", 123511, "16/10/1997", "Spain", 10000, 338, 85, True )
gestor.agregar_mecanico(red_bull, "Mec1", 1237123, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(red_bull, "Mec1", 1237111, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(red_bull, "Mec1", 1237444, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(red_bull, "Mec1", 1237555, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(red_bull, "Mec1", 1237666, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(red_bull, "Mec1", 1237777, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(red_bull, "Mec1", 1237888, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_mecanico(red_bull, "Mec1", 1237999, "01/09/1994", "italia", 1000, random.randint(50, 100))
gestor.agregar_piloto(ferrari, "Antonio Giovinazzi", 51341412, "01/01/2000", "Italia", 1000, 600, 78, False )
print("Los empleados de ferrari son:", ferrari.empleados)
print("ferrari puede participar:", ferrari.puede_participar()) #ESTO DEBERIA DAR TRUE
print("ferrari tiene capacidad titulares:" , gestor.tiene_capacidad(ferrari, 1)) #ESTO DEBERIA DAR FALSE
print("ferrari tiene capacidad director:" , gestor.tiene_capacidad(ferrari, 3))  #ESTO DEBERIA DAR FALSE
carrera1 = Carrera(campeonato)
print("Red Bull puede participar:", red_bull.puede_participar())
print("Los equipos participantes son", carrera1.equipos_participantes)
for piloto in carrera1.pilotos:
    print(piloto.nombre)
print(len(ferrari.empleados))
for piloto in ferrari.obtener_pilotos():
    print(piloto.es_titular)
print("Ferrari tiene capacidad de reserva:", gestor.tiene_capacidad(ferrari, 2))  #ESTO DEBERIA DAR FALSE
lecrerc = carrera1.buscar_piloto(332)
sainz = carrera1.buscar_piloto(331)
print("Los pilotos en la carrera son:", [piloto.nombre for piloto in carrera1.pilotos])
carrera1.registrar_imprevisto(338, 1)
carrera1.registrar_imprevisto(332, 2)
carrera1.registrar_imprevisto(500, 2)
carrera1.registrar_imprevisto(331, 3)
print("El score del plantel ferrari con lecrerc es:", [empleado.score for empleado in carrera1.obtener_plantel(lecrerc)])
carrera1.adjudicar_puntaje()
print("abandonaron", carrera1.abandonaron)
print("puntaje de sainz", sainz.puntaje_carrera)
carrera1.determinar_posiciones()
print("puntaje de sainz dps de determinar posiciones", sainz.puntaje_carrera)
print("puntaje ferrari:", ferrari.puntaje_campeonato)
print("Las posiciones de las carreras son:", carrera1.posiciones)
print("el puntaje de campeonato del piloto es:", lecrerc.puntaje_campeonato)
carrera1.resumen_posiciones()