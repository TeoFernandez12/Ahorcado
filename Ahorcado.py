from distutils.log import error
from random import random
import random

nombre = input("ingrese su nombre: ")
intentos = 3
palabras = ["GATO", "MOSCA", "CAFE", "MERMELADA", "LAMPARA", "ESCRITORIO", "IMPRESORA"]
seleccion = random.choice(palabras).upper()

print(seleccion)
letras = len(seleccion)

respuesta = []
for num in range(0, letras):
    respuesta.append("_")

print("Hola " + nombre + ", tu palabra tiene " + str(letras) + " letras")

errores = 0 

while errores <= intentos:

    letraIngresada = input("ingresa una letra: ").upper()

    print(letraIngresada.isnumeric())

    if len(letraIngresada) == 1 & ~ letraIngresada.isnumeric():

        encontrado = False
        index = 0

        for letra in seleccion:
            if letra == letraIngresada:
                encontrado = True
                respuesta[index] = letra
            index = index + 1

        if encontrado == False:
            errores = errores + 1

            if errores == intentos:
                print(nombre + " ya tuviste " + str(errores) + " errores. Perdiste el juego")
                quit()
            else:
                print("La letra " + letraIngresada + " no existe")

                vidas = intentos - errores

                if vidas >= 2:
                    print("Te quedan " +  str(vidas) + " intentos")
                else:
                    print("Te queda " +  str(vidas) + " intento")

        else:
            print(letraIngresada + " es correcta")
            print (respuesta)

            for index in respuesta:
                texto = respuesta.replace()

    else:
        print("Dato ingresado no válido !!!!")

