class ViajeroFrecuente:
    __num_viajero= ""
    __dni= ""
    __nombre=""
    __apellido= ""
    __millas_acum=""
    def __init__(self,numviaj,DNI,nombre,apellido,millacum):
        self.__num_viajero=int(numviaj)
        self.__dni=DNI
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=int(millacum)
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    def acumularMillas (self,cant):
        self.__millas_acum+=cant
        return self.__millas_acum
    def  canjearMillas(self,ct_canje):
        if ct_canje <= self.__millas_acum:
            self.__millas_acum-=ct_canje
            return self.__millas_acum
        else:
            return print ("Error en la operacion")
    def getNumViajero(self):
        return self.__num_viajero
    def mostrar(self):
        print("{}, {}, {}, {}, {}".format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum))
    def __gt__(self, other):
        if self.__millas_acum > other:
            return True
        else:
            return False
    def __radd__(self, other):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum+other)
    def __rsub__(self, other):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum-other)
    def __eq__(self, other) -> bool:
        if  (type(other)==ViajeroFrecuente):
            return  self.__millas_acum == other.__millas_acum
        elif (type(other)==int):
            return  self.__millas_acum == other


