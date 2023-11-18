from entities.gestion import Gestion
from entities.piloto import Piloto

def top_10_pilotos(gestion1:Gestion):
    top_10_pilotos_puntaje=[]
    for equipos in gestion1._equipos:
            for piloto in range(len(equipos._empleados)):
                if isinstance(piloto,Piloto):
                    top_10_pilotos_puntaje.append(piloto)
                    lambda x: x.puntaje_campeonato
                    top_10_pilotos_puntaje=sorted(top_10_pilotos_puntaje,key=lambda x: x.puntaje_campeonato,reverse=True)
            
    return top_10_pilotos_puntaje[:10]