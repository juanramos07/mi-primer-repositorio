
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
    def __init__(self,nombre):
        super().__init__()
        self.nombre = nombre
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
        self.nombre = "Ryo-Electronics"
        self.Nempleados= 1500
        self.giro = "comercial"
        self.producto = "Materiales para electronica"
    def Getnamempresa(self):
        return self.nombre

class Empleado(Persona,Empresa):
    def __init__(self,nombre):
        super().__init__(nombre)
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



class Gerente(Empleado,Vestimenta):
    def __init__(self,nombre):
        super().__init__(nombre)
        Vestimenta.__init__(self,saco,pantalones,camisa,corbata)
        self.__presupuesto = presupuesto
    #getters
    def getpresupuesto(self):
        print("el presupuesto es: ",self.__presupuesto)
    #setters
    def cambiarpresupuesto(self,nuevopres:int):
        self.__presupuesto = nuevopres

    def entrevistar(self):
        print("El gerente se llama",self.nombre,"en este momento el esta entrevistando a un candidato para una vacante en la empresa")
    def trabajar(self):
        print(self.nombre,"esta supervisando el area de markenting para las fechas del buen fin")











