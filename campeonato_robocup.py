class Jugador:
    def __init__(self, nombre, apellido, id, nivel, equipo):
        self.nombre=nombre
        self.apellido=apellido
        self.nivel=nivel
        self.id=id
        self.equipo=equipo
    
jugador = Jugador("Anthony", "Cabrera", 1, "Primero", "FCB")
print(jugador.equipo)
        
