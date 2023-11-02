class Mecanico:
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init___(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self._score = 0
    
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, new_score):
        self._score = new_score