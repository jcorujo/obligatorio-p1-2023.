class Auto:
    def __init__(self, modelo, anio, score):
        self._modelo = modelo
        self._anio = anio
        self._score = score
        self._equipo = None
    
    @property
    def modelo(self):
        return self._modelo
    @property
    def anio(self):
        return self._anio
    @property
    def score(self):
        return self._score
    @property
    def equipo(self):
        return self._equipo


    def __eq__(self, otro_auto):
        return self._modelo == otro_auto.modelo