import csv
import numpy as np
from ClaseCamas import cama
class ManejadorCamas:
    __arreglo=np.empty(3,dtype=cama)
    __dimension=0
    __cantidad=0
    __incremento=3
    def __init__(self,dimension,incremento=3):
        self.__arreglo=np.empty(dimension,dtype=cama)
        self.__cantidad=0
        self.__dimension=dimension
    def agregar_cam(self,unacama):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=unacama
        self.__cantidad+=1
    def cargar_objetos(self):
        archivo=open("camas.csv")
        reader=csv.reader(archivo,delimiter=";")
        next(reader,None)
        for fila in reader:
            c=cama(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.agregar_cam(c)
        archivo.close()
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreglo[i])
    def busca(self,nombreap):
        i=0
        while i<self.__cantidad and self.__arreglo[i].get_nom() != nombreap:
            i+=1
        if i < self.__cantidad:
            return i
        else:
            return -1
    def alta(self,fecha,pos):
        self.__arreglo[pos].set_alta(fecha)
    def get_id(self,pos):
        return self.__arreglo[pos].get_cama()
    def ct(self):
        return self.__cantidad
    def muestra_paciente(self,pos):
        print("\nPaciente: {}\t\t Cama: {}\t\t Habitacion: {}".format(self.__arreglo[pos].get_nom(),self.__arreglo[pos].get_cama(),self.__arreglo[pos].get_habitacion()))
        print("Diagnostico: {}\t\t Fecha de internacion: {}".format(self.__arreglo[pos].get_diag(),self.__arreglo[pos].get_internacion()))
        print("Fecha de alta: {}".format(self.__arreglo[pos].get_fecha_alt()))
    def listado_internados(self):
        diag=input("Ingrese un diagnostico: ")
        print("Pacientes internados con el diagnostico ingresado")
        for i in range(self.__cantidad):
            if self.__arreglo[i].get_diag() == diag and self.__arreglo[i].get_estado() == True:
                print(self.__arreglo[i])
            else:
                print("El paciente {} no posee el diagnostico ingresado o esta dado de alta...".format(self.__arreglo[i].get_nom()))