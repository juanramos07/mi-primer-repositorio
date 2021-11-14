
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
        print("estatura: ",self.estatura,"m")
        print("peso: ",self.peso)
    def getnombre(self):
        return self.nombre

class Empleado(Persona):
    def __init__(self,nombre,edad,estatura,peso,genero,sueldo,antiguedad):
        super().__init__(nombre, edad, estatura, peso, genero)
        self.sueldo = sueldo
        self.antiguedad = antiguedad

    def trabajar(self):
        print("trabajando")

    def principiante(self, other):
        other.__class__ = empleado

class Gerente(Empleado):
    def __init__(self, nombre,edad,estatura,peso,genero,sueldo,antiguedad,presupuesto = 36500):
        super().__init__(nombre,edad,estatura,peso,genero,sueldo,antiguedad)
        self.__presupuesto = presupuesto
    def getpresupuesto(self):
        print("el presupuesto es: ",self.__presupuesto)

    def cambiarpresupuesto(self,nuevopres:int):
        self.__presupuesto = nuevopres






