
import random
import json
import funciones as fnc

#Carga de variables
intentos = 3
aciertos = []
errores = []
encontrado = False
palabraIngresada = ""
tiempoInicio = 0
tiempoFin = 0

with open('palabras.json', 'r') as f:
  palabras = json.load(f)

nombre = input("\n\ningrese su nombre: ")
palabraSeleccionada = random.choice(palabras).upper()
letras = len(palabraSeleccionada)
print(palabraSeleccionada)

for num in range(0, letras):
    aciertos.append("_")#Pone los "_" en los arrays

print("\nHola " + nombre + ", tu palabra tiene " + str(letras) + " letras")

tiempoInicio = fnc.obtenerTiempo()

#While carcula las vidas
while len(errores) <= intentos:
    #ingreso de letra
    letraIngresada = input("\ningresa una letra o precione 1 para arriesgar: ").upper()

    #Compara la letra ingrsada
    if letraIngresada == "1":
            
        palabraIngresada = input("Escriba una palabra: ").upper()
    
        #fin del juego
        if palabraIngresada == palabraSeleccionada:

            
                tiempoFin = fnc.obtenerTiempo() - tiempoInicio

                print("Felicidades " + nombre + " acava de ganar el juego en " + str(tiempoFin) + " segundos")

        else:
            print ("\nPErdiste!!! La palabra era " + palabraSeleccionada)
        quit()

    index = 0

    #Comprueba la valides de la letra
    if len(letraIngresada) == 1 or ~ letraIngresada.isnumeric():        

        encontrado = fnc.buscarEnLista(aciertos,letraIngresada)

        #Indica que la letra no es valida, y la guarda en una lista
        if encontrado == False:
            encontrado = fnc.buscarEnLista(errores, letraIngresada)

        #If arriesgar
        if letraIngresada == "1":
            arriesgar = input("\n\nIngrese una palabra para arriesgar: ").upper()

            if arriesgar == palabraSeleccionada:

                tiempoFin = fnc.obtenerTiempo() - tiempoInicio

                ranking = [nombre, tiempoFin]

                with open('rankingg.json','w') as f:
                    json.dump(ranking, f, sort_keys=True)

                print(nombre + "Acava de ganar el juego en " + tiempoFin + " tiempo")

                print("El ranking quedaria: ")

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
                fnc.imprimirResultado(aciertos)

    else:
        DatoNoValido = intentos + 1
        print("Dato ingresado no válido !!!!")