class Carrera:
    def __init__(self, equipos_participantes: list):
        self._equipos_participantes = equipos_participantes
        self._empleados_participantes = []
    
    @property
    def equipos_participantes(self):
        return self._equipos_participantes
    @property
    def empleados_participantes(self):
        return self._empleados_participantes