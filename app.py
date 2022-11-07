import random
import json
import funciones 

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
    aciertos.append("_")

print("\nHola " + nombre + ", tu palabra tiene " + str(letras) + " letras")

tiempoInicio = funciones.obtenerTiempo()

while len(errores) <= intentos:

    letraIngresada = input("\ningresa una letra o precione 1 para arriesgar: ").upper()

    if letraIngresada == "1":
            
        palabraIngresada = input("Escriba una palabra: ").upper()
    
        if palabraIngresada == palabraSeleccionada:
            
                tiempoFin = funciones.obtenerTiempo() - tiempoInicio

                print("Felicidades " + nombre + " acava de ganar el juego en " + str(tiempoFin) + " segundos")

        else:
            print ("\nPErdiste!!! La palabra era " + palabraSeleccionada)
        quit()

    index = 0

    if len(letraIngresada) == 1 or ~ letraIngresada.isnumeric():        

        encontrado = funciones.buscarEnLista(aciertos,letraIngresada)

        if encontrado == False:
            encontrado = funciones.buscarEnLista(errores, letraIngresada)

        if letraIngresada == "1":
            arriesgar = input("\n\nIngrese una palabra para arriesgar: ").upper()

            if arriesgar == palabraSeleccionada:

                tiempoFin = funciones.obtenerTiempo() - tiempoInicio

                ranking = [nombre, tiempoFin]

                with open('rankingg.json','w') as f:
                    json.dump(ranking, f, sort_keys=True)

                print(nombre + "Acava de ganar el juego en " + tiempoFin + " tiempo")

                print("El ranking quedaria: ")

        if encontrado:
            print("La letra " + letraIngresada + " ya fue ingresada!!!" )

        else:

            for letra in palabraSeleccionada:
                if letra == letraIngresada:
                    encontrado = True
                    aciertos[index] = letra

                index = index + 1

            if encontrado == False:
                errores.append(letraIngresada)

                if len(errores) == intentos:
                    print(nombre + " ya tuviste 3 errores. Perdiste el juego.\nTu palabra era: " + palabraSeleccionada + "\n")
                    quit()
                else:
                    print("La letra " + letraIngresada + " no existe")
                    
                    vidas = intentos - len(errores)
                
                if vidas >= 2:
                    print("Te quedan " +  str(vidas) + " intentos")
                else:
                    print("Te queda " +  str(vidas) + " intento")

            else:
                print("La letra " + letraIngresada + ", es correcta")
                funciones.imprimirResultado(aciertos)

    else:
        DatoNoValido = intentos + 1
        print("Dato ingresado no válido !!!!")