
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
        print("estatura: ",self.estatura,"mts")
        print("peso: ",self.peso)
    def trabajar(self):
        print(self.nombre,"trabajando")
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


class Empleado(Persona):
    def __init__(self,nombre,edad,estatura,peso,genero,sueldo,antiguedad):
        super().__init__(nombre, edad, estatura, peso, genero)
        self.__sueldo = sueldo
        self.__antiguedad = antiguedad

    def trabajar(self):
        print("trabajando")


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
    def __init__(self, nombre,edad,estatura,peso,genero,sueldo,antiguedad,presupuesto = 36500):
        super().__init__(nombre,edad,estatura,peso,genero,sueldo,antiguedad)
        self.__presupuesto = presupuesto
    #getters
    def getpresupuesto(self):
        print("el presupuesto es: ",self.__presupuesto)
    #setters
    def cambiarpresupuesto(self,nuevopres:int):
        self.__presupuesto = nuevopres

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
    def __init__(self,saco,pantalones,camisa,corbata):
        super().__init__()
        #datos por defecto
        self.saco="negro"
        self.pantalones="negros"
        self.camisa = "blanca"
        self.corbata ="negra"

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







