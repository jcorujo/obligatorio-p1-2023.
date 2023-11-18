from entities.equipo import Equipo
from exceptions.Argumento_Invalido import ArgumentoInvalido

class Campeonato:
    def __init__(self, equipos_participantes: list):
        self._participantes = equipos_participantes
        self._posiciones = {}

    @property
    def participantes(self):
        return self._participantes
    @property
    def posiciones(self):
        return self._posiciones
    
    def agregar_equipo(self, equipo):
        self._participantes.append(equipo)
        
    def explusar_equipo(self, nombre):
        equipo_a_eliminar = None
        for equipo in self.participantes:
            if equipo.nombre == nombre:
                equipo_a_eliminar = equipo
                self.participantes.remove(equipo)
        if equipo_a_eliminar == None:
            raise ArgumentoInvalido(420, 'El equipo ingresado es invalido')
        
    def pilotos_con_mas_puntos(self):
        pilotos = []
        for equipo in self._participantes:
            pilotos_equipo = equipo.obtener_pilotos()
            for piloto in pilotos_equipo:
                pilotos.append(piloto)
        orden_puntaje = sorted(pilotos, key=lambda x: x.puntaje_campeonato, reverse=True)
        for posicion, piloto in enumerate(orden_puntaje):
            if posicion < 10:
                print (f"{posicion + 1} - {piloto.nombre}: {piloto.puntaje_campeonato}")
    
    def determinar_posiciones(self):
        orden_puntaje = sorted(self._participantes, key=lambda x: x.puntaje_campeonato, reverse = True)
        for posicion , equipo in enumerate(orden_puntaje):
            self._posiciones[posicion + 1] = [equipo, equipo.puntaje_campeonato]
    
    def resumen_campeonato(self):
            print("Resumen del campeonato: \n")
            for posicion, valor in self.posiciones.items():
                print (f"{posicion} - {valor[0].nombre}: {valor[1]}")
    
    def terminar_campeonato(self):
        #Para que se guarde la ultima informacion relativa al resultado del campeonato en el self._posicioens antes de resetear las estadisticas:
        self.determinar_posiciones()
        for equipo in self._participantes:
            equipo.puntaje_campeonato = 0
            pilotos_equipo = equipo.obtener_pilotos()
            for piloto in pilotos_equipo:
                piloto.puntaje_campeonato = 0