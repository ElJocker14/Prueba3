import random
import os
os.system("cls")
nombre = ""
edad = ""
NIF = ""
valor = ""


persona = []


def buscar():
    NIF = input('ingresa el nif de la persona a buscar')
    for personas in persona:
        if persona['NIF'] == NIF:
            print('informacion de la persona')
            return


def salir():
    print("Pablito espero mi 7 version 7.0")


def grabar():
    nombre = str(input("cual es tu nombre "))

    if nombre == '':
        print("nombre invalido")

    edad = int(input("cual es tu edad "))
    if edad > 15:
        NIF = input('ingresa su NIF')
        print('nif invalido')
        NIF == ''
    else:
        if edad < 15:
            print('no es necesaria tu nif ')
            NIF = ''
            return


personas = {
    "nombre": nombre,
    "edad": edad,
    "NIF": NIF

}

persona.append(personas)


def imprimir_certificados():
    NIF = input("ingrese los datos para inporimir certificado")
    for persona in persona:
        if persona["NIF"] == NIF:
            certificados = {
                "nacimiento ": random.randint(1500, 5000),
                "estado conyugal": random.randit(1500, 5000),
                "perteneciente a la union europea": random.randit(1500, 5000)
            }


while True:
    print("bienvenidos")
    print("------menu------")
    print("1.grabar\n , .buscar\n , 3.imprimir_certificados\n , 4. salir\n")
    opcion = 0

    opcion = int(input("ingrese una opcion"))
    if opcion == 1:
        grabar()

    elif opcion == 2:
        buscar()
    elif opcion == 3:
        imprimir_certificados()

    elif opcion == 4:
        salir()
        break
    else:
        print("opcion no valida")
