from collections import defaultdict, deque

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
        for result in self.prolog.query(
                f"setof(X,A^B^C^D^E^F^(actividad(A,lugar({provincia},X),B,C,D,E,F);lugar({provincia},X)),L)"):
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

    def get_actividades(self, ciudad, lugar, datetime, costo, tipos, calificaciones):
        if datetime is None:
            return []
        query = f"actividad(Nombre,lugar({ciudad},\"{lugar}\"),Tipo,Costo,date({datetime.year},{datetime.month},{datetime.day}),tiempo({datetime.hour},{datetime.minute}),Calificacion)"
        return self.__query_(query, costo, tipos, calificaciones)

    def get_otro_tipos(self):
        for result in self.prolog.query("setof(X,A^B^C^D^E^F^actividad(A,B,X,C,D,E,F),L)"):
            return [str(i) for i in result['L']]

    def get_restaurantes(self, ciudad, lugar, datetime, costo, tipos, calificaciones):
        if datetime is None:
            return []
        query = f"restaurante(Nombre, lugar({ciudad},\"{lugar}\"), Tipo, Costo, date({datetime.year},{datetime.month},{datetime.day}), tiempo({datetime.hour},{datetime.minute}), Calificacion)"
        return self.__query_(query, costo, tipos, calificaciones)

    def get_restaurante_tipos(self):
        for result in self.prolog.query("setof(X,A^B^C^D^E^restaurante(A,B,X,C,D,[],E),L)"):
            return [str(i) for i in result['L']]