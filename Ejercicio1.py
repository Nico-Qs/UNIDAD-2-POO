'''''
Defina una clase “Email” con los siguientes atributos: idCuenta, dominio, tipo de dominio y contraseña (todos estos datos se ingresan por teclado). Y los siguientes métodos:

a- El constructor.

b- Método “retornaEmail()” que construye una dirección e-mail con los valores de los atributos de Email. Por ejemplo:

idCuenta.: alumnopoo

dominio: gmail

tipoDominio: com

Resultado devuelto por retornaEmail: alumnopoo@gmail.com

c- Método “getDominio()”, que retorna el dominio.

d- Método “crearCuenta(), crea una cuenta a partir de una dirección de correo que recibe como parámetro.

Implemente un programa que permita:

1- Ingresar el nombre de una persona y de su cuenta de correo, el identificador de cuenta, dominio y tipo de dominio (crear una instancia de la clase Email) y luego imprima el siguiente mensaje:

Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.

2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña y realizar la modificación correspondiente.

3- Crear un objeto de clase Email, a partir de una dirección de correo, por ejemplo: informatica.fcefn@gmail.com, juanLiendro1957@yahoo.com, etc.

4- Leer de un archivo separado por comas 10 direcciones de e-mail, crear instancias de la clase Email; luego ingresar un identificador de cuenta e indicar si está repetido o no.
'''
import csv
class Email:
    idCuenta= ""
    dominio  = ""
    tip_dom = ""
    contraseña = ""
    def __init__(self,id,dom,tipdom,contra):
        self.idCuenta=id
        self.dominio=dom
        self.tip_dom=tipdom
        self.contraseña=contra
    def retornarEmail(self):
        return(self.idCuenta+"@"+self.dominio+"."+self.tip_dom)
    def getDominio(self):
        return (self.dominio)
    def crearCuenta(self,correo):
        adr=correo.split("@")
        tip=adr[1].split(".")
        self.idCuenta=adr[0]
        self.dominio=tip[0]
        self.tip_dom=tip[1]


def modifica_contra(actual,oldpass):
        if actual == oldpass:
            actual=input("Ingrese nueva contraseña:")
            print("Su contraseña se modifico a: "+actual)
            return actual
        else:
            print("Contraseña incorrecta")
def funcion4(adress):
    lista=[]
    for i in range(len(adress)):
        ad=Email("","","","")
        ad.crearCuenta(adress[i])
        lista.append(ad) 
    busca = input("Ingrese ID a buscar:")
    b=0
    for ad in lista:
        #print(ad.retornarEmail()) 
        if  ad.idCuenta == busca:
            b=1
    if b==1:
        print ("El ID ingresado se encuentra repetido")
    else: 
        print ("No se encuentra el ID ingresado")
if __name__ == '__main__':
    nom = input("Ingrese su nombre:")
    p = Email(input ("Ingrese su ID:"),input ("Ingrese su dominio:"),input ("Ingrese su tipo de dominio:"),input ("Ingrese su contraseña:"))
    print("Estimado "+nom+" te enviaremos tus mensajes a la direccion "+p.retornarEmail())
    p.contraseña=modifica_contra(input("Ingrese contraseña actual"),p.contraseña)
    corr=Email("","","","")
    corr.crearCuenta(input("Ingrese su correo:"))
    print(corr.retornarEmail())
    archi = open("Texto.txt")
    direcciones = archi.read().split(",")
    with open("Correos.csv","r") as archivo:
        direcciones = archivo.read().split(",")
        funcion4(direcciones) 
        archivo.close()