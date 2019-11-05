from sqlalchemy import create_engine
from pandas.io import sql
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
    def __init__(self, nombre, telefono, partidos_jugados=None, partidos_empatados=None, partidos_perdidos=None, 
                puntos_totales=None, goles_marcados=None, goles_recibidos=None, gol_diferencia=None, id_capitan=None):
        self.nombre=nombre
        self.telefono=telefono
        self.partidos_jugados=partidos_jugados
        self.partidos_empatados=partidos_empatados
        self.partidos_perdidos=partidos_perdidos
        self.puntos_totales=puntos_totales
        self.goles_marcados=goles_marcados
        self.goles_recibidos=goles_recibidos
        self.gol_diferencia=gol_diferencia
        self.id_capitan=id_capitan
    def like_a_frame(self):
        return {'nombre': self.nombre,'telefono': self.telefono,'partidos_jugados':self.partidos_jugados,
        'partidos_empatados':self.partidos_empatados,'partidos_perdidos':self.partidos_perdidos,'puntos_totales':self.puntos_totales,
        'goles_marcados':self.goles_marcados,'goles_recibidos':self.goles_recibidos,'gol_diferencia':self.gol_diferencia,'id_capitan':self.id_capitan}

class Campeonato:
    
    lista_equipos = []
    lista_jugadores = []
    grupo_a=object
    grupo_b=object
    cronograma=object

    def __init__(self):
        pass
    def cargar_torneo(self):
        pass

    def guardar_torneo(self):
        pass
    def comprobar_faltan_equipos(self):
        if len(self.lista_equipos) < 0: #CAMBIAR============================================================
            print("¡ERROR! Deben existir seis equipos.")
            print("Elementos actuales: " + str(len(self.lista_equipos)))
            return "0"
        else:
            return "2"

    def guardar_equipo_csv(self, equipo):
        columns=["nombre","telefono","partidos_jugados","partidos_empatados","partidos_perdidos","puntos_totales","goles_marcados","goles_recibidos","gol_diferencia","id_capitan"]
        tabla=pandas.DataFrame([equipo.like_a_frame()], columns=columns)
        with open("csv/equipos.csv", "a") as file:
            tabla.to_csv(file, header=file.tell()==0, index=False)
        self.lista_equipos.append(equipo)
    def inicio(self):
        opc1="0"
        while opc1 not in ["1","2"]:
            print("MENÚ")
            print("1. Ingresar a torneo creado (Cargar información)")
            print("2. Crear nuevo torneo (Nueva información)")
            opc1=input("Seleccione la opción: ")
            os.system('cls')
            if opc1.isdigit():
                if opc1 == "1":
                    pass
                elif opc1 == "2":
                    opc2="0"
                    while opc2 not in ["1","2","3","4","5"]:
                        print("MENÚ")
                        print("1. Ingresar equipo y sus jugadores")
                        print("2. Crear carnés de cancha")
                        print("3. Crear cronograma")
                        print("4. Definir resultados de partidos")
                        print("5. Consultar tabla de posiciones")
                        opc2=input("Seleccione la opción: ")                 
                        if opc2.isdigit():
                            if opc2=="1":
                                if len(self.lista_equipos) == 6:
                                    print("¡ERROR! No pueden haber más de seis equipos")
                                    opc2="0"
                                else:
                                    self.ingresar_equipo()
                                    opc2="0"
                            elif opc2=="2":
                                opc2=self.comprobar_faltan_equipos()
                                if(opc2=="2"):#EXISTEN 6 EQUIPOS
                                    self.imprimir_carnes()
                                    opc2=0
                            elif opc2=="3":
                                opc2=self.comprobar_faltan_equipos()
                                self.crear_cronograma()
                            elif opc2=="4":
                                opc2=self.comprobar_faltan_equipos()
                            elif opc2=="5":
                                opc2=self.comprobar_faltan_equipos()
                            else:
                                print("INGRESO INCORRECTO")
                        else:
                            opc2="0"
                            print("¡ERROR EN EL INGRESO!")
                else:
                    opc1=False
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
        while opc1!="s" or opc1!="n":
            opc1=str(input("¿Está de acuerdo?(s/n)"))
            if opc1 == "s":
                equipo=Equipo(equ_nombre, equ_telefono)
                self.guardar_equipo_csv(equipo)
                self.ingresar_jugadores(equipo)
                break
            elif opc1=="n":
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
            while opc2!="s" or opc2!="n":
                opc2=str(input("¿Está de acuerdo?(s/n)"))
                if opc2 == "s":
                    jugador=Jugador(jug_nombre, jug_apellido, jug_id, jug_nivel, equipo.nombre)
                    self.guardar_jugador_csv(jugador)
                    break
                elif opc2=="n":
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
        #CREAR GRUPOS
        lista=self.lista_equipos
        random.shuffle(lista)
        grupo_a=self.lista_equipos[:3]
        self.grupo_a=grupo_a
        grupo_b=self.lista_equipos[3:]
        self.grupo_b=grupo_b
        print("")
        print("GRUPO A:")
        for equipo_a in grupo_a:
            print(equipo_a.nombre)
        print("GRUPO B:")
        for equipo_b in grupo_b:
            print(equipo_b.nombre)
        #CREAR CRONOGRAMA
        emparejamientos_a=[[grupo_a[0].nombre,grupo_a[1].nombre],[grupo_a[0].nombre,grupo_a[2].nombre],grupo_a[1].nombre,grupo_a[2].nombre]
        emparejamientos_b=[[grupo_b[0].nombre,grupo_b[1].nombre],[grupo_b[0].nombre,grupo_b[2].nombre],grupo_b[1].nombre,grupo_b[2].nombre]
        campeonato=[]
        fecha_inicio="7/11/19"
        fecha=datetime.strptime(fecha_inicio, "%d/%m/%y")
        for i in range(3):
            campeonato.append(["A",emparejamientos_a[i],fecha])
            campeonato.append(["B",emparejamientos_b[i],fecha])
            fecha=fecha+timedelta(days=7)
        df=pandas.DataFrame(campeonato, columns=["Grupo","Partido","Día"])
        df


torneo = Campeonato()
torneo.inicio()       
