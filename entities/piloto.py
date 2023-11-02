class Piloto:
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, nro_auto):
        super().__init___(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self._nro_auto = nro_auto 
        self._esta_lesionado = False
        self._score = 0
        self._puntaje_campeonato = 0
        
    @property
    def nro_auto(self) -> int:
        return self._nro_auto
    @property
    def score(self) -> int:
        return self._score
    @property
    def esta_lesionado(self) -> bool:
        return self._esta_lesionado
    @property
    def puntaje_campeonato(self) -> int:
        return self._puntaje_campeonato

    @nro_auto.setter
    def nro_auto(self, nro_nuevo):
        self._nro_auto = nro_nuevo
    @esta_lesionado.setter
    def esta_lesionado(self, estado):
        self._esta_lesionado = estado
        

       