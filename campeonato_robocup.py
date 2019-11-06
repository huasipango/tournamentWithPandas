import csv
import pandas
import os
import random
from datetime import datetime, timedelta

class Jugador:
    def __init__(self, nombre, apellido, id, nivel, equipo):
        self.nombre=nombre
        self.apellido=apellido
        self.nivel=nivel
        self.id=id
        self.equipo=equipo
    def like_a_frame(self):
        return {'nombre':self.nombre,'apellido':self.apellido,'id':self.id,'nivel':self.nivel,'equipo':self.equipo}
class Equipo:
    jugadores = []
    def __init__(self, nombre, telefono, partidos_jugados=0, partidos_ganados=0, partidos_empatados=0, partidos_perdidos=0, 
                puntos_totales=0, goles_marcados=0, goles_recibidos=0, gol_diferencia=0, id_capitan=None):
        self.nombre=nombre
        self.telefono=telefono
        self.partidos_jugados=partidos_jugados
        self.partidos_ganados=partidos_ganados
        self.partidos_empatados=partidos_empatados
        self.partidos_perdidos=partidos_perdidos
        self.puntos_totales=puntos_totales
        self.goles_marcados=goles_marcados
        self.goles_recibidos=goles_recibidos
        self.gol_diferencia=gol_diferencia
        self.id_capitan=id_capitan
    def like_a_frame(self):
        return {'nombre': self.nombre,'telefono': self.telefono,'partidos_jugados':self.partidos_jugados,'partidos_ganados':self.partidos_ganados,
        'partidos_empatados':self.partidos_empatados,'partidos_perdidos':self.partidos_perdidos,'puntos_totales':self.puntos_totales,
        'goles_marcados':self.goles_marcados,'goles_recibidos':self.goles_recibidos,'gol_diferencia':self.gol_diferencia,'id_capitan':self.id_capitan}

