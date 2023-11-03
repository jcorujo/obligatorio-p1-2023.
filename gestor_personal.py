from entities.equipo import Equipo

class Gestor_Personal(Equipo):
       def __init__(self, empleados):
              super().__init__(empleados)
       
       def agregar_piloto(self, equipo, nombre, id, fecha_nacimiento, nacionalidad, salario, nro_auto):
              
              #VERIFICAR EXISTENCIA EQUIPO
              #VERIFICAR CAPACIDAD EQUIPO
              #VERIFICAR QUE NO EXISTA PILOTO CON MISMO ID, EN EL EQUIPO U OTROS EQUIPOS
              #CREAR PILOTO
              pass
       def agregar_mecanico(self, equipo, id, nombre, fecha_nacimiento, nacionalidad, salario):
              pass
       
       def agregar_director(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
              pass
       
       def cambiar_piloto(self):
              pass

       def cambiar_nombre(self, id, nombre):
              pass
       def cambiar_nacionalidad(self, id, nacionalidad):
              pass
       def cambiar_salario(self, id, salario):
              pass
       def cambiar_auto(self, id, nro_auto):
              #checkear que es piloto
              pass

       #CAMBIAR SALARIO, AUTO, NOMBRE
       def dar_baja(self, nombre):
              pass
       def dar_alta(self, nombre):
              pass   
      
     
