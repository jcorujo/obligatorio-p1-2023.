class Equipo:
    def __init__(self, nombre, pais, creacion):
        self._nombre = nombre
        self._pais = pais
        self._creacion = creacion
    @property
    def nombre(self) -> str:
        return self._nombre 
    @property
    def pais(self) -> str:
        return self._pais
    #FECHAS
    @property
    def creacion(self) -> int:
        return self._creacion