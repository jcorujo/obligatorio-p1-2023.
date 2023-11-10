from gestor_equipos import Gestor_Equipos
from entities.equipo import Equipo
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.director import Director
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste
from exceptions.NoEsPiloto import NoEsPiloto

class Gestor_Personal(Equipo):
       def __init__(self, empleados):
              super().__init__(empleados)

       def buscar_empleado(self, id):
              empleado_encontrado = None
              for empleado in self._empleados: 
                     if empleado.id() == id:
                            empleado_encontrado = empleado
              if empleado_encontrado == None:
                     raise EmpleadoNoExiste(410, "El empleado ingresado no existe, ingrese un id válido")
              return empleado_encontrado
       
       def agregar_piloto(self, id, nombre, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular):
              piloto = Piloto(id, nombre, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular)
              self._empleados.append(piloto)

       def es_piloto(self, id):
              empleado = Gestor_Personal.buscar_empleado(id)  
              es_piloto = isinstance(empleado, Piloto)
              return es_piloto
       
       def obtener_pilotos(self):
              pilotos = []
              for empleado in self._empleados:
                     if Gestor_Personal.es_piloto(empleado.id):
                            pilotos.append(empleado)
              return pilotos

       def agregar_mecanico(self,id, nombre, fecha_nacimiento, nacionalidad, salario, score):
              mecanico = Mecanico(id, nombre, fecha_nacimiento, nacionalidad, salario, score)
              self._empleados.append(mecanico)
       
       def es_mecanico(self, id):
              empleado = Gestor_Personal.buscar_empleado(id)  
              es_mecanico = isinstance(empleado, Piloto)
              return es_mecanico
       
       def obtener_mecanicos(self):
              mecanicos = []
              for empleado in self._empleados:
                     if Gestor_Personal.es_mecanico(empleado.id):
                            mecanicos.append(empleado)
              return mecanicos

       def agregar_director(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
              director = Director(id, nombre, fecha_nacimiento, nacionalidad, salario)
              self._empleados.append(director)

       def es_director(self, id):
              empleado = Gestor_Personal.buscar_empleado(id)  
              es_director = isinstance(empleado, Piloto)
              return es_director
       
       def retirar_empleado(self, id):
              empleado = Gestor_Personal.buscar_empleado(id)
              self._empleados.remove(empleado)
       
       def dar_baja_medica(self, id):
              if not Gestor_Personal.es_piloto(id):
                     raise NoEsPiloto(418, "El empleado ingresado no es piloto") 
              piloto = Gestor_Personal.buscar_empleado
              piloto.esta_lesionado(False)

       def dar_alta_medica(self, nombre):
              if not Gestor_Personal.es_piloto(id):
                     raise NoEsPiloto(418, "El empleado ingresado no es piloto") 
              piloto = Gestor_Personal.buscar_empleado
              piloto.esta_lesionado(True)
                 
#¿Vamos a agregar metodos para cambiar salarios, nro_autos , etc?


      
     
