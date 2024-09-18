

class Alumno:
    def __init__(self):
        
        self.nombre = "sin nombre"
        self.apellido = "sin definir"

    def __str__(self):
        return self.nombre + " " + self.apellido