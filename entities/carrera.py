from entities.campeonato import Campeonato
from entities.equipo import Equipo
from entities.piloto import Piloto
from exceptions.Argumento_Invalido import ArgumentoInvalido
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste
from exceptions.EquipoNoExiste import EquipoNoExiste

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
            piloto.esta_lesionado = True
            self.pilotos.remove(piloto)
            equipo = piloto.equipo
            for piloto in equipo.habilitados_para_correr():
                if piloto not in self.pilotos:
                    self.pilotos.append(piloto)
            if len(equipo.habilitados_para_correr()) == 0:
                self.equipos_participantes.remove(equipo)
            
        elif tipo_imprevisto == 1:
            self.abandonaron.append(piloto)
            self.pilotos.remove(piloto)               
        
        elif tipo_imprevisto == 2:
            piloto.puntaje_carrera -= 5
        
        elif tipo_imprevisto == 3:
            piloto.puntaje_carrera -= 8
        
        else:
            raise ArgumentoInvalido(420, "El tipo de imprevisto ingresado es incorrecto: \n Para indicar que el piloto se encuentra lesionado ingrese '0' \n- Para indicar el abandono del piloto ingrese '1' \n- Para indicar un error en pits ingrese '2' \n- Para indicar una penalidad por infrigir una norma ingrese '3'")
    
    def obtener_plantel(self, piloto):
        plantel = []
        piloto = self.buscar_piloto(piloto.nro_auto)
        plantel.append(piloto)
        equipo = piloto.equipo
        mecanicos = equipo.obtener_mecanicos()
        for mecanico in mecanicos:
            plantel.append(mecanico)
        plantel.append(equipo.auto)
        
        return plantel
    
    def adjudicar_puntaje(self):
        for piloto in self._pilotos:
            plantel = self.obtener_plantel(piloto)
             
            for integrante in plantel: 
                piloto.agregar_puntaje_carrera(integrante.score)
            
            if piloto in self.abandonaron:
                piloto.puntaje_carrera = 0
            
            if piloto.puntaje_carrera < 0:
                piloto.puntaje_carrera = 0
    
    def resetear_atributos(self):
        for equipo in self._equipos_participantes:
            for piloto in equipo.obtener_pilotos():
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
            print (f"{posicion} - {valor[0].nombre}: {valor[1]} puntos")

