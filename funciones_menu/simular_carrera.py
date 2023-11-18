import sys
from entities.carrera import Carrera
from entities.campeonato import Campeonato
from exceptions.Argumento_fuera_de_rango import ArgumentoFueraDeRango
from exceptions.Argumento_vacio import ArgumentoVacio

def simular_carrera(gestion):
    equipos=gestion._equipos
    campeonato = Campeonato(equipos)
    carrera = Carrera(campeonato)
    simulando = True
    while simulando:
        menu_simular_carrera=0
        while menu_simular_carrera != 6:
            while (menu_simular_carrera>6) or (menu_simular_carrera<1):
                try:    
                    menu_simular_carrera = int(input("\nIngrese una opción:\n 1. Ingresar numero de auto de pilotos lesionados \n 2. Ingresar numero de auto de todos los pilotos que abandonan la carrera \n 3. Ingresar numero de auto de todos los pilotos que cometen error en pits \n 4. Ingrese numero de auto de todos los pilotos que reciben penalidad \n 5. Simular Carrera \n 6. Volver al menu principal \n"))
                except ValueError: 
                    print("Valor incorrecto.\nIntentelo de nuevo\n")
                    break

                if (menu_simular_carrera>6) or (menu_simular_carrera<1):
                    try:
                        raise ArgumentoFueraDeRango(400,"Valor fuera de rango esperado\n Intentelo nuevamente\n")
                    
                    except ArgumentoFueraDeRango as e:
                        print(e)
                        return None
                    
                elif (menu_simular_carrera==None):
                    try:
                        raise ArgumentoVacio(410,"El argumento ingresado es vacio\n Intentalo nuevamente\n")
                    except ArgumentoVacio as e:
                        print(e)
                        return None
                    
                else:
                    if menu_simular_carrera==1:
                        while True:
                            try:
                                nro_auto = int(input("Ingrese el numero de auto del piloto: \n"))
                            except ValueError:
                                print("El argumento ingresado es de un tipo incorrecto")
                                break

                            if (nro_auto<=0):
                                try:
                                    raise ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera del rango esperado")
                                except ArgumentoFueraDeRango as e:
                                    print(e)
                                    sys.exit()
                            elif nro_auto=="":
                                try:
                                    raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                                except ArgumentoVacio as e:
                                    print(e)
                                    sys.exit()
                            else:
                                carrera.registrar_imprevisto(nro_auto, 0)
                                menu_numero_auto = 0
                                while menu_numero_auto !=2:
                                    while (menu_numero_auto>2) or (menu_numero_auto<1):    
                                        try:    
                                            menu_numero_auto = int(input("\nIngrese una opción:\n 1.Si desea seguir agregando numeros de auto de pilotos lesionados \n 2.No desea seguir agregando numeros de autos \n" ))
                            
                                        except ValueError: 
                                            print("Valor incorrecto.\nIntentelo de nuevo\n")
                                            menu_numero_auto = 0

                                        if (menu_numero_auto>2) or (menu_numero_auto<1):
                                            try:
                                                raise ArgumentoFueraDeRango(400,"Valor fuera de rango esperado\n Intentelo nuevamente\n")
                                            
                                            except ArgumentoFueraDeRango as e:
                                                print(e)
                                                return None

                                        elif (menu_numero_auto==None):
                                            try:
                                                raise ArgumentoVacio(410,"El argumento ingresado es vacio\n Intentalo nuevamente\n")
                                            except ArgumentoVacio as e:
                                                print(e)
                                                menu_numero_auto = 0
                                        elif menu_numero_auto == 1:
                                            
                                            try:
                                                nro_auto = int(input("Ingrese el numero de auto del piloto: \n"))
                                            except ValueError:
                                                print("El argumento ingresado es de un tipo incorrecto")
                                                break

                                            if (nro_auto <= 0):
                                                try:
                                                    raise ArgumentoFueraDeRango(420, "El argumento ingresado esta fuera del rango esperado")
                                                except ArgumentoFueraDeRango as e:
                                                    print(e)
                                                    sys.exit()
                                            elif nro_auto == "":
                                                try:
                                                    raise ArgumentoVacio(430, "El argumento ingresado es vacio")
                                                except ArgumentoVacio as e:
                                                    print(e)
                                                    sys.exit()
                                            else:
                                                carrera.registrar_imprevisto(nro_auto, 0)
                                                menu_numero_auto = 0
                                        elif menu_numero_auto == 2:
                                            menu_simular_carrera = 0
                                            break
                                break      
                                        
                                            
                    elif menu_simular_carrera==2:
                        while True:
                            try:
                                nro_auto = int(input("Ingrese el numero de auto del piloto: \n"))
                            except ValueError:
                                print("El argumento ingresado es de un tipo incorrecto")
                                break

                            if (nro_auto<=0):
                                try:
                                    raise ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera del rango esperado")
                                except ArgumentoFueraDeRango as e:
                                    print(e)
                                    sys.exit()
                            elif nro_auto=="":
                                try:
                                    raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                                except ArgumentoVacio as e:
                                    print(e)
                                    sys.exit()
                            else:
                                carrera.registrar_imprevisto(nro_auto, 1)
                                menu_numero_auto = 0
                                while menu_numero_auto !=2:
                                    while (menu_numero_auto>2) or (menu_numero_auto<1):    
                                        try:    
                                            menu_numero_auto = int(input("\nIngrese una opción:\n 1.Si desea seguir agregando numeros de auto de pilotos que abandonaron \n 2.No desea seguir agregando numeros de autos \n" ))
                            
                                        except ValueError: 
                                            print("Valor incorrecto.\nIntentelo de nuevo\n")
                                            menu_numero_auto = 0

                                        if (menu_numero_auto>2) or (menu_numero_auto<1):
                                            try:
                                                raise ArgumentoFueraDeRango(400,"Valor fuera de rango esperado\n Intentelo nuevamente\n")
                                            
                                            except ArgumentoFueraDeRango as e:
                                                print(e)
                                                return None

                                        elif (menu_numero_auto==None):
                                            try:
                                                raise ArgumentoVacio(410,"El argumento ingresado es vacio\n Intentalo nuevamente\n")
                                            except ArgumentoVacio as e:
                                                print(e)
                                                menu_numero_auto = 0
                                        elif menu_numero_auto == 1:
                                        
                                            try:
                                                nro_auto = int(input("Ingrese el numero de auto del piloto: \n"))
                                            except ValueError:
                                                print("El argumento ingresado es de un tipo incorrecto")
                                                break

                                            if (nro_auto <= 0):
                                                try:
                                                    raise ArgumentoFueraDeRango(420, "El argumento ingresado esta fuera del rango esperado")
                                                except ArgumentoFueraDeRango as e:
                                                    print(e)
                                                    sys.exit()
                                            elif nro_auto == "":
                                                try:
                                                    raise ArgumentoVacio(430, "El argumento ingresado es vacio")
                                                except ArgumentoVacio as e:
                                                    print(e)
                                                    sys.exit()
                                            else:
                                                carrera.registrar_imprevisto(nro_auto, 1)
                                                menu_numero_auto = 0
                                        elif menu_numero_auto == 2:
                                            menu_simular_carrera = 0
                                            break
                                break      
                    
                    elif menu_simular_carrera==3:
                        while True:
                            try:
                                nro_auto = int(input("Ingrese el numero de auto del piloto: \n"))
                            except ValueError:
                                print("El argumento ingresado es de un tipo incorrecto")
                                break

                            if (nro_auto<=0):
                                try:
                                    raise ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera del rango esperado")
                                except ArgumentoFueraDeRango as e:
                                    print(e)
                                    sys.exit()
                            elif nro_auto=="":
                                try:
                                    raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                                except ArgumentoVacio as e:
                                    print(e)
                                    sys.exit()
                            else:
                                carrera.registrar_imprevisto(nro_auto, 2)
                                menu_numero_auto = 0
                                while menu_numero_auto !=2:
                                    while (menu_numero_auto>2) or (menu_numero_auto<1):    
                                        try:    
                                            menu_numero_auto = int(input("\nIngrese una opción:\n 1.Si desea seguir agregando numeros de auto de pilotos que cometieron errores en pit \n 2.No desea seguir agregando numeros de autos \n" ))
                            
                                        except ValueError: 
                                            print("Valor incorrecto.\nIntentelo de nuevo\n")
                                            menu_numero_auto = 0

                                        if (menu_numero_auto>2) or (menu_numero_auto<1):
                                            try:
                                                raise ArgumentoFueraDeRango(400,"Valor fuera de rango esperado\n Intentelo nuevamente\n")
                                            
                                            except ArgumentoFueraDeRango as e:
                                                print(e)
                                                return None

                                        elif (menu_numero_auto==None):
                                            try:
                                                raise ArgumentoVacio(410,"El argumento ingresado es vacio\n Intentalo nuevamente\n")
                                            except ArgumentoVacio as e:
                                                print(e)
                                                menu_numero_auto = 0
                                        elif menu_numero_auto == 1:
                                        
                                            try:
                                                nro_auto = int(input("Ingrese el numero de auto del piloto: \n"))
                                            except ValueError:
                                                print("El argumento ingresado es de un tipo incorrecto")
                                                break

                                            if (nro_auto <= 0):
                                                try:
                                                    raise ArgumentoFueraDeRango(420, "El argumento ingresado esta fuera del rango esperado")
                                                except ArgumentoFueraDeRango as e:
                                                    print(e)
                                                    sys.exit()
                                            elif nro_auto == "":
                                                try:
                                                    raise ArgumentoVacio(430, "El argumento ingresado es vacio")
                                                except ArgumentoVacio as e:
                                                    print(e)
                                                    sys.exit()
                                            else:
                                                carrera.registrar_imprevisto(nro_auto, 2)
                                                print("ee")
                                                menu_numero_auto = 0
                                        elif menu_numero_auto == 2:
                                            menu_simular_carrera = 0
                                            break
                                break
                        
                    elif menu_simular_carrera==4:
                        while True:
                            try:
                                nro_auto = int(input("Ingrese el numero de auto del piloto: \n"))
                            except ValueError:
                                print("El argumento ingresado es de un tipo incorrecto")
                                break

                            if (nro_auto<=0):
                                try:
                                    raise ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera del rango esperado")
                                except ArgumentoFueraDeRango as e:
                                    print(e)
                                    sys.exit()
                            elif nro_auto=="":
                                try:
                                    raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                                except ArgumentoVacio as e:
                                    print(e)
                                    sys.exit()
                            else:
                                carrera.registrar_imprevisto(nro_auto, 3)
                                menu_numero_auto = 0
                                while menu_numero_auto !=2:
                                    while (menu_numero_auto>2) or (menu_numero_auto<1):    
                                        try:    
                                            menu_numero_auto = int(input("\nIngrese una opción:\n 1.Si desea seguir agregando numeros de auto de pilotos que reciben penalidad \n 2.No desea seguir agregando numeros de autos \n" ))
                            
                                        except ValueError: 
                                            print("Valor incorrecto.\nIntentelo de nuevo\n")
                                            menu_numero_auto = 0

                                        if (menu_numero_auto>2) or (menu_numero_auto<1):
                                            try:
                                                raise ArgumentoFueraDeRango(400,"Valor fuera de rango esperado\n Intentelo nuevamente\n")
                                            
                                            except ArgumentoFueraDeRango as e:
                                                print(e)
                                                return None

                                        elif (menu_numero_auto==None):
                                            try:
                                                raise ArgumentoVacio(410,"El argumento ingresado es vacio\n Intentalo nuevamente\n")
                                            except ArgumentoVacio as e:
                                                print(e)
                                                menu_numero_auto = 0
                                        elif menu_numero_auto == 1:
                                        
                                            try:
                                                nro_auto = int(input("Ingrese el numero de auto del piloto: \n"))
                                            except ValueError:
                                                print("El argumento ingresado es de un tipo incorrecto")
                                                continue

                                            if (nro_auto <= 0):
                                                try:
                                                    raise ArgumentoFueraDeRango(420, "El argumento ingresado esta fuera del rango esperado")
                                                except ArgumentoFueraDeRango as e:
                                                    print(e)
                                                    menu_numero_auto = 0
                                                    break
                                            elif nro_auto == "":
                                                try:
                                                    raise ArgumentoVacio(430, "El argumento ingresado es vacio")
                                                except ArgumentoVacio as e:
                                                    print(e)
                                                    menu_numero_auto = 0
                                                    break
                                            else:
                                                carrera.registrar_imprevisto(nro_auto, 3)
                                                menu_numero_auto = 0
                                        elif menu_numero_auto == 2:
                                            menu_simular_carrera = 0
                                            break
                                break
                    elif menu_simular_carrera == 5:
                        print("")
                        carrera.determinar_posiciones()
                        carrera.resumen_posiciones()
                        return
                    elif menu_simular_carrera == 6:
                        simulando = False
                        break                   
            
        




                                                

