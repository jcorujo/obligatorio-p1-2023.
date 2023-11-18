import sys
from entities.carrera import Carrera
from entities.campeonato import Campeonato
from gestion import Gestion
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.auto import Auto
from entities.director import Director
from entities.equipo import Equipo
from funciones_menu.alta_empleado import alta_empleado
from funciones_menu.alta_auto import alta_de_auto
from funciones_menu.alta_equipo import alta_de_equipo
from funciones_menu.realizar_consultas import realizar_consultas
from funciones_menu.simular_carrera import simular_carrera
from exceptions.Argumento_fuera_de_rango import ArgumentoFueraDeRango
from exceptions.Argumento_vacio import ArgumentoVacio

def menu(gestion:Gestion):
    gestion0=gestion
    menu_principal = 0
    while menu_principal !=6:
        # Opciones menu
        while (menu_principal>6) or (menu_principal<1):
            try:   
                menu_principal = int(input("\nIngrese una opción:\n 1.Alta de empleado \n 2.Alta de auto \n 3.Alta de equipo \n 4.Simular carrera \n 5.Realizar consultas \n 6.Finalizar programa\n"))
            except ValueError: 
                print("Valor incorrecto.\nIntentelo de nuevo\n")
                break

            if (menu_principal>6) or (menu_principal<1):
                try:
                    raise ArgumentoFueraDeRango(400,"Valor fuera de rango esperado\n Intentelo nuevamente\n")
                
                except ArgumentoFueraDeRango as e:
                    print(e)
            elif (menu_principal==None):
                try:
                    raise ArgumentoVacio(410,"El argumento ingresado es vacio\n Intentalo nuevamente\n")
                except ArgumentoVacio as e:
                    print(e)
            
        
            else:
                if menu_principal == 1:
                    empleado=alta_empleado(gestion0)
                    if empleado != None and empleado!=[]:
                        gestion0.empleados.append(empleado[0])
                        print("Se ha agregado un empleado de forma exitosa")
                        menu_principal = 0
                    else:
                        print("No se ha podido agregar al empleado")
                        menu_principal=0
                    
                if menu_principal == 2:
                    auto=alta_de_auto(gestion0)
                    if auto !=None and auto != []:
                        gestion0.autos.append(auto[0])
                        print("Se ha agregado el automovil de forma exitosa")
                        menu_principal=0
                        
                    else:
                        
                        print("No se ha podido agregar el auto")
                        menu_principal=0
                    
                if menu_principal == 3:
                    equipo=alta_de_equipo(gestion0)
                    if equipo!=[] and equipo!=None:
                        gestion0.equipos.append(equipo[0])
                        print("Se ha agregado el equipo de forma existosa")
                        menu_principal=0
                    
                    else:
                        print("No se ha podido agregar el equipo")
                        menu_principal=0
                    
                    
                if menu_principal == 4:
                    print("")
                    carrera=simular_carrera(gestion0)
                    menu_principal = 0
                if menu_principal == 5:
                    consultas=realizar_consultas(gestion0)
                    print(consultas)
                    menu_principal=0
                    
                if menu_principal == 6:
                    sys.exit(0)
                    
    menu_principal=0

if __name__=="__main__":
    gestion=Gestion()
    menu_de_inicio=menu(gestion)
    
  
    