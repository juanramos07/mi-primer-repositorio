import clasesempresa as Ce
#persona busca al gerente
print("la persona entra a la empresa buscando al Carlos")
# se crea el objeto de la persona
persona1=Ce.Persona()
persona1.hablar(print("Buenas tardes,busco a una persona"))
asistente= Ce.Empleado()
asistente.hablar("¿Como se llama usted?")
myname=input("escriba su nombre: ")
print("asistente anota el nombre de la persona")
persona1.setnombre(myname)
asistente.hablar("¿A quien busca?")
pbuscado= input("escriba el nombre de la persona que busca: ")

#se crea objeto gerente
gerente=Ce.Gerente()
gerente.setnombre(pbuscado)
(gerente.entrevistar())


