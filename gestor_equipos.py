class Gestor_Equipos:
    def __init__(self, equipos):
        self._equipos = []
    #CREAR EXCEPCIONES
    @property
    def equipos(self):
        return self._equipos
    
    def buscar_equipo(self, nombre_equipo):
        equipo_encontrado = None
        for equipo in self._equipos:
            if equipo.nombre == nombre_equipo:
                equipo_encontrado = equipo
        return equipo_encontrado
    
    def agregar_equipo(self, equipo):
        #Verificar que equipo no exista
        pass
    
    def cambiar_nombre(self, equipo, nuevo_nombre):
        pass
   
    def traspasar_pilotos(self, equipo, piloto):
        pass