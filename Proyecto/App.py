#Hecho en Python 3.9, compatible con python 3.5+
import time

from pyswip import Prolog
from visual.VentaPrincipal import VentaPrincial
from apis.restaurante import get_restaurante

prolog = None

def init():
    global prolog
    prolog = Prolog()
    prolog.consult('final.pl')

# __name__ es una variable global del archivo, esto es para verificar
# si es el archivo que se llama en la corrida, ya que a correr
# un archivo con Python (python App.py) ejecuta el programa setteando
# el __name__ como __main__
if __name__ == "__main__":
    init()
    principal = VentaPrincial(prolog)