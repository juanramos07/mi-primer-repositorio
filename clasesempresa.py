
class Persona:
    def __init__(self,nombre,edad,estatura,peso,genero = "x"):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def describir(self):
        print(" ")
        print("nombre: ",self.nombre)
        print("Genero : ",self.genero)
        print("Edad: ",self.edad)
        print("estatura: ",self.estatura)
        print("peso: ",self.peso)

class Gerente(persona):
    def __init__(self,nombre,edad,estatura,peso,genero,sueldo):
        super().__init__(nombre, edad, estatura, peso, genero)
        self.sueldo = sueldo

    def trabajar(self):
        print("trabajando")

    def principiante(self, other):
        other.__class__ = empleado

class Empleado(Gerente):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def viajando(self):
        print("viajando")





