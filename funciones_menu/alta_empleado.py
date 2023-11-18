import sys
from datetime import datetime
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.director import Director
sys.path.append('..')
from gestion import Gestion
from exceptions.Argumento_Invalido import ArgumentoInvalido
from exceptions.La_entidad_ya_existe import LaEntidadYaExiste
from exceptions.Argumento_fuera_de_rango import ArgumentoFueraDeRango
from exceptions.Argumento_vacio import ArgumentoVacio
import re

def alta_empleado(gestion:Gestion):
    lista_empleados=[]
    lista_numeros=[]
    date =datetime.now()
    while True:
        try:
            id = int(input("Ingrese el número de cedula del empleado:"))
        except ValueError:
            break

        if str(id).isspace()==True:
            try:
                raise ArgumentoInvalido(400,"El argumento ingresado es invalido")
            except ArgumentoInvalido as e:
                print(e)
                return None
        
        elif len(str(id))!=8:
            try:
                raise ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera de los rangos esperados")
            except ArgumentoFueraDeRango as e:
                print(e)
                return None   
               
        else:
            try:
                nombre = input("Ingrese el nombre del empleado: ")
                p=re.compile(r"\d+")
                lista_numeros=p.findall(nombre)
            
                if lista_numeros!=[]:
                    raise ArgumentoInvalido(400,"El argumento ingresado es invalido")
            
            except ArgumentoInvalido:
                return None
            
            if (nombre==""):
                try:
                    raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                except ArgumentoVacio as e:
                    print(e)
                    return None
            else:
                try:
                    fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato (DD/MM/YYYY): ")
                except ValueError:
                    print("La fecha ingresada este en un formato erroneo")
                    return None

                

                fecha_n = fecha_nacimiento.split("/") #Crea una lista separando los elementos por la /
                
                try: 
                    dia=int(fecha_n[0])
                    mes=int(fecha_n[1])
                    anio=int(fecha_n[2])
                except IndexError:
                    print("El argumento ingresado esta fuera de rango")
                    return None
            

                if (dia=="") or (mes=="") or (anio==""):
                    try:
                        raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                    except ArgumentoVacio as e:
                        print(e)
                        return None

                elif dia>30 or dia<1 or mes>12 or mes<1 or anio<1900 or anio>date.year:
                    try:
                        raise ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera de los rangos esperados")
                    except ArgumentoFueraDeRango as e:
                        print(e)
                        return None
                else:

                    if mes<date.month:
                        edad=date.year-anio
                        
                    elif mes>date.month:
                        edad=date.year-anio+1
                    
                    elif mes==date.month and dia>=date.day:
                        edad=edad=date.year-anio+1
                        
                    else:
                        edad=date.year-anio

                    if edad < 18:
                        try:
                            raise ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera de los rangos esperados")   
                        except ArgumentoFueraDeRango as e:
                            print(e)
                            return None                    
                    try:
                        nacionalidad = str(input("Ingrese la nacionalidad del empleado:"))
                        p=re.compile(r"\d+")
                        lista_numeros=p.findall(nacionalidad)
                        if lista_numeros!=[]:
                            try:
                                raise ArgumentoInvalido(400,"El argumento ingresado es invalido")
                            except ArgumentoInvalido as e:
                                print (e)
                                return None

                    except ValueError:
                        try:
                            raise ArgumentoInvalido(400,"El argumento ingresado es invalido")
                        except ArgumentoInvalido as e:
                            print(e)
                            return None
                        
                    if (nacionalidad=="") :
                        try:
                            raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                        except ArgumentoVacio as e:
                            print(e)
                            return None
                    else:
                        try:
                            salario = float(input("Ingrese el salario del empleado:"))
                        except ValueError:
                            print("El argumento ingresado es de un tipo incorrecto")
                            return None

                        if (salario<=0):
                            try:
                                raise ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera del rango esperado")
                            except ArgumentoFueraDeRango as e:
                                print(e)
                                return None
                        elif salario=="":
                            try:
                                raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                            except ArgumentoVacio as e:
                                print(e)
                                return None
                        
                        else:
                            try:
                                opcion_cargo = int(input("\nIngresé el cargo del empleado:\n 1.Piloto\n 2.Piloto de reserva\n 3.Mecanico\n 4.Jefe de equipo\n"))
                            except ValueError:
                                print("El argumento ingresado es erroneo")
                                return None
                            
                            if (opcion_cargo>4) or (opcion_cargo<1):
                                try:
                                    ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera del rango esperado")
                                except ArgumentoFueraDeRango as e:
                                    print(e)
                                    return None
                            elif opcion_cargo=="":
                                try:
                                    ArgumentoVacio(430,"El argumento ingresado es vacio")
                                except ArgumentoVacio as e:
                                    print(e)
                                    return None
                               
                            else:
                                if opcion_cargo == 1:
                                    try:
                                        score = int(input("Ingrese el score del piloto:"))
                                    except ValueError:
                                        print("El valor ingresado ha sido distinto de un numero")
                                        return None
                                    
                                    if (score<1) or (score>99):
                                        try:
                                            raise ArgumentoFueraDeRango(420,"Argumento fuera de rango") #
                                        except ArgumentoFueraDeRango as e:
                                            print(e)
                                            return None
                                        
                                    elif (score==""):
                                        try:
                                            ArgumentoVacio(430,"El argumento ingresado es vacio")
                                        except ArgumentoVacio as e:
                                            print(e)
                                            return None
                                    else:
                                        try:
                                            nbr_auto=int(input("Ingrese el numero de auto de ese piloto:"))
                                        except ValueError:
                                            print("El valor ingresado ha sido distinto de un numero")
                                            return None
                                        if (nbr_auto<1) :
                                            try:
                                                raise ArgumentoFueraDeRango(420,"Argumento fuera de rango")
                                            except ArgumentoFueraDeRango as e:
                                                print(e)
                                                return None
                                        elif (nbr_auto==""):
                                            try:
                                                ArgumentoVacio(430,"El argumento ingresado es vacio")
                                            except ArgumentoVacio as e:
                                                print(e)
                                                return None
                                        else:
                                            if gestion.buscar_empleado(id):
                                                try:
                                                    raise LaEntidadYaExiste(410,"La entidad ya existe")
                                                except LaEntidadYaExiste as e:
                                                    print(e)
                                                    return None
                                            else:
                                                piloto1=Piloto(id,nombre,fecha_nacimiento,nacionalidad,salario,nbr_auto,score, True)
                                                lista_empleados.append(piloto1)
                                            return lista_empleados

                                        
                                elif opcion_cargo == 2:
                                    try:
                                        score = int(input("Ingrese el score del piloto:"))
                                    except ValueError:
                                        print("El valor ingresado ha sido distinto de un numero")
                                        return None
                                    
                                    if (score<1) or (score>99):
                                        try:
                                            raise ArgumentoFueraDeRango(420,"Argumento fuera de rango") #
                                        except ArgumentoFueraDeRango as e:
                                            print(e)
                                            return None
                                        
                                    elif (score==""):
                                        try:
                                            ArgumentoVacio(430,"El argumento ingresado es vacio")
                                        except ArgumentoVacio as e:
                                            print(e)
                                            return None
                                    else:
                                        try:
                                            nbr_auto=int(input("Ingrese el numero de auto de ese piloto:"))
                                        except ValueError:
                                            print("El valor ingresado ha sido distinto de un numero")
                                            return None
                                        if (nbr_auto<1) :
                                            try:
                                                raise ArgumentoFueraDeRango(420,"Argumento fuera de rango")
                                            except ArgumentoFueraDeRango as e:
                                                print(e)
                                                return None
                                        elif (nbr_auto==""):
                                            try:
                                                ArgumentoVacio(430,"El argumento ingresado es vacio")
                                            except ArgumentoVacio as e:
                                                print(e)
                                                return None
                                        else:
                                                if gestion.buscar_empleado(id):
                                                    try:
                                                        raise LaEntidadYaExiste(410,"La entidad ya existe")
                                                    except LaEntidadYaExiste as e:
                                                        print(e)
                                                        return None
                                                else:
                                                    piloto2=Piloto(id,nombre,fecha_nacimiento,nacionalidad,salario,nbr_auto,score, False)
                                                    lista_empleados.append(piloto2)
                                                return lista_empleados

                                elif opcion_cargo == 3:
                                    try:
                                        score = int(input("Ingrese el score del mecanico:"))
                                    except ValueError:
                                        print("El valor ingresado ha sido distinto de un numero")
                                        return None
                                    
                                    if (score<1) or (score>99):
                                        try:
                                            raise ArgumentoFueraDeRango(420,"Argumento fuera de rango") #
                                        except ArgumentoFueraDeRango as e:
                                            print(e)
                                            return None
                                        
                                    elif (score==""):
                                        try:
                                            ArgumentoVacio(430,"El argumento ingresado es vacio")
                                        except ArgumentoVacio as e:
                                            print(e)
                                            return None
                                    else:
                                        if gestion.buscar_empleado(id):
                                            try:
                                                raise LaEntidadYaExiste(410,"La entidad ya existe")
                                            except LaEntidadYaExiste as e:
                                                print(e)
                                                return None
                                        else:
                                            mecanico=Mecanico(id,nombre,fecha_nacimiento,nacionalidad,salario,score)
                                    
                                            lista_empleados.append(mecanico)
                                        return lista_empleados

                                elif opcion_cargo == 4:
                                        if gestion.buscar_empleado(id):
                                            try:
                                                raise LaEntidadYaExiste(410,"La entidad ya existe")
                                            except LaEntidadYaExiste as e:
                                                print(e)
                                                return None
                                        else:
                                            jefe_equipo=Director(id,nombre,fecha_nacimiento,nacionalidad,salario)
                                            lista_empleados.append(jefe_equipo)
                                        return lista_empleados

                                else:
                                    return lista_empleados