import csv

from ClaseMedicamentos import medicamento
class ManejadorMedicamentos:
    __lista : list[medicamento]
    def __init__(self):
        self.__lista=[]
    def cargarlista(self):
        archivo=open("medicamentos.csv")
        reader=csv.reader(archivo,delimiter=";")
        next(reader,None)
        for fila in reader:
            m=medicamento(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            self.__lista.append(m)
        archivo.close()
    def mostrar (self):
        for elemento in self.__lista:
            print (elemento)
    def get_lista(self):
        return self.__lista
    def listado(self,id):
        acum=0
        print("Medicamento/Monodroga\t Presentacion\t\tCantidad\t\tPrecio\n")
        for i in range(len(self.__lista)):
            if self.__lista[i].get_idcam() == id:
                print("{}/{}\t{}\t\t\t{}\t\t\t{} $ ".format(self.__lista[i].get_nom(),self.__lista[i].get_mono(),self.__lista[i].get_pres(),self.__lista[i].get_ct(),self.__lista[i].get_precio()))
                acum+=self.__lista[i].get_precio()
        print("Total adeudado: --{}--".format(acum))
