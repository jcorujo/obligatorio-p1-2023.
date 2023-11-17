class Campeonato:
    def __init__(self, equipos_participantes: list):
        self._participantes = equipos_participantes

    @property
    def participantes(self):
        return self._participantes
    
    def pilotos_con_mas_puntos(self):
        for equipo in self._participantes:
            pilotos = equipo.obtener_pilotos()
            for piloto in pilotos:
                orden_puntaje = sorted(self.participantes, key=lambda x: x.puntaje_carrera, reverse=True)
                pass

    
    def resumen_puntos(self):
        pass
    
    def pilotos_mayor_salario(self):
        pass
    
    def jefes_de_equipo(self):
        pass