class Campeonato:
    
    lista_equipos = []
    lista_jugadores = []
    grupo_a=object
    grupo_b=object
    cronograma=pandas.DataFrame()
    tabla_puntuaciones=pandas.DataFrame()

    def __init__(self):
        pass

    def comprobar_faltan_equipos(self):
        if len(self.lista_equipos) < 6: #CAMBIAR============================================================
            print("¡ERROR! Deben existir seis equipos.")
            print("Elementos actuales: " + str(len(self.lista_equipos)))
            return True
        else:
            return False
    def guardar_equipo_csv(self, equipo):
        columns=["nombre","telefono","partidos_jugados","partidos_ganados","partidos_empatados","partidos_perdidos","puntos_totales","goles_marcados","goles_recibidos","gol_diferencia","id_capitan"]
        tabla=pandas.DataFrame([equipo.like_a_frame()], columns=columns)
        with open("csv/equipos.csv", "a") as file:
            tabla.to_csv(file, header=file.tell()==0, index=False)
        self.lista_equipos.append(equipo)
    def guardar_puntajes_grupo_a_csv(self, puntajes):
        if os.path.exists("csv/puntajes-grupo-a.csv"):
            os.remove("csv/puntajes-grupo-a.csv")    
        with open("csv/puntajes-grupo-a.csv", "a") as file:
            puntajes.to_csv(file, header=file.tell()==0, index=False)
    def guardar_puntajes_grupo_b_csv(self, puntajes):
        if os.path.exists("csv/puntajes-grupo-b.csv"):
            os.remove("csv/puntajes-grupo-b.csv")    
        with open("csv/puntajes-grupo-b.csv", "a") as file:
            puntajes.to_csv(file, header=file.tell()==0, index=False)
    def inicio(self):
        opc1="0"
        while opc1 not in ["1","2","3","4"]:
            print("MENÚ")
            print("1. Crear un torneo nuevo")
            print("2. Consultar equipos de la pasada edición")
            print("3. Consultar jugadores de la pasada edición")
            print("4. Consultar tabla de puntuación de la pasada edición")
            opc1=input("Seleccione la opción: ")
            os.system('cls')
            if opc1.isdigit():
                if opc1 == "1":
                    opc2="0"
                    while opc2 not in ["1","2","3","4","5","6"]:
                        print("MENÚ")
                        print("1. Ingresar equipo y sus jugadores")
                        print("2. Crear carnés de cancha")
                        print("3. Crear cronograma")
                        print("4. Definir resultados de partidos")
                        print("5. Consultar tabla de posiciones")
                        print("6. Atrás")
                        opc2=input("Seleccione la opción: ")                 
                        if opc2.isdigit():
                            if opc2=="1":
                                if len(self.lista_equipos) == 6:
                                    print("¡ERROR! No pueden haber más de seis equipos")
                                else:
                                    self.ingresar_equipo()
                                opc2="0"
                            elif opc2=="2":
                                if self.comprobar_faltan_equipos()==False:#EXISTEN 6 EQUIPOS
                                    self.imprimir_carnes()
                                opc2="0"
                            elif opc2=="3":
                                if self.comprobar_faltan_equipos()==False:
                                    if self.cronograma.empty==True:
                                        self.crear_cronograma()
                                    else:
                                        print("¡ERROR! Ya se generó un cronograma para este evento")
                                    print(self.cronograma.to_string(index=False))
                                opc2="0"
                            elif opc2=="4":
                                if self.comprobar_faltan_equipos()==False:
                                    if self.cronograma.empty==True:
                                        print("¡ERROR! Aún no ha creado el cronograma. Intente con la opción 3 e intente de nuevo.")
                                    else:
                                        self.ingresar_resultados()
                                opc2="0"
                            elif opc2=="5":
                                if self.comprobar_faltan_equipos()==False:
                                    self.imprimir_tabla()
                                opc2="0"
                            elif opc2=="6":
                                opc1="0"     
                            else:
                                print("INGRESO INCORRECTO")
                        else:
                            opc2="0"
                            print("¡ERROR EN EL INGRESO!")
                elif opc1=="2":
                    if os.path.exists("csv/equipos.csv"):
                        df=pandas.read_csv("csv/equipos.csv")
                        print (df)
                    else:
                        print("¡ERROR! No existe historial de la edición pasada, cree una nueva con la opción 1.")
                    opc1="0"
                elif opc1=="3":
                    if os.path.exists("csv/jugadores.csv"):
                        df=pandas.read_csv("csv/jugadores.csv")
                        print (df)
                    else:
                        print("¡ERROR! No existe historial de la edición pasada, cree una nueva con la opción 1.")
                    opc1="0"
                elif opc1=="4":
                    if os.path.exists("csv/puntajes-grupo-a.csv") and os.path.exists("csv/puntajes-grupo-b.csv"):
                        df1=pandas.read_csv("csv/puntajes-grupo-a.csv")
                        df2=pandas.read_csv("csv/puntajes-grupo-b.csv")
                        print (df1)
                        print (df2)
                    else:
                        print("¡ERROR! No existe historial de la edición pasada, cree una nueva con la opción 1.")
                    opc1="0"
            else:
                print("¡ERROR EN EL INGRESO!")
    def ingresar_equipo(self):
        print("Complete la siguiente información del equipo:")
        val_nombre=True
        val_numero=True
        while val_nombre:
            equ_nombre=input("(1/2)Nombre: ")
            if equ_nombre.isdigit():
                print("El campo no es una cadena de caracteres")
                val_nombre=True
            else:
                val_nombre=False
        while val_numero:
            equ_telefono=input("(2/2)Teléfono de contacto: ")
            if equ_telefono.isdigit():
                val_numero=False
            else:
                print("El campo no es un número")
                val_numero=True
        os.system('cls')
        print("")
        print("Los datos del equipo a guardar son:")
        print( "Nombre: " + equ_nombre + " Teléfono: " + equ_telefono)
        print("")
        opc1="a"
        equipo=object
        while opc1!="S" or opc1!="N":
            opc1=str(input("¿Está de acuerdo?(S/N)"))
            if opc1 == "S":
                equipo=Equipo(equ_nombre, equ_telefono)
                self.guardar_equipo_csv(equipo)
                self.ingresar_jugadores(equipo)
                break
            elif opc1=="N":
                break
            else:
                print("¡ERROR EN EL INGRESO!")        
    def ingresar_jugadores(self, equipo):
        opc1=True
        num_jugadores=0
        while opc1:
            num_jugadores=input("¿Cuántos jugadores tiene el equipo? (Mínimo 8 - máximo 12): ")
            if num_jugadores not in ["1","8","9","10","11","12"]:#TENCIÓN CORREGIR ==========================================
                print("¡ERROR EN EL INGRESO!")
                opc1=True
            else:
                opc1=False
        for i in range(int(num_jugadores)):
            os.system('cls')
            print("Complete la siguiente información del jugador " + str(i) + " :")
            val_nombre=True
            val_apellido=True
            val_id=True
            val_nivel=True
            while val_nombre:
                jug_nombre=input("(1/4) Ingrese el nombre: ")
                if jug_nombre.isdigit():
                    val_nombre=True 
                    print("El campo no es un nombre")
                else:
                    val_nombre=False
            while val_apellido:
                jug_apellido=input("(2/4) Ingrese el apellido: ")
                if jug_nombre.isdigit():
                    val_apellido=True 
                    print("El campo no es un apellido")
                else:
                    val_apellido=False
            while val_id:
                jug_id=input("(3/4) Ingrese la cédula de identificación: ")
                if jug_id.isdigit():
                    val_id=False
                else:
                    print("El campo no es un número")
                    val_id=True
            while val_nivel:
                jug_nivel=input("(4/4) Ingrese el número del nivel: ")
                if jug_nivel.isdigit():
                    val_nivel=False
                else:
                    print("El campo no es un número")
                    val_nivel=True
            os.system('cls')
            print("")
            print("Los datos del jugador son:")
            print( "Nombre: " + jug_nombre + " Apellido: " + jug_apellido + " CI: " + jug_id + " Nivel: " + jug_nivel)
            print("")
            opc2="a"
            jugador=object
            while opc2!="S" or opc2!="N":
                opc2=str(input("¿Está de acuerdo?(S/N)"))
                if opc2 == "S":
                    jugador=Jugador(jug_nombre, jug_apellido, jug_id, jug_nivel, equipo.nombre)
                    self.guardar_jugador_csv(jugador)
                    break
                elif opc2=="N":
                    pass
                else:
                    print("¡ERROR EN EL INGRESO!")       
    def guardar_jugador_csv(self, jugador):
        columns=["nombre","apellido","id","nivel","equipo"]
        tabla=pandas.DataFrame([jugador.like_a_frame()], columns=columns)
        with open("csv/jugadores.csv", "a") as file:
            tabla.to_csv(file, header=file.tell()==0, index=False)
        self.lista_jugadores.append(jugador)
    def imprimir_carnes(self):
        print("Existen "+str(len(self.lista_jugadores))+" jugadores")
        for jugador1 in self.lista_jugadores:
            nombre=jugador1.nombre
            apellido=jugador1.apellido
            id=str(jugador1.id)
            nivel=str(jugador1.nivel)
            equipo=jugador1.equipo
            impresion=(
                f"_____________________________\n"
                f"_____________________________\n"
                f"C A R N E - D E - C A N C H A\n"
                f"     R O B O C U P  5\n"
                f" I N G. M E C A T R O N I C A\n"
                f"_____________________________\n"
                f"||Nombre: {nombre}\n"
                f"||Apellido: {apellido}\n"
                f"||CI: {id}\n"
                f"||Nivel: {nivel}\n"
                f"||Equipo: {equipo}\n"
                f"||___________________________|\n"
            )
            f=open("txt/"+str(id)+".txt", "w+")
            f.write(impresion)
            f.close()
    def crear_cronograma(self):
        lista=self.lista_equipos
        random.shuffle(lista)
        self.grupo_a=lista[:3]
        self.grupo_b=lista[3:]
        print("")
        print("GRUPO A:")
        for equipo_a in self.grupo_a:
            print(equipo_a.nombre)
        print("GRUPO B:")
        for equipo_b in self.grupo_b:
            print(equipo_b.nombre)
        grupo_a=self.grupo_a
        grupo_b=self.grupo_b
        #CREAR CRONOGRAMA
        emparejamientos_a=[[grupo_a[0].nombre,grupo_a[1].nombre], [grupo_a[0].nombre,grupo_a[2].nombre], [grupo_a[1].nombre,grupo_a[2].nombre]]
        emparejamientos_b=[[grupo_b[0].nombre,grupo_b[1].nombre], [grupo_b[0].nombre,grupo_b[2].nombre], [grupo_b[1].nombre,grupo_b[2].nombre]]
        campeonato=[]
        fecha_inicio="7/11/19"
        fecha=datetime.strptime(fecha_inicio, "%d/%m/%y")
        for i in range(3):
            campeonato.append([i+1, "A", emparejamientos_a[i][0], emparejamientos_a[i][1], fecha.strftime("%d/%m/%Y")])
            campeonato.append([i+1, "B", emparejamientos_b[i][0], emparejamientos_b[i][1], fecha.strftime("%d/%m/%Y")])
            fecha=fecha+timedelta(days=7)
        df=pandas.DataFrame(campeonato, columns=["Fecha","Grupo","Equipo 1","Equipo 2","Día"])
        df.style.hide_index()
        self.cronograma=df
    def ingresar_resultados(self):
        print("INGRESO DE RESULTADOS")
        for indice_fila, fila in self.cronograma.iterrows():
            print("Grupo " + fila['Grupo'])
            print(fila['Equipo 1'] + " vs " + fila['Equipo 2'])
            val=True
            while val:
                goles_a=input("Goles de " + fila['Equipo 1'] + ":")
                if goles_a.isdigit():
                    goles_b=input("Goles de " + fila['Equipo 2'] + ":")
                    if goles_b.isdigit():
                        val=False
                    else:
                        print("INGRESO INCORRECTO")
                        val=True
                else:
                    print("INGRESO INCORRECTO")
                    val=True
            for i in range(len(self.lista_equipos)):
                if fila['Equipo 1'] == self.lista_equipos[i].nombre: #EQUIPO 1
                    if goles_a>goles_b: #GANA
                        self.lista_equipos[i].partidos_ganados+=1
                        self.lista_equipos[i].puntos_totales+=3
                    elif goles_a<goles_b: #PIERDE
                        self.lista_equipos[i].partidos_perdidos+=1
                    else: #EMPATA
                        self.lista_equipos[i].partidos_empatados+=1
                        self.lista_equipos[i].puntos_totales+=1
                    self.lista_equipos[i].partidos_jugados+=1
                    self.lista_equipos[i].goles_marcados+=int(goles_a)
                    self.lista_equipos[i].goles_recibidos+=int(goles_a)
                    self.lista_equipos[i].gol_diferencia+=int(goles_a)
                    self.lista_equipos[i].gol_diferencia-=int(goles_b)
                if fila['Equipo 2'] == self.lista_equipos[i].nombre: #EQUIPO PERDEDOR
                    if goles_a>goles_b: #PIERDE
                        self.lista_equipos[i].partidos_perdidos+=1
                    elif goles_a<goles_b: #GANA
                        self.lista_equipos[i].partidos_ganados+=1
                        self.lista_equipos[i].puntos_totales+=3
                    else: #EMPATA
                        self.lista_equipos[i].partidos_empatados+=1
                        self.lista_equipos[i].puntos_totales+=1
                    self.lista_equipos[i].partidos_jugados+=1
                    self.lista_equipos[i].goles_marcados+=int(goles_b)
                    self.lista_equipos[i].goles_recibidos+=int(goles_a)
                    self.lista_equipos[i].gol_diferencia+=int(goles_b)
                    self.lista_equipos[i].gol_diferencia-=int(goles_a)
        self.actualizar_equipo_csv()
    def actualizar_equipo_csv(self):
        os.remove("csv/equipos.csv")
        for equipo in self.lista_equipos:
            columns=["nombre","telefono","partidos_jugados","partidos_ganados","partidos_empatados","partidos_perdidos","puntos_totales","goles_marcados","goles_recibidos","gol_diferencia","id_capitan"]
            tabla=pandas.DataFrame([equipo.like_a_frame()], columns=columns)
            with open("csv/equipos.csv", "a") as file:
                tabla.to_csv(file, header=file.tell()==0, index=False)
    def imprimir_tabla(self):
        df=pandas.read_csv("csv/equipos.csv")
        nuevo_df=df
        nuevo_df.drop(columns=['telefono','id_capitan'], axis=1, inplace=True)
        nuevas_columnas=nuevo_df.columns.values
        nuevas_columnas=["Equipo","PJ","PG","PE","PP","PT","GM","GR","GD"]
        nuevo_df.columns=nuevas_columnas
        tabla_grupo_a=nuevo_df[:3]
        tabla_grupo_b=nuevo_df[3:]
        print("GRUPO A")
        nueva_columna=["A","A","A"]
        tabla_grupo_a.insert(loc=0, column="Grupo", value=nueva_columna)
        tabla_grupo_a=tabla_grupo_a.reset_index(drop=True)
        tabla_imprimir=tabla_grupo_a.sort_values(by=['PT','GD'], ascending=False)
        self.guardar_puntajes_grupo_a_csv(tabla_imprimir)
        print(tabla_imprimir.to_string(index=False))
        print("GRUPO B")
        nueva_columna=["B","B","B"]
        tabla_grupo_b.insert(loc=0, column="Grupo", value=nueva_columna)
        tabla_grupo_b=tabla_grupo_b.reset_index(drop=True)
        tabla_imprimir=tabla_grupo_b.sort_values(by=['PT','GD'], ascending=False)
        self.guardar_puntajes_grupo_b_csv(tabla_imprimir)
        print(tabla_imprimir.to_string(index=False))
torneo = Campeonato()
torneo.inicio()       
