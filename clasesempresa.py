
class Saco:
    def __init__(self):
        self.botones= 3
        self.ranuras=3
        self.bolsillo=False
    def getbotones(self):
        return self.botones
    def setbotones(self,nbotones):
        self.botones=nbotones

class Vestimenta(Saco):
    def __init__(self):
        super().__init__()
        #datos por defecto
        self.saco="negro"
        self.pantalones="negros"
        self.camisa = "blanca"
        self.corbata ="negra"
        self.zapatos = "negros"

    def getsaco(self):
        return self.saco

    def getpantalones(self):
        return self.pantalones
    def getcamisa(self):
        return self.camisa
    def getcorbata(self):
        return self.corbata

    def setsaco(self,setsa):
        self.saco= setsa
    def setpantalones(self,panta):
        self.pantalones = panta
    def setcamisa(self,nuecamisa):
        self.camisa = nuecamisa
    def setcorbata(self,nuevacorba):
        self.corbata= nuevacorba

class Persona(Vestimenta):
    def __init__(self):
        super().__init__()
        self.nombre = "Sin nombre"
        self.genero = "x"
        self.edad = 36
        self.estatura = 1.80
        self.peso = 80

    def describir(self):
        print(" ")
        print("nombre: ",self.nombre)
        print("Genero : ",self.genero)
        print("Edad: ",self.edad)
        print("estatura: ",self.estatura,"mts")
        print("peso: ",self.peso)

    def trabajar(self):
        print(self.nombre,"trabajando")

    def hablar(self,pregunta):
        print(pregunta)

    def vestir(self):
        print(self.nombre,"viste un saco",self.saco,"pantalones",self.pantalones,"y zapatos",self.zapatos)

    #getters
    def getnombre(self):
        return self.nombre
    def getgenero(self):
        return self.genero
    def getedad(self):
        return  self.edad
    def getestatura(self):
        return self.estatura
    def getpeso(self):
        return self.peso

    #setters
    def setnombre(self,n):
        self.nombre= n
    def setgener(self,g):
        self.genero= g
    def setedad(self,e):
        self.edad=e
    def setestatura(self,estatu):
        self.estatura= estatu
    def setpeso(self,pes):
        self.peso = pes


class Empresa:
    def __init__(self):
        self.nombreempresa = "Ryo-Electronics"
        self.Nempleados= 1500
        self.giro = "comercial"
        self.producto = "Materiales para electronica"
    def Getnamempresa(self):
        return self.nombreempresa

class Empleado(Persona,Empresa):
    def __init__(self):
        super().__init__()
        Empresa.__init__(self)
        self.__sueldo = 12000
        self.__antiguedad = 2

    def trabajar(self):
        print("trabajando en el area de ventas")

    #getters
    def getsueldo(self):
        return self.__sueldo
    def getantiguedad(self):
        return self.__antiguedad
    #setters
    def aumentarsueldo(self,porcentaje:int):
        self.__sueldo += (self.__sueldo * porcentaje)/100
    def setantiguedad(self,nant):
        self.__antiguedad = nant



class Gerente(Empleado):
    def __init__(self):
        super().__init__()
        self.presupuesto = 36000
    #getters
    def getpresupuesto(self):
        print("el presupuesto es: ",self.presupuesto)
    #setters
    def cambiarpresupuesto(self,nuevopres:int):
        self.presupuesto = nuevopres

    def entrevistar(self):
        print("El gerente se llama",Gerente.getnombre(self),"en este momento el esta entrevistando a un candidato para una vacante en la empresa")


    def trabajar(self):
        print(self.nombre,"esta supervisando el area de markenting para las fechas del buen fin")
    def contratar(self,r1,r2,r3,r4,r5):
        cal1=0
        cal2=0
        cal3=0
        cal4=0
        cal5=0
        if r1==3:
            cal1=1
        else:
            cal1=0
        if r2==2:
            cal2=1
        else:
            cal2=0
        if r3==1:
            cal3=1
        else:
            cal3=0
        if r4== 1 or 2:
            cal4=1
        else:
            cal4=0
        if r5==3:
            cal5=1
        else:
            cal5=0
        res=cal1+cal2+cal3+cal4+cal5
        if res== 5:
            print("Felicades estas contrado en la empresa",Empresa.Getnamempresa(self))
        else:
            print("Fue una agradable entrevista muy contundentes sus respuestas, nosotros le llamamos la siguiente semana para confirmarle")















