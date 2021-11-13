import clasesempresa as Ce

# datos de persona
nombre = input("ingrese el nombre de la persona:")
genero = input("ingrese el genero de la persona:")
edad = int(input("ingrese la edad de la persona:"))
estatura = float(input("ingrese la estatura de la persona:"))
peso = float(input("ingrese el peso de la persona:"))

persona1=Ce.Persona(nombre,edad,estatura,peso,genero)
persona1.describir()
