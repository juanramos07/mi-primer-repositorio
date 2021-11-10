class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def viajando(self):
        print("viajando")



class empleado(persona):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def trabajar(self):
        print("trabajando")

    def principiante(self, other):
        other.__class__ = empleado


juan = persona("juan", 25)
juan.viajando()
print(type(juan))
jose = empleado("jose", 23)
jose.trabajar()

jose.principiante(juan)
print(type(juan))

