#Hecho en Python 3.9, compatible con python 3.5+
from pyswip import Prolog
from tkinter import *

prolog = Prolog()
prolog.consult('final.pl')

def main():
    ventana = Tk()
    ventana.title("Planeamiento de Rutas")
    ventana.minsize(800, 600)
    ventana.mainloop()

# __name__ es una variable global del archivo, esto es para verificar
# si es el archivo que se llama en la corrida, ya que a correr
# un archivo con Python (python App.py) ejecuta el programa setteando
# el __name__ como __main__
if __name__ == "__main__":
    for c in prolog.query("interes(X)"):
        print(c)
    main()