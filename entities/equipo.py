from entities.piloto import Piloto
from entities.mecanico import Mecanico
from entities.director import Director
from exceptions.NoEsPiloto import NoEsPiloto
from exceptions.EquipoSinCapacidad import EquipoSinCapacidad
from exceptions.EmpleadoNoExiste import EmpleadoNoExiste

class Equipo:
    def __init__(self, nombre:str):
        self._nombre = nombre
        self._auto = None
        self._empleados = []
        self._puntaje_campeonato = 0
    
    @property
    def nombre(self) -> str:
        return self._nombre 
    @property
    def empleados(self):
        return self._empleados
    @property
    def auto(self):
        return self._auto
    @property
    def puntaje_campeonato(self):
        return self._puntaje_campeonato

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    @auto.setter
    def auto(self, nuevo_auto):
        self._auto = nuevo_auto
    @puntaje_campeonato.setter
    def puntaje_campeonato(self, puntaje):
        self._puntaje_campeonato = puntaje

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
    
    def agregar_empleado(self, empleado):
        if isinstance(empleado, Piloto) or isinstance(empleado, Director) or isinstance(empleado, Mecanico):
            self._empleados.append(empleado)
    
    def es_piloto(self, id):
        empleado = self.verificar_empleado(id)  
        return isinstance(empleado, Piloto)
    
    def obtener_pilotos(self):
        pilotos = []
        for empleado in self._empleados:
            if self.es_piloto(empleado.id):
                pilotos.append(empleado)
        return pilotos

    def es_mecanico(self, id):
        empleado = self.verificar_empleado(id)  
        return isinstance(empleado, Mecanico)

    def obtener_mecanicos(self):
        mecanicos = []
        for empleado in self._empleados:
            if self.es_mecanico(empleado.id):
                 mecanicos.append(empleado)
        return mecanicos
    

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
        piloto.esta_lesionado = True

    def dar_alta_medica(self, id):
        if not self.es_piloto(id):
            raise NoEsPiloto(418, "El empleado ingresado no es piloto") 
        piloto = self.verificar_empleado(id)
        piloto.esta_lesionado = False
       
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

    def puede_participar(self):
        if len(self.habilitados_para_correr()) > 0:
            mecanicos = self.obtener_mecanicos()
            if len(mecanicos) > 7:
                for empleado in self.empleados:
                    if self.es_director(empleado.id):
                        return True
        return False
        