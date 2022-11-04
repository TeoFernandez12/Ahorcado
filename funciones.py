import calendar
import json
import time
from app import *

def obtenerTiempo():
  current_GMT = time.gmtime()
  time_stamp = calendar.timegm(current_GMT)
  return  time_stamp

def imprimirResultado(aciertos2):#
    resultado2 = ""
    for letra2 in aciertos2:
        resultado2 = resultado2 + letra2
    print(resultado2)

def buscarEnLista(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False
