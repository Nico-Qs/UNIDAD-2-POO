"""
Sobrecarga de operadores

Dada la clase ViajeroFrecuente definida en el ejercicio 2, resolver lo siguiente:

1-    Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos ViajeroFrecuente cuál posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en python).

2-    Acumular millas usando la sobrecarga del operador binario suma(+), obteniendo como resultado de la suma una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de acumular millas se resuelve de la siguiente forma v = v + 100.

3-    Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de canjear millas se resuelve de la siguiente forma v = v - 100.
"""
import csv
from ClaseViajeroFrecuente import ViajeroFrecuente
def funcion1(lista):
    maxx=-1
    for i in range(len(lista)):
        if lista[i] > maxx:
            maxx=lista[i].cantidadTotaldeMillas()
    print("APARTADO --1--")
    print("Viajeros con mayor millas acumuladas")
    for i in range(len(lista)):
        if lista[i].cantidadTotaldeMillas() == maxx:
            lista[i].mostrar()
def funcion2_3(lista):
    print("--APARTADO 2 Y 3--")
    viajero=lista[0]
    viajero.mostrar()
    viajero+=1000
    print("Se acumulan nuevas millas")
    viajero.mostrar()
    print("Se realiza un canje de millas")
    viajero-=2500
    viajero.mostrar()
if __name__ == "__main__":
    archivo = open("Viajeros.csv")
    reader = csv.reader(archivo, delimiter=",")
    lista = []
    next(reader)
    for fila in reader:
        p = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
        lista.append(p)
    funcion1(lista)
    funcion2_3(lista)