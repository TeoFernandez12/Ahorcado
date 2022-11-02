
from distutils.log import error
from random import random
import random
import json

#Carga de variables
intentos = 3
aciertos = []
errores = []
encontrado = False
palabraIngresada = ""

#Ingreso de Nombre
nombre = input("ingrese su nombre: ")

#Ingreso de variables. Carga de palabras
#palabras = ["GATO", "MOSCA", "CAFE", "MERMELADA", "LAMPARA", "ESCRITORIO", "IMPRESORA","ENCHUFE", "CAJA", "ESTUFA", "PERRO"]

with open('palabras.json', 'r') as f:
  palabras = json.load(f)

palabraSeleccionada = random.choice(palabras).upper()#Selecciona palabra random
letras = len(palabraSeleccionada)
print(palabraSeleccionada)


#CARGA DE FUNCIONES
#guarda los aciertos
def imprimirResultado(aciertos2):#
    resultado2 = ""
    for letra2 in aciertos2:
        resultado2 = resultado2 + letra2
    print(resultado2)

#Valida que la letra ya fuè ingresada
def buscarEnLista(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False

#Arriesga la palabra
def ArriesgaPalabra():#Arriesga Palabra
    for arriesgar in palabras:
        if arriesgar == palabras:
            return True
    return False


for num in range(0, letras):
    aciertos.append("_")#Pone los "_" en los arrays

print("Hola " + nombre + ", tu palabra tiene " + str(letras) + " letras")

#While carcula las vidas
while len(errores) <= intentos:
    #ingreso de letra
    letraIngresada = input("\n\ningresa una letra o precione 1 para arriesgar: ").upper()

    print(letraIngresada)

    #Compara la letra ingrsada
    if letraIngresada == "1":
            
        palabraIngresada = input("Escriba una palabra: ").upper()
    
        #fin del juego
        if palabraIngresada == palabraSeleccionada:
            print("\nFelicitaciones " + nombre + " ganaste el juego!!! Tu palabra era: " + palabraSeleccionada)
        else:
            print ("\nPErdiste!!! La palabra era " + palabraSeleccionada)
        quit()

    #Comprueba la valides de la letra
    if len(letraIngresada) == 1 or ~ letraIngresada.isnumeric():

        #inicializa el histrial en 0
        index = 0

        encontrado = buscarEnLista(aciertos,letraIngresada)

        #Indica que la letra no es valida, y la guarda en una lista
        if encontrado == False:
            encontrado = buscarEnLista(errores, letraIngresada)

        #If arriesgar
        if letraIngresada == "1":
            arriesgar = input("\n\nIngrese una palabra para arriesgar: ").upper()
        
            if arriesgar == palabraSeleccionada:
                print(nombre + "Acava de ganar el juego")

        #Indica que la letra ya fue ingresada antes    
        if encontrado:
            print("La letra " + letraIngresada + " ya fue ingresada!!!" )

        else:

            #Compara la letra "True" con la palabra.
            for letra in palabraSeleccionada:
                if letra == letraIngresada:
                    encontrado = True
                    aciertos[index] = letra

                index = index + 1

            #Letras falsas            
            if encontrado == False:
                errores.append(letraIngresada)

                #Indica que perdiste el juego
                if len(errores) == intentos:
                    print(nombre + " ya tuviste 3 errores. Perdiste el juego.\nTu palabra era: " + palabraSeleccionada + "\n")
                    quit()
                else:
                    print("La letra " + letraIngresada + " no existe")
                    
                    vidas = intentos - len(errores)
                
                #Indica las cantidad de vidas que le quedn al jugador.
                if vidas >= 2:
                    print("Te quedan " +  str(vidas) + " intentos")
                else:
                    print("Te queda " +  str(vidas) + " intento")

            #Indica que la letra es correcta
            else:
                print("La letra " + letraIngresada + ", es correcta")
                imprimirResultado(aciertos)

                if len(aciertos) == len(palabraSeleccionada):
                    print("Felicitaciones " + nombre + " acava de ganar el juego")
            
    #hola
    #Dato no valido
    else:
        DatoNoValido = intentos + 1
        print("Dato ingresado no válido !!!!")

#Falata:Terminar el juego al completar la palabra.

#GASTE EL JUEGO
#if arriesgar == palabraSeleccionada or aciertos != "_":
#if arriesgar == palabraSeleccionada or aciertos("_") == False:
#if arriesgar == palabraSeleccionada or aciertos("_") == palabraSeleccionada:
#if aciertos != "_":