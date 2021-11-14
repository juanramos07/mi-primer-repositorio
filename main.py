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

# escenario del gerente entrevistando a la persona interesada en la vacante
print("Nos contextualizamos en la oficina del gerente entrevistando a la persona")
gerente.hablar("Buenas tardes, ¿como se llama?")
#se crea objeto
persona2=Ce.Persona()
npersona2=input(("Mi nombre es: "))
persona2.setnombre(npersona2)
gerente.hablar("Bien , ahora empezaremos con las preguntas")
gerente.hablar("Hablame de ti")
print("")
print("Respuestas posibles a esta pregunta"
      "\n1)responder haciendo un resumen de la historia de mi carrera"
      "\n2)contar mis aspiraciones de carrera a largo plazo"
      "\n3)reponder con la oportunidad en cuestión, observando cómo puedo agregarle valor a la organización")

op1= int(input("elija la opcion que tenga pensado en mente: "))

gerente.hablar("¿Por qué te interesa trabajar en esta empresa?")
print("Respuestas posibles a esta pregunta"
      "\n1)responder el interes de la oportunidad"
      "\n2)responde der acuerdo a una investigación previa sobre la empresa, demostrando interese por la organizacion")

op2= int(input("elija la opcion que tenga pensado en mente: "))

gerente.hablar("¿Me puedes describir tus fortalezas?")
print("Respuestas posibles a esta pregunta"
      "\n1) decir fortalezas en las habilidades exigidas para el cargo"
      "\n2)contar como mis fortalezas ayudaron en otro trabajo "
      "\n3)describir como mis fortalezas en mi exito profesional")

op3= int(input("elija la opcion que tenga pensado en mente: "))

gerente.hablar("¿Cuáles son tus principales debilidades?")
print("Respuestas posibles a esta pregunta"
      "\n1)trabajo demasiado"
      "\n2)siempre apunto muy alto "
      "\n3)siempre duermo con mi despertador y lucho para comenzar a trabajar todos los días")

op4= int(input("elija la opcion que tenga pensado en mente: "))

gerente.hablar("¿Cómo te ves en cinco años?")
print("Respuestas posibles a esta pregunta"
      "\n1)mi plan es estar en una playa en Bali"
      "\n2)espero estar realizando mi propio negocio "
      "\n3)aportando en los objetivos organizacionales de la empresa")

op5= int(input("elija la opcion que tenga pensado en mente: "))

gerente.contratar(op1,op2,op3,op4,op5)



