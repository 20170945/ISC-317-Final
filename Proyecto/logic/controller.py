from collections import defaultdict

from pyswip import Prolog


def parse_prolog(string):
    return " ".join(string.split("_")).title()


def parse_text(string):
    return "_".join(string.lower().split(" "))


class Controlador:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult('final.pl')

    def get_ciudades(self):
        for result in self.prolog.query("setof(X,A^B^C^D^E^actividad(A,X,B,C,D,E),L)"):
            return defaultdict(lambda : None, {parse_prolog(str(i)): str(i) for i in result['L']})

    def get_tipos(self):
        for result in self.prolog.query("setof(X,A^B^C^D^E^actividad(A,B,X,C,D,E),L)"):
            return [str(i) for i in result['L']]

    def get_actividades(self, ciudad, fecha, costo, tipos, calificaciones):
        if fecha is None:
            return []
        query = f"actividad(Nombre,{ciudad},Tipo,Costo,date({fecha.year},{fecha.month},{fecha.day}),Calificacion)"
        if costo is not None:
            query+=f",Costo=<{costo}"
        if len(tipos) > 0:
            query+=f",member(Tipo,[{','.join(tipos)}])"
        else:
            return []
        if len(calificaciones) > 0:
            query+=f",member(Calificacion,[{','.join(calificaciones)}])"
        else:
            return []
        return [i for i in self.prolog.query(query)]
