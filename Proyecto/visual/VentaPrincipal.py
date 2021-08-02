from tkinter import *
from tkinter import ttk
from visual.ScrollableFrame import *

class VentaPrincial:
    def __init__(self, prolog):
        self.prolog = prolog
        self.root = Tk()
        self.root.title("Planeamiento de Rutas")
        self.root.minsize(800, 600)
        self.__menubar()
        self.__tabla()

        style = ttk.Style(self.root)
        style.theme_use(style.theme_names()[0])

        seleccionBtn = Button(self.root, text="Seleccionar", command=lambda :print("Seleccionar"))
        seleccionBtn.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

        self.__current_option = StringVar()
        self.__options = ttk.Combobox(self.root, textvariable=self.__current_option)
        self.__options.grid(row=1,column=1, padx=10, pady=10, sticky=N)

        planBtn = Button(self.root, text="Ver plan", command=lambda: print("Plan"))
        planBtn.grid(row=2, column=1, padx=10, pady=10, sticky=EW)
        mapaBtn = Button(self.root, text="Ver mapa", command=lambda: print("Mapa"))
        mapaBtn.grid(row=3, column=1, padx=10, pady=10, sticky=EW)
        #spacer
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=10)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.mainloop()

    def __menubar(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo", command=None)
        filemenu.add_command(label="Abrir", command=None)
        filemenu.add_command(label="Guardar", command=None)
        filemenu.add_command(label="Exportar", command=None)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        self.root.config(menu=menubar)

    def __refresh_options(self):
        pass

    def __tabla(self):
        tabla = ScrollableFrame(self.root)
        tabla.grid(row=0,column=0, sticky=NSEW, padx=10, pady=10, rowspan=4)
        for r in range(0, 100):
            for c in range(0, 5):
                cell = ttk.Entry(tabla.scrollable_frame, width=10)
                cell.grid(row=r, column=c)
                cell.insert(0, '({}, {})'.format(r, c))

