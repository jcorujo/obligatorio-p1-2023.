import sys
from entities.equipo import Equipo
from entities.director import Director
sys.path.append('..')
from gestion import Gestion
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.auto import Auto
from exceptions.Argumento_Invalido import ArgumentoInvalido
from exceptions.Argumento_fuera_de_rango import ArgumentoFueraDeRango
from exceptions.Argumento_vacio import ArgumentoVacio
from exceptions.La_entidad_ya_existe import LaEntidadYaExiste
import re

def alta_de_equipo(gestion:Gestion):
    
    while True:
        try:
            nombre_equipo = input("Ingrese el nombre del equipo: ")
            p=re.compile(r"\d+")
            lista_numeros=p.findall(nombre_equipo)
        
            if lista_numeros!=[]:
                raise ArgumentoInvalido(400,"El argumento ingresado es invalido")
        
        except ArgumentoInvalido:
            return None
        if (nombre_equipo==""):
                try:
                    raise ArgumentoVacio(430,"El argumento ingresado es vacio")
                except ArgumentoVacio as e:
                    print(e)
                    return None
        else:
            
            try:
                modelo = str(input("Ingrese el modelo del auto:"))
                p=re.compile(r"\d+")
                lista_numeros=p.findall(modelo)
                
                if lista_numeros!=[]:
                    try:
                        raise ArgumentoInvalido(400,"El argumento ingresado es invalido")
                    except ArgumentoInvalido as e:
                        print(e)
                        return None
                
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
                cedulas_reg = []
                for i in range(13):
                    try:
                        id_empleado = int(input(f"Ingrese el número de cedula del empleado {i+1}:"))
                    except ValueError:
                        break

                    if id_empleado in cedulas_reg:
                        try:
                            raise LaEntidadYaExiste(440,"La entidad que se quiere ingresar ya existe en el sistema")
                        except LaEntidadYaExiste as e:
                            print(e)
                            return None
                        
                    cedulas_reg.append(id_empleado)
                    print(cedulas_reg)
                    if str(id_empleado).isspace()==True:
                        try:
                            raise ArgumentoInvalido(400,"El argumento ingresado es invalido")
                        except ArgumentoInvalido as e:
                            print(e)
                            return None
                    
                    elif len(str(id_empleado))!=8:
                        try:
                            raise ArgumentoFueraDeRango(420,"El argumento ingresado esta fuera de los rangos esperados")
                        except ArgumentoFueraDeRango as e:
                            print(e)
                            return None
                    #...............................................................................................................

                    equipo=Equipo(nombre_equipo)
                    gestion.equipos.append(equipo)
                    gestion.campeonato.agregar_equipo(equipo)
                    
                    for empleado in gestion._empleados:
                        if isinstance(empleado,Director):
                            gestion.agregar_director(equipo, gestion.buscar_empleado(id_empleado))
                        elif isinstance(empleado,Piloto):
                            gestion.agregar_piloto(equipo, gestion.buscar_empleado(id_empleado))
                        elif isinstance(empleado,Mecanico):
                            gestion.agregar_mecanico(equipo, gestion.buscar_empleado(id_empleado))

                    automovil=Auto(modelo,"","")

                    for auto in gestion._autos:
                        if auto.equipo == None:
                            if modelo == auto.modelo:
                                automovil = auto
                                equipo.auto = automovil
                                auto.equipo = equipo

                        else:break
                    