import sys
from entities.auto import Auto
sys.path.append('..')
from gestion import Gestion
from exceptions.Argumento_Invalido import ArgumentoInvalido
from exceptions.La_entidad_ya_existe import LaEntidadYaExiste
from exceptions.Argumento_vacio import ArgumentoVacio
from exceptions.Argumento_fuera_de_rango import ArgumentoFueraDeRango
from datetime import datetime

def alta_de_auto(gestion:Gestion):
    lista_de_autos=[]
    date =datetime.now()
    while True:
        try:
            modelo = str(input("Ingrese el modelo del auto:"))
        except ArgumentoInvalido:
            print("El argumento ingresado es invalido")
            return None
        
        if (modelo==""):
            try:
                raise ArgumentoVacio(430,"El argumento ingresado es vacio")
            except ArgumentoVacio as e:
                print(e)
                return None
        else:
            try:
                anio_auto = int(input("Ingrese el año del auto:"))
            except ValueError:
                print("El valor ingresado ha sido distinto de un numero")
                return None
            
            if anio_auto<1900 or anio_auto>date.year:
                try:
                    raise ArgumentoFueraDeRango(410,"Argumento fuera de rango") #
                except ArgumentoFueraDeRango as e:
                    print(e)
                    return None
                
            elif anio_auto=="":
                try:
                    raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                except ArgumentoVacio as e:
                    print(e)
                    return None
                
            else:
                try:
                    score_auto = int(input("Ingrese el score del auto:"))
                except ValueError:
                    print("El valor ingresado ha sido distinto de un numero")
                    return None
                
                if (score_auto<1) or (score_auto>100):
                    try:
                        raise ArgumentoFueraDeRango(420,"Argumento fuera de rango") #
                    except ArgumentoFueraDeRango as e:
                        print(e)
                        return None
                    
                elif (score_auto==""):
                    try:
                        ArgumentoVacio(430,"El argumento ingresado es vacio")
                    except ArgumentoVacio as e:
                        print(e)
                        return None
                else:
                    auto_temp=Auto(modelo,None,None)
                    for elementos in gestion._autos:
                        if elementos.__eq__(auto_temp):
                            try:
                                raise LaEntidadYaExiste(410,"El auto ya existe")
                            except LaEntidadYaExiste as e:
                                print(e)
                                return None
                    
                    auto1 = Auto(modelo,anio_auto,score_auto)
                    lista_de_autos.append(auto1)
                    
                return lista_de_autos
                 
                
                    