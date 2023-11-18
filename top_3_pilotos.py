import sys
sys.path.append('..')
from gestion import Gestion
from entities.piloto import Piloto

def top_3_pilotos(gestion1:Gestion):
    pilotos_habilidosos= []
    posiciones = {}
    for equipo in gestion1._equipos:
            for piloto in equipo.obtener_pilotos():
                if isinstance(piloto,Piloto):
                    pilotos_habilidosos.append(piloto)
                    lambda x: x._score
                    pilotos_habilidosos=sorted(pilotos_habilidosos,key=lambda x: x._score,reverse=True)
            for posicion, piloto in enumerate(pilotos_habilidosos):
                 if posicion < 2:
                      posiciones[posicion + 1] = piloto
                 
    for posicion, piloto in posiciones.items():
            print (f"{posicion} - {piloto.nombre}")