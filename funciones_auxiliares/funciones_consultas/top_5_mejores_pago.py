import sys
sys.path.append('..')
from gestion import Gestion
from entities.piloto import Piloto

def top_5_mejores_pago(gestion1:Gestion):
    pilotos_mejor_pago=[]
    for equipos in gestion1.equipos:
            for piloto in equipos.empleados:
                if isinstance(piloto,Piloto):
                    pilotos_mejor_pago.append(piloto)
                    pilotos_mejor_pago=sorted(pilotos_mejor_pago,key=lambda x: x.salario,reverse=True)
            
    return pilotos_mejor_pago[:5]