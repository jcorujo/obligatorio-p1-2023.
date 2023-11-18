import sys
sys.path.append('..')
from gestion import Gestion
from entities.director import Director

def retornar_jefes(gestion:Gestion):
    jefes_equipo=[]
    for equipo in gestion.equipos:
        director = ''
        for empleado in equipo.empleados:
            if isinstance(empleado, Director):
                director = empleado
        
        director_nombre_equipo=f"{director.nombre} ({equipo.nombre})"
        jefes_equipo.append(director_nombre_equipo)
    
    jefes_equipo_ordenado=sorted(jefes_equipo)
    return jefes_equipo_ordenado