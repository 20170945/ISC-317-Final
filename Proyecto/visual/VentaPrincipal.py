from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from logic.controller import Controlador
from visual.ScrollableFrame import *
from visual.widgets.fecha import WidgetFecha


class VentaPrincial:
    def __init__(self):
        self.controller = Controlador()
        self.root = Tk()
        self.root.title("Consulta")
        self.root.minsize(800, 600)
        # self.__menubar()
        self.__ciudades = self.controller.get_ciudades()
        self.root.grid_rowconfigure(4, weight=1)
        # self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_columnconfigure(1, weight=8)
        self.__table_data = []
        self.tipos = []
        self.calificaciones = []

        style = ttk.Style(self.root)
        style.theme_use(style.theme_names()[0])

        frame_lugar = Frame(self.root)
        frame_lugar.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky=EW)
        frame_lugar.grid_columnconfigure(1, weight=1)
        frame_lugar.grid_columnconfigure(3, weight=1)

        Label(frame_lugar, text="Ciudad:").grid(row=0, column=0, sticky=W)

        self.__current_city = StringVar(value="Seleccione la ubicación.")
        self.__options_city = ttk.Combobox(frame_lugar, textvariable=self.__current_city, state="readonly",
                                           values=sorted(list(self.__ciudades.keys())))
        self.__options_city.grid(row=0, column=1, padx=(5, 0), sticky=EW)
        self.__options_city.bind("<<ComboboxSelected>>", self.__on_city_change)

        Label(frame_lugar, text="Lugar:").grid(row=0, column=2, sticky=W)
        self.__current_place = StringVar()
        self.__options_place = ttk.Combobox(frame_lugar, textvariable=self.__current_place, state="readonly")
        self.__options_place.grid(row=0, column=3, padx=(5, 0), sticky=EW)
        self.__options_place.bind("<<ComboboxSelected>>", self.__on_change)


        frame_presupuesto = Frame(self.root)
        frame_presupuesto.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 0), sticky=EW)
        frame_presupuesto.grid_columnconfigure(1, weight=1)

        Label(frame_presupuesto, text="Presupuesto:").grid(row=0, column=0, sticky=W)

        vcmd = (self.root.register(lambda P: (str.isdigit(P) or P == "")), '%P')

        presupuesto_var = StringVar()
        self.__presupuesto = Entry(frame_presupuesto, validate='all', textvariable=presupuesto_var, validatecommand=vcmd, justify=RIGHT)
        presupuesto_var.trace_add("write", lambda a,b,c : self.__on_change())

        self.__presupuesto.grid(row=0, column=1, padx=(5, 0), sticky=EW)

        frame_fecha = Frame(self.root)
        frame_fecha.grid(row=2, column=0, columnspan=2, padx=10, pady=(10, 0), sticky=EW)
        frame_fecha.grid_columnconfigure(1, weight=1)

        Label(frame_fecha, text="Fecha:").grid(row=0, column=0, sticky=W)

        self.__fecha = WidgetFecha(frame_fecha)
        self.__fecha.grid(row=0, column=1, sticky=W)
        self.__fecha.set_on_change(self.__on_change)

        #calificacion
        frame_calif = Frame(self.root, borderwidth=2, relief=SUNKEN)
        frame_calif.grid(row=3, column=0, padx=(10,5),pady=(10,5),sticky=NSEW)
        self.__califs_valor = []
        Label(frame_calif, text="Calificaciones:").grid(row=0, column=0, sticky=W)
        for index,i in enumerate(range(5,0,-1)):
            self.__califs_valor.append(StringVar(value=i))
            Checkbutton(frame_calif, text=i, variable=self.__califs_valor[index],
                        onvalue=str(i), offvalue="",
                        command=self.__on_calif_select).grid(row=index+1, column=0, sticky=W)
        self.__on_calif_select()

        # tipos
        frame_tipos = Frame(self.root, borderwidth=2, relief=SUNKEN)
        frame_tipos.grid(row=4, column=0, padx=(10, 5), pady=(0,10), sticky=NSEW)
        frame_tipos.grid_columnconfigure(0, weight=1)
        frame_tipos.grid_rowconfigure(1, weight=1)
        Label(frame_tipos, text="Tipos:").grid(row=0, column=0, sticky=W)
        tipos_scrollingframe = ScrollableFrame(frame_tipos)
        tipos_scrollingframe.grid(row=1, column=0, sticky=NSEW)
        self.__tipos_valor = []
        for index, tipo in enumerate(self.controller.get_tipos()):
            self.__tipos_valor.append(StringVar(value=tipo))
            Checkbutton(tipos_scrollingframe.scrollable_frame, text=tipo.title(), variable=self.__tipos_valor[index], onvalue=tipo, offvalue="",
                        command=self.__on_tipo_select).grid(row=index, column=0, sticky=W)
        self.__on_tipo_select()

        # parte de la tabla
        self.tabla = ScrollableFrame(self.root, borderwidth=2, relief=SUNKEN)
        self.tabla.grid(row=3, rowspan=2, column=1, sticky=NSEW, padx=(0, 10), pady=10)

        self.tabla.scrollable_frame.grid_columnconfigure(0, weight=3)
        self.tabla.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.tabla.scrollable_frame.grid_columnconfigure(2, weight=1)
        self.tabla.scrollable_frame.grid_columnconfigure(3, weight=1)
        Label(self.tabla.scrollable_frame, text=" Nombre ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=0,
                                    sticky=EW)
        Label(self.tabla.scrollable_frame, text=" Calificación ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=1,
                                    sticky=EW)
        Label(self.tabla.scrollable_frame, text=" Tipo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=2,
                                    sticky=EW)
        Label(self.tabla.scrollable_frame, text=" Costo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=3,
                                    sticky=EW)


        self.root.grid_columnconfigure(0, weight=1)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def __on_change(self, event=None):
        costo = self.__presupuesto.get()
        if len(costo) == 0:
            costo = None
        ciudad = self.__ciudades[self.__current_city.get()]
        for row in self.__table_data:
            for col in row:
                col.destroy()
        self.__table_data.clear()
        if ciudad is not None:
            for index, row in enumerate(self.controller.get_actividades(ciudad, self.__current_place.get(), self.__fecha.get_fecha(), costo, self.tipos, self.calificaciones), start=1):
                h = row['Nombre']
                if type(h) is bytes:
                    h = h.decode("utf-8")
                drow = [
                    Label(self.tabla.scrollable_frame, text=f" {h} ", anchor=W, borderwidth=1, relief="solid",
                          bg="white"),
                    Label(self.tabla.scrollable_frame, text=f" {row['Calificacion']} ",  justify=CENTER, borderwidth=1,
                          relief="solid",
                          bg="white"),
                    Label(self.tabla.scrollable_frame, text=f" {row['Tipo'].title()} ", borderwidth=1, justify=CENTER,
                          relief="solid",
                          bg="white"),
                    Label(self.tabla.scrollable_frame, text=f" {row['Costo']} ", anchor=E, borderwidth=1,
                          relief="solid",
                          bg="white")
                ]
                for j, i in enumerate(drow):
                    i.grid(row=index, column=j, sticky=NSEW)
                self.__table_data.append(drow)

    def __on_tipo_select(self):
        self.tipos = set([i.get() for i in self.__tipos_valor if i.get()!=""])
        self.__on_change()

    def __on_calif_select(self):
        self.calificaciones = set([i.get() for i in self.__califs_valor if i.get()!=""])
        self.__on_change()

    def __on_city_change(self, event=None):
        self.__current_place.set("Ciudad")
        self.__options_place["values"] = self.controller.get_lugares(self.__ciudades[self.__current_city.get()])
        self.__on_change(event)

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

    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Quieres salir del programa?"):
            self.root.destroy()
