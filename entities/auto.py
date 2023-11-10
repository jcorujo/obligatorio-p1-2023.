class Auto:
    def __init__(self, modelo,score):
        self._modelo = modelo
        self._score = score
        self._equipo = None
    
    @property
    def modelo(self):
        return self._modelo
    @property
    def score(self):
        return self._score
    @property
    def equipo(self):
        return self._equipo
    
    @score.setter
    def score(self, nuevo_score):
        self._score = nuevo_score
    


