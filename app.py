import random
import json
import funciones 

intentos = 5
aciertos = []
errores = []
encontrado = False
palabraIngresada = ""
tiempoInicio = 0
tiempoFin = 0
listaRanking = []

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

                datos = {
                    'Nombre': nombre,
                    'Tiempo': tiempoFin
                    }

                with open('ranking.json','a') as f:
                    json.dump(datos, f, sort_keys=True)

        #        def escribeJson(data, filename="ranking.json"):
       #             with open(filename, 'w') as f:
      #                  json.dump(data, f, indent=4)
                
     #           with open("ranking.json") as json_file:
    #                data = json.load(json_file)
   #                 temp = data ["RANKING"]
  #                  y = {"Nombre": nombre, "Tiempo": tiempoFin}
 #                   temp.append(y)

#                write_json(data)

                print("Felicidades " + nombre + " acava de ganar el juego en " + str(tiempoFin) + " segundos")

                print(datos)

                if __name__=='__app__':
                    ruta='ranking,json'
                    rankingOrden(ruta)

                print(ranking.json())

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

                print(nombre + "Acava de ganar el juego en " + tiempoFin + " tiempo")

                print("El datos quedaria: ")

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