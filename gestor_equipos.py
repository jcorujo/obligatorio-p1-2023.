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
    
    def buscar_piloto(self, id): 
        for equipo in self._equipos:
            pass
        
    def agregar_equipo(self, equipo):
        #Verificar que equipo no exista
        pass
    
    def cambiar_nombre(self, equipo, nuevo_nombre):
        pass
   

    def habilitados_para_correr(self):
        #checkear capacidad pilotos
        #return pilotos que corren
        #return a list
        pass
    def puede_participar(self):
        pass
        #checkear que tiene al menos un piloto
        #checkear que tiene los mecanicos necesarios
        #checkear que no falta un director
    def obtener_puntajes_pilotos(self):
        pass
    
