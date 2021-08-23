import requests
from json import *


def get_restaurante(ll=None):
    url = "https://www.menu.com.do/api/v1/businesses/search.json"
    parametros = {
        "query": "a:*" if ll is None else f"ll:{ll}",
        "limit": 25,
        "offset": 0
    }
    request = requests.get(url, parametros)
    respuesta = request.json()
    for i in respuesta['result']['Business']:
        print(i['vanity_name'])
        ver_restaurante(i['vanity_name'])
    # restaurante(nombre_vanidad, provincia)
    # categoria(nombre_vanidad, categoria)


def ver_restaurante(vanity_name):
    url = f"https://www.menu.com.do/api/v1/businesses/{vanity_name}.json"
    request = requests.get(url)
    respuesta = request.json()
    for menu in respuesta['result']['Menu']:
        get_menu(menu['id'],menu['business_id'])
    # menu(nombre_vanidad_restaurante, id)

def get_menu(id, business_id):
    url = f"https://www.menu.com.do/api/v1/menues/{id}.json"
    parametros = {
        "business_id": business_id
    }
    request = requests.get(url, parametros)
    respuesta = request.json()
    print(respuesta)
    # menu(nombre_vanidad_restaurante, id, plato, precio)
