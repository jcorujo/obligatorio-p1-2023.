from campeonato import Campeonato
from gestor_equipos import Gestor_Equipos
from gestor_personal import Gestor_Personal
from entities.equipo import Equipo
from exceptions.ArgumentoInvalido import ArgumentoInvalido

class Carrera(Campeonato):
    def __init__(self):
        self._equipos_participantes = [Gestor_Equipos.habilitados_para_correr in Campeonato._participantes]
        #checkear que equipos puedan participar, if not raise exc
        self._pilotos_participantes = []
        self._posiciones = []

    
    @property
    def equipos_participantes(self):
        return self._equipos_participantes
    
    def buscar_piloto
    
    def imprevisto(self, id_piloto, tipo_imprevisto:int):

        if tipo_imprevisto == 0:
            pass
        if tipo_imprevisto == 1:
            pass
        if tipo_imprevisto == 2:
            pass
        else:
            raise ArgumentoInvalido(420, "El tipo de imprevisto ingresado es incorrecto: \n- Para indicar el abandono del piloto ingrese '0' \n- Para indicar un error en pits ingrese '1' \n- Para indicar una penalidad por infrigir una norma ingrese '2'")
    def determinar_posiciones(self):
        pass
    def adjudicar_puntos(self):
        pass

equipo1 = Equipo("Equipo1", "Uruguay", '16-05-1990', 20)
Campeonato1 = Campeonato([equipo1])
Carrera1 = Carrera()
Carrera1.imprevisto(self, piloto)
