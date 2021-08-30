from collections import defaultdict, deque

import pyswip.easy
from pyswip import Prolog


def parse_prolog(string):
    return " ".join(string.split("_")).title()


def parse_text(string):
    return "_".join(string.lower().split(" "))


class Controlador:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult('final.pl')

    def get_provincias(self):
        for result in self.prolog.query("setof(X,Y^lugar(X,Y),L)"):
            return defaultdict(lambda: None, {parse_prolog(str(i)): str(i) for i in result['L']})

    def get_lugares(self, provincia):
        for result in self.prolog.query(f"setof(X,lugar({provincia},X),L)"):
            listado = [i.decode("utf-8") for i in result['L']]
            return listado

    def __query_(self, og_query, costo, tipos, calificaciones):
        query = og_query
        if costo is not None:
            query += f",Costo=<{costo}"
        if len(tipos) > 0:
            query += f",member(Tipo,[{','.join(tipos)}])"
        else:
            return []
        if len(calificaciones) > 0:
            query += f",member(Calificacion,[{','.join(calificaciones)}])"
        else:
            return []
        return [i for i in self.prolog.query(query)]

    def __query_2(self, og_query, costo, calificaciones, porcentaje, min, max):
        query = og_query
        if costo is not None:
            query += f",Costo=<{costo}"
        if max is not None:
            query += f",Costo=<{max}"
        if min is not None:
            query += f",Costo>={min}"
        if porcentaje is not None and costo is not None:
            query += f",Costo=<{(int(costo) * porcentaje)/100}"
        if len(calificaciones) > 0:
            query += f",member(Calificacion,[{','.join(calificaciones)}])"
        else:
            return []
        return [i for i in self.prolog.query(query)]

    def get_actividades(self, provincia, lugar, datetime, costo, tipos, calificaciones):
        if datetime is None:
            return []
        query = f"actividad(Nombre,lugar({provincia},\"{lugar}\"),Tipo,Costo,date({datetime.year},{datetime.month},{datetime.day}),tiempo({datetime.hour},{datetime.minute}),Calificacion)"
        return self.__query_(query, costo, tipos, calificaciones)

    def get_otro_tipos(self):
        for result in self.prolog.query("tipos_de_otros(L)"):
            return [str(i) for i in result['L']]

    def get_restaurantes(self, provincia, lugar, datetime, costo, tipos, calificaciones):
        if datetime is None:
            return []
        query = f"restaurante(Nombre, lugar({provincia},\"{lugar}\"), Tipo, Costo, date({datetime.year},{datetime.month},{datetime.day}), tiempo({datetime.hour},{datetime.minute}), Calificacion)"
        return self.__query_(query, costo, tipos, calificaciones)

    def get_bares(self, ciudad, lugar, datetime, costo, calificaciones, porcentaje, min, max):
        if datetime is None:
            return []
        query = f"bar(Nombre, lugar({ciudad},\"{lugar}\"), Costo, Calificacion, date({datetime.year},{datetime.month},{datetime.day}), tiempo({datetime.hour},{datetime.minute}))"
        return self.__query_2(query, costo, calificaciones, porcentaje, min, max)

    def get_restaurante_tipos(self):
        for result in self.prolog.query("tipos_de_restaurantes(L)"):
            return [str(i) for i in result['L']]

    def get_cines(self, provincia, lugar):
        for result in self.prolog.query(f"cines(L,lugar({provincia},\"{lugar}\"))"):
            return [{'nombre': i.args[0].decode('utf-8'), 'calif': i.args[2]} for i in result['L']]
        return []

    def get_generos_pelicula(self):
        for result in self.prolog.query("generos_de_peliculas(L)"):
            return [str(i) for i in result['L']]

    def get_cines_disponibles(self, provincia, calificaciones, presupuesto, datetime, lugar, generos):
        if len(generos) == 0:
            return []
        if len(calificaciones) == 0:
            return 0
        if presupuesto is None:
            presupuesto = 'inf'
        for result in self.prolog.query(
                f"cines_disponibles(L,lugar({provincia},\"{lugar}\"),[{','.join(calificaciones)}] ,{presupuesto},date({datetime.year},{datetime.month},{datetime.day}), tiempo({datetime.hour},{datetime.minute}), [{','.join(generos)}])"):
            datos = [{'nombre': i.args[0].decode('utf-8'), 'calif': i.args[2]} for i in result['L']]
            return datos
        return []

    def get_peliculas_disponibles_cine(self, nombre_cine, provincia, lugar, calificaciones, presupuesto, datetime,
                                       generos):
        q_lugar = f"lugar({provincia},\"{lugar}\")"
        if len(calificaciones) == 0:
            return 0
        if presupuesto is None:
            presupuesto = 'inf'
        for result in self.prolog.query(
                f"weekday(date({datetime.year},{datetime.month},{datetime.day}),Weekday),peliculas_de_cine(cine(\"{nombre_cine}\",{q_lugar},_),Peliculas,[{','.join(calificaciones)}],{presupuesto},Weekday,tiempo({datetime.hour},{datetime.minute}),[{','.join(generos)}])"):
            return [i.args for i in result['Peliculas']]
