#Hecho en Python 3.9, compatible con python 3.5+
import time

from pyswip import Prolog
from tkinter import *
from Grafo import dijkstra
from collections import defaultdict
from itertools import permutations

prolog = None

def main():
    ventana = Tk()
    ventana.title("Planeamiento de Rutas")
    ventana.minsize(800, 600)
    ventana.mainloop()

def init():
    global prolog
    start_time = time.time()
    prolog = Prolog()
    prolog.consult('final.pl')
    grafo = defaultdict(lambda: {})
    prolog_time = time.time()
    for arista in prolog.query('biarista(Desde,Hasta,Peso)'):
        grafo[arista['Desde']][arista['Hasta']]=arista['Peso']
    for desde, hasta in permutations(grafo.keys(), 2):
        path, peso = dijkstra(grafo, desde, hasta)
        prolog.asserta(f'camino({desde},{hasta},[{",".join(path)}],{peso})')
    finish_time = time.time()
    print(f'Prolog se inicio en {prolog_time-start_time}, el inicio total es {finish_time-start_time}')

# __name__ es una variable global del archivo, esto es para verificar
# si es el archivo que se llama en la corrida, ya que a correr
# un archivo con Python (python App.py) ejecuta el programa setteando
# el __name__ como __main__
if __name__ == "__main__":
    init()
    main()