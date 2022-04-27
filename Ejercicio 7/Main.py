""""
Sobrecarga por derecha (reverse operators)


Dada la clase ViajeroFrecuente definida en el ejercicio 2 con las sobrecargas de operadores solicitadas en el ejercicio 6, resolver lo siguiente:

1-    Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero a través de la sobrecarga del operador igual (== o __eq__). Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar tanto v ==  100 como 100 == v.

2-    Acumular millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 + v.

3-    Canjear millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 - v.
"""
import csv
from ClaseViajeroFrecuente import ViajeroFrecuente
if __name__ == "__main__":
    archivo = open("Viajeros.csv")
    reader = csv.reader(archivo, delimiter=",")
    lista = []
    next(reader)
    for fila in reader:
        p = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
        lista.append(p)
    v=lista[0]
    print("--Por izquierda--")
    print(v==2500)
    print("--Por derecha--")
    print(2500==v)
    print("Comparacion entre Objetos")
    print(v==lista[1])
    print("Entre otros objetos")
    print(v==lista[2])
    print("--APARTADO 2 Y 3--")
    v.mostrar()
    v=1000+v
    print("Se acumulan nuevas millas")
    v.mostrar()
    print("Se realiza un canje de millas")
    v=2500-v
    v.mostrar()
