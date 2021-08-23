from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from logic.controller import Controlador
from visual.ScrollableFrame import *


class VentaPrincial:
    def __init__(self, prolog):
        self.controller = Controlador(prolog)
        self.root = Tk()
        self.root.title("Consulta")
        self.root.minsize(800, 600)
        self.__menubar()
        self.__ciudades = self.controller.get_ciudades()

        style = ttk.Style(self.root)
        style.theme_use(style.theme_names()[0])

        frame_lugar = Frame(self.root)
        frame_lugar.grid(row=0, column=0, padx=10, pady=(10,0), sticky=EW)
        frame_lugar.grid_columnconfigure(1,weight=1)

        Label(frame_lugar, text="Lugar:").grid(row=0, column=0, sticky=W)

        self.__current_option = StringVar()
        self.__current_option.set("Seleccione la ubicación.")
        self.__options = ttk.Combobox(frame_lugar, textvariable=self.__current_option, state="readonly", values=sorted(list(self.__ciudades.keys())))
        self.__options.grid(row=0, column=1, padx=(5,0), sticky=EW)

        frame_presupuesto = Frame(self.root)
        frame_presupuesto.grid(row=1, column=0, padx=10, pady=(10, 0), sticky=EW)
        frame_presupuesto.grid_columnconfigure(1, weight=1)

        Label(frame_presupuesto, text="Presupuesto:").grid(row=0, column=0, sticky=W)

        vcmd = (self.root.register(lambda P: (str.isdigit(P) or P == "")), '%P')

        self.__presupuesto = Entry(frame_presupuesto, validate='all', validatecommand=vcmd)
        self.__presupuesto.grid(row=0, column=1, padx=(5,0), sticky=EW)



        # parte de la tabla
        self.tabla = ScrollableFrame(self.root)
        self.tabla.grid(row=2, column=0, sticky=NSEW, padx=10, pady=10)

        self.tabla.scrollable_frame.grid_columnconfigure(0, weight=3)
        self.tabla.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.tabla.scrollable_frame.grid_columnconfigure(2, weight=1)
        self.tabla.scrollable_frame.grid_columnconfigure(3, weight=1)
        Label(self.tabla.scrollable_frame, text=" Actividad ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=0,
                                    sticky=EW)
        Label(self.tabla.scrollable_frame, text=" Tipo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=1,
                                    sticky=EW)
        Label(self.tabla.scrollable_frame, text=" Costo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=2,
                                    sticky=EW)
        Label(self.tabla.scrollable_frame, text=" Opción ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=3,
                                    sticky=EW)


        self.root.grid_columnconfigure(0, weight=1)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
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

    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Quieres salir del programa?"):
            self.root.destroy()
