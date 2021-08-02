from tkinter import *


class VentaPrincial:
    def __init__(self, prolog):
        self.prolog = prolog
        self.root = Tk()
        self.root.title("Planeamiento de Rutas")
        self.root.minsize(800, 600)
        self.__menubar()
        self.root.mainloop()

    def __menubar(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo", command=None)
        filemenu.add_command(label="Abrir", command=None)
        filemenu.add_command(label="Guardar", command=None)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        self.root.config(menu=menubar)
