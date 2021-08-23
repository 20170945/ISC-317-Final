class Controlador:
    def __init__(self, prolog):
        self.prolog = prolog

    def get_ciudades(self):
        return {self.parse_prolog(i['X']): i['X'] for i in self.prolog.query("ciudad(X)")}

    def get_playas(self, ciudad):
        return [i['X'] for i in self.prolog.query(f"playa(X,{ciudad})")]


    def parse_prolog(self, string):
        return " ".join(string.split("_")).title()

    def parse_text(self, string):
        return "_".join(string.lower().split(" "))
