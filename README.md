obligatorio-p1-2023 / Juan Manuel Corujo ; Santiago  Onandi

EXPLICACIÓN DE LA APLICACIÓN

Para usar la aplicación deberá ejecutrse el siguiente código en el menú principal (main):

    Inicializar una instancia de Gestión: gestion = Gestion().
    gestión inicializará un campeonato automaticamente.
    Cada equipo que se crea se incorpora automáticamente al campeonato.

    Ejecutar el método menú, que recibe como argumento la instancia de gestión: menu_de_inicio = menu(gestion)

    ALTA DE EMPLEADO:
    
    id = las id ingresadas deberan tener 8 dígitos. 
    nombre = string cualquiera (sin numeros)
    fecha nacimiento = deben ser de formato (DD/MM/AAAA). No puede ser inferior a 1900, el piloto no puede ser menor de 18 años.
    nacionalidad = string cualquiera.
    salario = int

    tipo empleado = 1 (Piloto titular) ; 2 (Piloto reserva) ; 3 (Mecanico) ; 4 (Jefe de Equipo)

        PILOTO TITULAR

        score = int (0-100)
        nro_auto = int

        PILOTO RESERVA

        score = int (0-100)
        nro_auto = int

        MECANICO

        score = int (0-100)
        
    ALTA DE AUTO
    
SACAR AGREGAR PUNTAJE CARRERA Y CAMPEONATO EN PILOTO Y EQUIPO!!!!!!!!!!
DESCRIPCIÓN DEL MODELO UML

Clase Auto:
    Atributos: "modelo", "anio" y "score". Variable de instancia "equipo".
    Cuenta con método __eq__.

Clase Empleado:
    
    Es una clase abstracta que heredan las clases Piloto, Mecánico, Director, que integra las características que comparten todos los tipos de empleado.

Clase Mecánico:
    
    Añade el score a los atributos de empleado. Se incorpora la variable de instancia "equipo".

Clase Director:
    
    Incorpora la variable de instancia "equipo".

Clase Piloto:
    
    Añade a los atributos de empleado el nro_auto; score ; es_titutular: bool. 
    Incorpora las variables de instancia "equipo" , "esta_lesionado",
    
    "puntaje_campeonato" (donde se almacena el puntaje que el Piloto acumula durante la vida del campeonato), 
    
    "puntaje_carrera" (donde se almacena el puntaje que el Piloto acumula durante una sola carrera, será 0 cuando esta termine), "
    
Clase Equipo:
    
    Cuenta con el atributo "nombre". Tiene en el constructor las siguientes variables de instancia: "auto" (de la clase Auto), "Empleados" (de la clase Piloto, Director o Mecanico), "puntaje_campeonato".

    Los métodos de instancia que posee son:

        buscar_empleado(id): busca un empleado por su ID en los empleados del equipo y lo retorna, si no pertenece, retorna None.
        
        verificar_empleado(id): Idem. al anterior pero si no encuentra levanta excepción.

        agregar_empleado(empleado): verifica que empleado sea una instancia valida y agrega el empleado al equipo.

        es_piloto(id): retorna True si empleado es piloto, False en caso contrario.
        es_mecanico(id): retorna True si empleado es mecánico, False en caso contrario.
        es_director(id): retorna True si empleado es director, False en caso contrario.
        
        obtener_pilotos(): devuelve una lista de las instancias de Piloto en self.empleados.
        obtener_mecanicos(): devuelve una lista de las instancias de Mecanico en self.empleados.  
        
        retirar_empleado(id): retira a un empleado del equipo.
        dar_alta_medica(id): si es piloto, cambia su variable de instancia "esta_lesionado" a False.
        dar_baja_medica(id): si es piloto, cambia su variable de instancia "esta_lesionado" a True.

        habilitados_para_correr(id): devuelve todos los pilotos habilitados para correr (que no están lesionados). Si un piloto titular esta lesionado y el reserva no, el reserva será devuelto en la lista en reemplazo al piloto titular.

        puede_participar(): si el equipo tiene al menos 8 mecanicos, un director, y al menos un piloto sin lesionar, devuelve True, caso contrario, False.

