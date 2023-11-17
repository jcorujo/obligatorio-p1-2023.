class Campeonato:
    def __init__(self, equipos_participantes: list):
        self._participantes = equipos_participantes
        self._posiciones = {}

    @property
    def participantes(self):
        return self._participantes
    
    def pilotos_con_mas_puntos(self):
        pilotos = []
        for equipo in self._participantes:
            pilotos_equipo = equipo.obtener_pilotos()
            for piloto in pilotos_equipo:
                pilotos.append(piloto)
        orden_puntaje = sorted(pilotos, key=lambda x: x.puntaje_campeonato, reverse=True)
        for posicion, piloto in enumerate(orden_puntaje):
            if posicion < 10:
                print (f"{posicion} - {piloto.nombre}")
    
    def determinar_posiciones(self):
        orden_puntaje = sorted(self._participantes, key=lambda x: x.puntaje_campeonato, reverse = True)
        for posicion , equipo in enumerate(orden_puntaje):
            print (f"{posicion} - {equipo.nombre}: {equipo.puntaje_campeonato}")
    
    def terminar_campeonato(self):
        for equipo in self._participantes:
            equipo.puntaje_campeonato = 0
            pilotos_equipo = equipo.obtener_pilotos()
            for piloto in pilotos_equipo:
                piloto.puntaje_campeonato = 0

        
    
