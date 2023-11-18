import sys
from entities.piloto import Piloto
sys.path.append('..')
from gestion import Gestion
from funciones_auxiliares.funciones_consultas.top_5_mejores_pago import top_5_mejores_pago
from funciones_auxiliares.funciones_consultas.top_3_pilotos import top_3_pilotos
from funciones_auxiliares.funciones_consultas.retornar_jefes import retornar_jefes

def realizar_consultas(gestion:Gestion):
    gestion1=gestion
    
    while True:
        menu_consultas=int(input("\nIngresé el tipo de consulta:\n 1.Top 10 pilotos con mas puntos en el campeonato\n 2.Resumen campeonato de constructores(equipo)\n 3.Top 5 pilotos mejores pago\n 4.Top 3 pilotos mas habilidosos\n 5.Retornar jefes de equipo \n 6.Volver al menu principal \n"))
        if menu_consultas == 1:
            print ("Top 10 pilotos - Campeonato: ")
            gestion1.campeonato.pilotos_con_mas_puntos()
        
        elif menu_consultas == 2:
            gestion1.campeonato.determinar_posiciones()
            gestion1.campeonato.resumen_campeonato()
                 
        elif menu_consultas == 3:
            top_5_pilotos_mejor_pago = top_5_mejores_pago(gestion1)
            print("")
            print("Top 5 pilotos mejor pago:")
            for piloto in range(len(top_5_pilotos_mejor_pago)):
                print(f"{piloto+1}. {top_5_pilotos_mejor_pago[piloto].nombre}")
            break
            
        
        elif menu_consultas == 4:
            print("Top 3 pilotos mas habilidosos:")
            top_3_pilotos(gestion1) 
                
        elif menu_consultas == 5:
            jefes_de_equipo=retornar_jefes(gestion1)
            print("Lista de Jefes de Equipo: ")
            for jefes in range(len(jefes_de_equipo)):
                print(f"{jefes+1}. {jefes_de_equipo[jefes]}")
            break
        
        elif menu_consultas == 6:
            break
        break
        