clase Carrera:
    
    Recibe como argumento una instancia de Campeonato.
    
    De la instancia de Campeonato toma los equipos que lo conforman, si el equipo puede_participar, lo incorpora en la variabe de instancia "equipos_participantes".
    
    De los equipos participantes toma los pilotos en habilitados_para_correr y los incoropora a "pilotos".
    
    También tiene una variable de instancia denominada "abandonaron", que es una lista que contendrá a los pilotos para los que se registre el imprevisto 0 (abandonaron).
    
    Para almacenar las posiciones de los pilotos una vez corrida la carrera, tiene una variable de instancia llamada "posiciones" que es un diccionario que toma como key la posicion, y como valor al piloto.

    Dentro de los métodos de instancia encontramos:

    buscar_piloto(nro_auto): busca un piloto en self._pilotos y lo retornea, si no existe levanta excepción.

    expulsar_piloto(nro_auto): retira a un piloto de la carrrera.

    registrar_imprevisto(nro_auto, tipo_imprevisto): recibe como argumentos el nro_auto de un piloto y el imprevisto que se le quiere asignar. 

        Si tipo_imprevisto es 0, lesiona al piloto y lo retira de la lista de pilotos, incorpora al piloto de reserva si es posible. Si estan todos los pilotos lesionados, retira al equipo de la carrera.
        
        Si tipo_imprevisto es 1, retira al piloto de la carrera.

        Si tipo_imprevisto a 2, piloto comete error en pits y recibe penalización de 5 puntos.

        Si tipo_imprevisto es 3, piloto comete infracción, recibe penañización de 8 puntos.

        Else levanta excepción.

    obtener_plantel(piloto): devuelve en una lista al piloto, junto a los mecanicos del equipo más el automovil del Equipo.

    adjudicar_puntaje(): para cada piloto participante, obtiene su plantel y le añade al atributo "puntaje_carrera" el score del piloto, mecanicos y automovil.
    Si el piloto abandonó el puntaje_carrera será 0.

    resetear_atributos(): para cada piloto en todos los equipos, deja a todos sin lesionar y elimina "puntaje_carrera".

    determinar_posiciones(): llama al método adjudicar_puntaje(), determina las posciones de mayor  a menor en forma descentente tomando el puntaje_carrera de cada piloto y las asocia a la variable de instancia "posiciones", de acuerdo a la posicion actualiza el valor de puntaje_campeonato. Al terminar llama a resetear_atributos().

    resumen_posiciones(): printea las posicioens de la carrera en forma descendente.

clase Campeonato:
    Recibe como argumento una lista de equipos participantes. El atributo se denomina "participantes"
    Tiene un diccionaro "posiciones".

    Cuenta con los siguientes métodos:

        agregar_equipo(equipo): agrega un equipo al atributo "participantes".
        
        expulsar_equipo(nombre_equipo): si existe un equipo con el mismo nombre lo elimina del campeonato.

        pilotos_con_mas_puntos(): printea en forma ascendente las posiciones (de mejor a peor) de los pilotos de los equipos en el campeonato.

        determinar_posiciones(): actualiza los valores en self.posiciones de acuerdo a "puntaje_campeonato" en los Equipos.

        resumen_posiciones(): printea las posiciones.

        terminar_campeonato(): reinicia el puntaje_campeonato para pilotos y equipos. 

A su vez, para facilitar la gestión y procesos existe la clase Gestión, a partir de la cual es funcional la aplicación. 

Esta contiene los siguientes métodos:

    buscar_empleado(id)

    buscar_equipo(nombre)

    agregar_piloto(equipo, piloto): toma un piloto existente y lo añade a un equipo existente.
    agregar_mecanico(equipo, piloto): toma un mecáncio existente y lo añade a un equipo existente.
    agregar_director(equipo, piloto): toma un director existente y lo añade a un equipo existente.

    tiene_capacidad(): para los diferentes tipos de empleados (1- Piloto titular; 2- Piloto reserva; 3- Director ; 4- Mecanico) verifica si existe capacidad para más empleados del mismo tipo.