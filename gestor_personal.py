from entities.equipo import Equipo
from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.director import Director
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste
from exceptions.NoEsPiloto import NoEsPiloto

class Gestor_Personal():
       def __init__(self, equipo):
              self._equipo = equipo
              self._empleados = equipo.empleados

       @property
       def equipo(self):
              return self._equipo
      
       def buscar_empleado(self, id):
              empleado_encontrado = None
              for empleado in self._empleados: 
                     if empleado.id == id:
                            empleado_encontrado = empleado
              return empleado_encontrado   
       
       def verificar_empleado(self, id):
              empleado_encontrado = None
              for empleado in self._empleados: 
                     if empleado.id == id:
                            empleado_encontrado = empleado
              if empleado_encontrado == None:
                     raise EmpleadoNoExiste(410, "El empleado ingresado no existe, ingrese un id válido")
              return empleado_encontrado
       
       def agregar_piloto(self, id, nombre, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular):
              piloto = Piloto(id, nombre, fecha_nacimiento, nacionalidad, salario, nro_auto, score, es_titular)
              self.equipo.agregar_empleado(piloto)

       def es_piloto(self, id):
              empleado = self.verificar_empleado(id)  
              es_piloto = isinstance(empleado, Piloto)
              return es_piloto
       
       def obtener_pilotos(self):
              pilotos = []
              for empleado in self._empleados:
                     if self.es_piloto(empleado.id):
                            pilotos.append(empleado)
              return pilotos

       def agregar_mecanico(self,id, nombre, fecha_nacimiento, nacionalidad, salario, score):
              mecanico = Mecanico(id, nombre, fecha_nacimiento, nacionalidad, salario, score)
              self._empleados.append(mecanico)
       
       def es_mecanico(self, id):
              empleado = self.verificar_empleado(id)  
              es_mecanico = isinstance(empleado, Mecanico)
              return es_mecanico
       
       def obtener_mecanicos(self):
              mecanicos = []
              for empleado in self._empleados:
                     if self.es_mecanico(empleado.id):
                            mecanicos.append(empleado)
              return mecanicos

       def agregar_director(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
              director = Director(id, nombre, fecha_nacimiento, nacionalidad, salario)
              self._empleados.append(director)

       def es_director(self, id):
              empleado = self.verificar_empleado(id)  
              es_director = isinstance(empleado, Director)
              return es_director
       
       def retirar_empleado(self, id):
              empleado = self.verificar_empleado(id)
              self._empleados.remove(empleado)
       
       def dar_baja_medica(self, id):
              if not self.es_piloto(id):
                     raise NoEsPiloto(418, "El empleado ingresado no es piloto") 
              piloto = self.verificar_empleado(id)
              piloto.esta_lesionado(True)

       def dar_alta_medica(self, id):
              if not Gestor_Personal.es_piloto(self, id):
                     raise NoEsPiloto(418, "El empleado ingresado no es piloto") 
              piloto = Gestor_Personal.verificar_empleado
              piloto.esta_lesionado(False)
       
       def habilitados_para_correr(self):
        pilotos_habilitados = []
        for piloto in self.obtener_pilotos():
            if piloto.es_titular and not piloto.esta_lesionado:
                pilotos_habilitados.append(piloto)
        if len(pilotos_habilitados) < 2:
            for piloto in self.obtener_pilotos():
                if not piloto.es_titular and not piloto.esta_lesionado:
                    pilotos_habilitados.append(piloto)
        return pilotos_habilitados

                 



      
     
