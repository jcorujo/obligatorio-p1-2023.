class Auto:
    def __init__(self, modelo, color, score):
        self._modelo = modelo
        self._color = color
        self._score = score
        self._equipo = ''
    
    @property
    def modelo(self):
        return self._modelo
    @property
    def color(self):
        return self._color
    @property
    def score(self):
        return self._score
    @property
    def equipo(self):
        return self._equipo
    
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color
    @score.setter
    def score(self, nuevo_score):
        self._score = nuevo_score


