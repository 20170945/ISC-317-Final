import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from logic.controller import Controlador
from visual.ActividadesCulturalesSemanal import ActividadesCulturalesSemanal
from visual.EventoMensual import Evento_Mensual
from visual.Listado_Peliculas import Lista_Peliculas
from visual.ScrollableFrame import *
from visual.widgets.datetime import WidgetFecha, WidgetTiempo


class VentaPrincial:
    def __init__(self):
        self.controller = Controlador()
        self.root = Tk()
        self.root.title("Consulta")
        self.root.minsize(800, 600)
        self.__menubar()
        self.__provincias = self.controller.get_provincias()
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.cine_query = {
            "cine": {
                "calif": []
            },
            "pelicula": {
                "calif": [],
                "generos": []
            }
        }

        self.__table_data = []
        self.__tabla_restaurante = []
        self.tipos = []
        self.calificaciones = []

        style = ttk.Style(self.root)
        style.theme_use(style.theme_names()[0])

        self.opciones_generales()

        self.actividades_tab = ttk.Notebook(self.root)

        tab_restaurante = self.gtab_restaurante(self.actividades_tab)
        tab_cine = self.gtab_cines(self.actividades_tab)
        tab_otros = self.gtab_otro(self.actividades_tab)
        tab_bar = self.gtab_bar(self.actividades_tab)
        self.actividades_tab.add(tab_restaurante, text="Restaurante")
        self.actividades_tab.add(tab_cine, text="Cines")
        self.actividades_tab.add(tab_bar, text="Bar")
        self.actividades_tab.add(tab_otros, text="Otros")
        self.actividades_tab.grid(row=3, column=0, pady=(5,10), padx=10, sticky=NSEW)
        self.actividades_tab.bind('<<NotebookTabChanged>>', self.__on_change)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def gtab_otro(self, cont):
        tab_otros = Frame(cont)
        tab_otros.grid_columnconfigure(0, weight=1)
        tab_otros.grid_columnconfigure(1, weight=9)
        tab_otros.grid_rowconfigure(1, weight=1)

        # calificacion
        frame_calif = Frame(tab_otros, borderwidth=2, relief=SUNKEN)
        frame_calif.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), sticky=NSEW)
        self.__califs_valor = []
        Label(frame_calif, text="Calificaciones:").grid(row=0, column=0, sticky=W)
        for index, i in enumerate(range(5, 0, -1)):
            self.__califs_valor.append(StringVar(value=i))
            Checkbutton(frame_calif, text=i, variable=self.__califs_valor[index],
                        onvalue=str(i), offvalue="",
                        command=self.__on_change).grid(row=index + 1, column=0, sticky=W)
        # self.__on_calif_select()

        # tipos
        frame_tipos = Frame(tab_otros, borderwidth=2, relief=SUNKEN)
        frame_tipos.grid(row=1, column=0, padx=(0, 5), pady=(0, 0), sticky=NSEW)
        frame_tipos.grid_columnconfigure(0, weight=1)
        frame_tipos.grid_rowconfigure(1, weight=1)
        Label(frame_tipos, text="Tipos:").grid(row=0, column=0, sticky=W)
        tipos_scrollingframe = ScrollableFrame(frame_tipos)
        tipos_scrollingframe.grid(row=1, column=0, sticky=NSEW)
        self.__tipos_valor = []
        for index, tipo in enumerate(self.controller.get_otro_tipos()):
            self.__tipos_valor.append(StringVar(value=tipo))
            Checkbutton(tipos_scrollingframe.scrollable_frame, text=tipo.replace('_', ' ').title(),
                        variable=self.__tipos_valor[index],
                        onvalue=tipo, offvalue="",
                        command=self.__on_change).grid(row=index, column=0, sticky=W)
        # self.__on_tipo_select()

        # parte de la tabla
        self.tabla_otro = ScrollableFrame(tab_otros, borderwidth=2, relief=SUNKEN)
        self.tabla_otro.grid(row=0, rowspan=2, column=1, sticky=NSEW)

        self.tabla_otro.scrollable_frame.grid_columnconfigure(0, weight=3)
        self.tabla_otro.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.tabla_otro.scrollable_frame.grid_columnconfigure(2, weight=1)
        self.tabla_otro.scrollable_frame.grid_columnconfigure(3, weight=1)
        Label(self.tabla_otro.scrollable_frame, text=" Nombre ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=0,
                                    sticky=EW)
        Label(self.tabla_otro.scrollable_frame, text=" Calificaci??n ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=1,
                                    sticky=EW)
        Label(self.tabla_otro.scrollable_frame, text=" Tipo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=2,
                                    sticky=EW)
        Label(self.tabla_otro.scrollable_frame, text=" Costo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=3,
                                    sticky=EW)
        return tab_otros

    def gtab_restaurante(self, cont):
        tab = Frame(cont)
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_columnconfigure(1, weight=9)
        tab.grid_rowconfigure(1, weight=1)

        # calificacion
        frame_calif = Frame(tab, borderwidth=2, relief=SUNKEN)
        frame_calif.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), sticky=NSEW)
        self.__calif_rest = []
        Label(frame_calif, text="Calificaciones:").grid(row=0, column=0, sticky=W)
        for index, i in enumerate(range(5, 0, -1)):
            self.__calif_rest.append(StringVar(value=i))
            Checkbutton(frame_calif, text=i, variable=self.__calif_rest[index],
                        onvalue=str(i), offvalue="",
                        command=self.__on_change).grid(row=index + 1, column=0, sticky=W)

        # tipos
        frame_tipos = Frame(tab, borderwidth=2, relief=SUNKEN)
        frame_tipos.grid(row=1, column=0, padx=(0, 5), sticky=NSEW)
        frame_tipos.grid_columnconfigure(0, weight=1)
        frame_tipos.grid_rowconfigure(1, weight=1)
        Label(frame_tipos, text="Tipos:").grid(row=0, column=0, sticky=W)
        tipos_scrollingframe = ScrollableFrame(frame_tipos)
        tipos_scrollingframe.grid(row=1, column=0, sticky=NSEW)
        self.__tipos_res_valor = []
        for index, tipo in enumerate(self.controller.get_restaurante_tipos()):
            self.__tipos_res_valor.append(StringVar(value=tipo))
            Checkbutton(tipos_scrollingframe.scrollable_frame, text=tipo.replace('_', ' ').title(),
                        variable=self.__tipos_res_valor[index],
                        onvalue=tipo, offvalue="",
                        command=self.__on_change).grid(row=index, column=0, sticky=W)

        # parte de la tabla
        self.tabla_res = ScrollableFrame(tab, borderwidth=2, relief=SUNKEN)
        self.tabla_res.grid(row=0, rowspan=2, column=1, sticky=NSEW)

        self.tabla_res.scrollable_frame.grid_columnconfigure(0, weight=3)
        self.tabla_res.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.tabla_res.scrollable_frame.grid_columnconfigure(2, weight=1)
        self.tabla_res.scrollable_frame.grid_columnconfigure(3, weight=1)
        Label(self.tabla_res.scrollable_frame, text=" Nombre ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=0,
                                    sticky=EW)
        Label(self.tabla_res.scrollable_frame, text=" Calificaci??n ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=1,
                                    sticky=EW)
        Label(self.tabla_res.scrollable_frame, text=" Tipo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=2,
                                    sticky=EW)
        Label(self.tabla_res.scrollable_frame, text=" Costo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=3,
                                    sticky=EW)
        return tab

    def gtab_bar(self, cont):
        tab = Frame(cont)
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_columnconfigure(1, weight=9)
        tab.grid_rowconfigure(1, weight=1)

        # calificacion
        frame_calif = Frame(tab, borderwidth=2, relief=SUNKEN)
        frame_calif.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), sticky=NSEW)
        self.__calif_bar = []
        Label(frame_calif, text="Calificaciones:").grid(row=0, column=0, sticky=W)
        for index, i in enumerate(range(5, 0, -1)):
            self.__calif_bar.append(StringVar(value=i))
            Checkbutton(frame_calif, text=i, variable=self.__calif_bar[index],
                        onvalue=str(i), offvalue="",
                        command=self.__on_change).grid(row=index + 1, column=0, sticky=W)

        # parte de la tabla
        self.tabla_bar = ScrollableFrame(tab, borderwidth=2, relief=SUNKEN)
        self.tabla_bar.grid(row=0, rowspan=2, column=1, sticky=NSEW)

        self.tabla_bar.scrollable_frame.grid_columnconfigure(0, weight=3)
        self.tabla_bar.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.tabla_bar.scrollable_frame.grid_columnconfigure(2, weight=1)
        Label(self.tabla_bar.scrollable_frame, text=" Nombre ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=0,
                                    sticky=EW)
        Label(self.tabla_bar.scrollable_frame, text=" Calificaci??n ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=1,
                                    sticky=EW)
        Label(self.tabla_bar.scrollable_frame, text=" Costo ", borderwidth=2, relief="solid", justify=CENTER,
               bg="light gray").grid(row=0,
                                                    column=2,
                                                    sticky=EW)
        return tab

    def gtab_cines(self, cont):
        tab = Frame(cont)
        tab.grid_rowconfigure(3, weight=1)
        tab.grid_columnconfigure(0, weight=2)
        # tab.grid_columnconfigure(1, weight=2)
        tab.grid_columnconfigure(3, weight=12)
        cines = Frame(tab, borderwidth=2, relief=SUNKEN)
        cines.grid(row=1, column=0, columnspan=2, padx=(0, 5), pady=(0, 5), sticky=NSEW)
        self.calif_cine = []
        self.peliculas_tipos = []
        self.calif_pelicula = []

        def update():
            self.cine_query["cine"]["calif"] = [i.get() for i in self.calif_cine if i.get() != ""]
            self.cine_query["pelicula"]["calif"] = [i.get() for i in self.calif_pelicula if i.get() != ""]
            self.cine_query["pelicula"]["generos"] = [i.get() for i in self.peliculas_tipos if i.get() != ""]
            try:
                self.__on_change()
            except:
                pass

        Label(cines, text="Calificaciones:").grid(row=0, column=0, sticky=W)
        for index, i in enumerate(range(5, 0, -1)):
            self.calif_cine.append(StringVar(value=i))
            Checkbutton(cines, text=i, variable=self.calif_cine[index],
                        onvalue=str(i), offvalue="",
                        command=update).grid(row=index + 1, column=0, sticky=W)

        Label(tab, text="Tienen pel??culas con:").grid(row=2, column=0, columnspan=2, sticky=W)

        # generos de pelicula
        frame_generos = Frame(tab, borderwidth=2, relief=SUNKEN)
        frame_generos.grid(row=3, column=0, padx=(0, 5), sticky=NSEW)
        frame_generos.grid_columnconfigure(0, weight=1)
        frame_generos.grid_rowconfigure(1, weight=1)
        Label(frame_generos, text="Generos:").grid(row=0, column=0, sticky=W)
        generos_scrollingframe = ScrollableFrame(frame_generos)
        generos_scrollingframe.grid(row=1, column=0, sticky=NSEW)

        for index, tipo in enumerate(self.controller.get_generos_pelicula()):
            self.peliculas_tipos.append(StringVar(value=tipo))
            Checkbutton(generos_scrollingframe.scrollable_frame, text=tipo.replace('_', ' ').title(),
                        variable=self.peliculas_tipos[index],
                        onvalue=tipo, offvalue="",
                        command=update).grid(row=index, column=0, sticky=W)

        calif_peli = Frame(tab, borderwidth=2, relief=SUNKEN)
        calif_peli.grid(row=3, column=1, padx=(0, 5), sticky=NS)

        Label(calif_peli, text="Calificaciones:").grid(row=0, column=0, sticky=W)
        for index, i in enumerate(range(5, 0, -1)):
            self.calif_pelicula.append(StringVar(value=i))
            Checkbutton(calif_peli, text=i, variable=self.calif_pelicula[index],
                        onvalue=str(i), offvalue="",
                        command=update).grid(row=index + 1, column=0, sticky=W)

        self.tabla_cine = ScrollableFrame(tab, borderwidth=2, relief=SUNKEN)
        self.tabla_cine.grid(row=0, rowspan=4, column=3, sticky=NSEW)

        self.tabla_cine.scrollable_frame.grid_columnconfigure(0, weight=8)
        self.tabla_cine.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.tabla_cine.scrollable_frame.grid_columnconfigure(2, weight=1)
        Label(self.tabla_cine.scrollable_frame, text=" Nombre ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=0,
                                    sticky=EW)
        Label(self.tabla_cine.scrollable_frame, text=" Calificaci??n ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=1,
                                    sticky=EW)
        Label(self.tabla_cine.scrollable_frame, text=" Pel??culas ", borderwidth=2, relief="solid",
              justify=CENTER,bg="light gray").grid(row=0,
                                    column=2,
                                    sticky=EW)
        update()
        return tab

    def opciones_generales(self):
        frame_lugar = Frame(self.root)
        frame_lugar.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky=EW)
        frame_lugar.grid_columnconfigure(1, weight=1)
        frame_lugar.grid_columnconfigure(3, weight=1)

        def call_on_change(a,b,c):
            self.__on_change()

        Label(frame_lugar, text="Provincia:").grid(row=0, column=0, sticky=W)

        self.__current_provincia = StringVar(value="Seleccione la ubicaci??n.")
        self.__options_provincia = ttk.Combobox(frame_lugar, textvariable=self.__current_provincia, state="readonly",
                                                values=sorted(list(self.__provincias.keys())))
        self.__options_provincia.grid(row=0, column=1, padx=(5, 0), sticky=EW)
        self.__options_provincia.bind("<<ComboboxSelected>>", self.__on_provincia_change)

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

        self.__presupuesto_var = StringVar()
        self.__presupuesto = Entry(frame_presupuesto, validate='all', textvariable=self.__presupuesto_var,
                                   validatecommand=vcmd, justify=RIGHT)
        self.__presupuesto_var.trace_add("write", call_on_change)

        self.__presupuesto.grid(row=0, column=1, padx=(5, 0), sticky=EW)

        frame_datetime = Frame(self.root)
        frame_datetime.grid(row=2, column=0, columnspan=2, padx=10, pady=(10, 0), sticky=EW)

        frame_fecha = Frame(frame_datetime)
        frame_fecha.grid(row=0, column=0, sticky=NSEW)
        frame_fecha.grid_columnconfigure(1, weight=1)

        Label(frame_fecha, text="Fecha:").grid(row=0, column=0, sticky=W)

        self.__fecha = WidgetFecha(frame_fecha)
        self.__fecha.grid(row=0, column=1, sticky=W)
        self.__fecha.set_on_change(self.__on_change)

        frame_tiempo = Frame(frame_datetime)
        frame_tiempo.grid(row=0, column=1, sticky=NSEW, padx=(20, 0))
        Label(frame_tiempo, text="Tiempo:").grid(row=0, column=0, sticky=W)
        self.__tiempo = WidgetTiempo(frame_tiempo)
        self.__tiempo.grid(row=0, column=1, sticky=W)
        self.__tiempo.set_on_change(self.__on_change)

        # Campo de Precio Min
        frame_min = Frame(frame_datetime)
        frame_min.grid(row=0, column=1, sticky=NSEW, padx=(205, 0))
        Label(frame_min, text="Precio Min:").grid(row=0, column=0, sticky=W)

        vcmd = (self.root.register(lambda P: (str.isdigit(P) or P == "")), '%P')

        self.__min_var = StringVar()
        self.__min = Entry(frame_min, validate='all', textvariable=self.__min_var,
                           validatecommand=vcmd, width=7, justify=RIGHT)
        self.__min_var.trace_add("write", lambda a, b, c: self.__on_change())

        self.__min.grid(row=0, column=1, sticky=W)

        #Campo de Precio M??x
        frame_max = Frame(frame_datetime)
        frame_max.grid(row=0, column=1, sticky=NSEW, padx=(322, 0))
        Label(frame_max, text="Precio M??x:").grid(row=0, column=0, sticky=W)

        # vcmd = (self.root.register(lambda P: (str.isdigit(P) or P == "")), '%P')

        self.__max_var = StringVar()
        self.__max = Entry(frame_max, validate='all', textvariable=self.__max_var,
                                   validatecommand=vcmd, width=7, justify=RIGHT)
        self.__max_var.trace_add("write", call_on_change)

        self.__max.grid(row=0, column=1, sticky=W)

        # Campo de Porcentaje de presupuesto
        frame_porcentaje = Frame(frame_datetime)
        frame_porcentaje.grid(row=2, column=0, pady=(10, 0), sticky=NSEW)
        frame_porcentaje.grid_columnconfigure(1, weight=1)

        Label(frame_porcentaje, text="Porcentaje:").grid(row=0, column=0, sticky=W)

        vcmd = (self.root.register(lambda P: (str.isdigit(P) or P == "")), '%P')
        self.__porc_var = StringVar()

        self.__porc = ttk.Spinbox(
            frame_porcentaje,
            from_=0,
            to=100,
            textvariable=self.__porc_var,
            wrap=True,
            validate=ALL,
            validatecommand=vcmd,
            justify=RIGHT
        )

        self.__porc_var.trace_add("write", lambda a, b, c: self.__on_change())

        self.__porc.grid(row=0, column=1, sticky=W)


    def __on_change(self, event=None):
        tab_id = self.actividades_tab.index(self.actividades_tab.select())
        if tab_id == 0:
            self.load_table_restaurante()
        elif tab_id == 1:
            self.load_table_cines()
        elif tab_id == 2:
            self.load_table_bar()
        elif tab_id == 3:
            self.load_table_otros()


    def load_table_cines(self):
        fecha = self.__fecha.get_fecha()
        tiempo = self.__tiempo.get_time()
        costo = self.__presupuesto.get()
        fechatiempo = datetime.datetime(fecha.year, fecha.month, fecha.day, tiempo.hora, tiempo.minuto)
        if len(costo) == 0:
            costo = None
        provincia = self.__provincias[self.__current_provincia.get()]
        for row in self.__table_data:
            for col in row:
                col.destroy()
        self.__table_data.clear()
        datos = self.controller.get_cines_disponibles(provincia,self.cine_query["pelicula"]["calif"], costo, fechatiempo, self.__current_place.get(), self.cine_query["pelicula"]["generos"])
        def creador_de_lambda(name):
            return lambda: Lista_Peliculas(
                self.root,
                name,
                self.controller.get_peliculas_disponibles_cine(
                    name,
                    provincia,
                    self.__current_place.get(),
                    self.cine_query["pelicula"]["calif"],
                    costo,
                    fechatiempo,
                    self.cine_query["pelicula"]["generos"]
                )
            )
        if provincia is not None:
            for index, row in enumerate(datos, start=1):
                drow = [
                    Label(self.tabla_cine.scrollable_frame, text=f" {row['nombre']} ", anchor=W, borderwidth=1, relief="solid",
                          bg="white"),
                    Label(self.tabla_cine.scrollable_frame, text=f" {row['calif']} ", justify=CENTER,
                          borderwidth=1,
                          relief="solid",
                          bg="white"),
                    Button(self.tabla_cine.scrollable_frame, text=" Ver ", justify=CENTER,
                           command=creador_de_lambda(row['nombre']))
                ]
                for j, i in enumerate(drow):
                    i.grid(row=index, column=j, sticky=NSEW)
                self.__table_data.append(drow)

    def load_table_otros(self):
        fecha = self.__fecha.get_fecha()
        tiempo = self.__tiempo.get_time()
        fechatiempo = datetime.datetime(fecha.year, fecha.month, fecha.day, tiempo.hora, tiempo.minuto)
        costo = self.__presupuesto.get()
        tipos = set([i.get() for i in self.__tipos_valor if i.get() != ""])
        max = self.__max.get()
        min = self.__min.get()
        porcentaje = self.__porc.get()
        calificaciones = set([i.get() for i in self.__califs_valor if i.get() != ""])
        if len(costo) == 0:
            costo = None
        if len(max) == 0:
            max = None
        if len(min) == 0:
            min = None
        if len(porcentaje) == 0 or int(porcentaje) == 0:
            porcentaje = None
        else:
            porcentaje = int(porcentaje)
        provincia = self.__provincias[self.__current_provincia.get()]
        for row in self.__table_data:
            for col in row:
                col.destroy()
        self.__table_data.clear()
        if provincia is not None:
            for index, row in enumerate(
                    self.controller.get_actividades(provincia, self.__current_place.get(), fechatiempo,
                                                    costo, tipos, calificaciones, porcentaje, min, max), start=1):
                h = row['Nombre']
                if type(h) is bytes:
                    h = h.decode("utf-8")
                drow = [
                    Label(self.tabla_otro.scrollable_frame, text=f" {h} ", anchor=W, borderwidth=1, relief="solid",
                          bg="white"),
                    Label(self.tabla_otro.scrollable_frame, text=f" {row['Calificacion']} ", justify=CENTER,
                          borderwidth=1,
                          relief="solid",
                          bg="white"),
                    Label(self.tabla_otro.scrollable_frame, text=f" {row['Tipo'].title()} ", borderwidth=1,
                          justify=CENTER,
                          relief="solid",
                          bg="white"),
                    Label(self.tabla_otro.scrollable_frame, text=f" {row['Costo']} ", anchor=E, borderwidth=1,
                          relief="solid",
                          bg="white")
                ]
                for j, i in enumerate(drow):
                    i.grid(row=index, column=j, sticky=NSEW)
                self.__table_data.append(drow)

    def load_table_restaurante(self):
        fecha = self.__fecha.get_fecha()
        tiempo = self.__tiempo.get_time()
        fechatiempo = datetime.datetime(fecha.year, fecha.month, fecha.day, tiempo.hora, tiempo.minuto)
        costo = self.__presupuesto.get()
        tipos = set([i.get() for i in self.__tipos_res_valor if i.get() != ""])
        max = self.__max.get()
        min = self.__min.get()
        porcentaje = self.__porc.get()
        calificaciones = set([i.get() for i in self.__calif_rest if i.get() != ""])
        if len(costo) == 0:
            costo = None
        if len(max) == 0:
            max = None
        if len(min) == 0:
            min = None
        if len(porcentaje) == 0 or int(porcentaje) == 0:
            porcentaje = None
        else:
            porcentaje = int(porcentaje)
        provincia = self.__provincias[self.__current_provincia.get()]
        for row in self.__table_data:
            for col in row:
                col.destroy()
        self.__table_data.clear()
        if provincia is not None:
            for index, row in enumerate(
                    self.controller.get_restaurantes(provincia, self.__current_place.get(), fechatiempo,
                                                     costo, tipos, calificaciones, porcentaje, min, max), start=1):
                h = row['Nombre']
                if type(h) is bytes:
                    h = h.decode("utf-8")
                drow = [
                    Label(self.tabla_res.scrollable_frame, text=f" {h} ", anchor=W, borderwidth=1, relief="solid",
                          bg="white"),
                    Label(self.tabla_res.scrollable_frame, text=f" {row['Calificacion']} ", justify=CENTER,
                          borderwidth=1,
                          relief="solid",
                          bg="white"),
                    Label(self.tabla_res.scrollable_frame, text=f" {row['Tipo'].replace('_',' ').title()} ", borderwidth=1,
                          justify=CENTER,
                          relief="solid",
                          bg="white"),
                    Label(self.tabla_res.scrollable_frame, text=f" {row['Costo']} ", anchor=E, borderwidth=1,
                          relief="solid",
                          bg="white")
                ]
                for j, i in enumerate(drow):
                    i.grid(row=index, column=j, sticky=NSEW)
                self.__table_data.append(drow)

    def load_table_bar(self):
        fecha = self.__fecha.get_fecha()
        tiempo = self.__tiempo.get_time()
        fechatiempo = datetime.datetime(fecha.year, fecha.month, fecha.day, tiempo.hora, tiempo.minuto)
        costo = self.__presupuesto.get()
        max = self.__max.get()
        min = self.__min.get()
        porcentaje = self.__porc.get()
        calificaciones = set([i.get() for i in self.__calif_bar if i.get() != ""])
        if len(costo) == 0:
            costo = None
        if len(max) == 0:
            max = None
        if len(min) == 0:
            min = None
        if len(porcentaje) == 0 or int(porcentaje) == 0:
            porcentaje = None
        else:
            porcentaje = int(porcentaje)
        provincia = self.__provincias[self.__current_provincia.get()]
        for row in self.__table_data:
            for col in row:
                col.destroy()
        self.__table_data.clear()
        if provincia is not None:
            for index, row in enumerate(
                    self.controller.get_bares(provincia, self.__current_place.get(), fechatiempo,
                                                     costo, calificaciones, porcentaje, min, max), start=1):
                h = row['Nombre']
                if type(h) is bytes:
                    h = h.decode("utf-8")
                drow = [
                    Label(self.tabla_bar.scrollable_frame, text=f" {h} ", anchor=W, borderwidth=1, relief="solid",
                          bg="white"),
                    Label(self.tabla_bar.scrollable_frame, text=f" {row['Calificacion']} ", justify=CENTER,
                          borderwidth=1,
                          relief="solid",
                          bg="white"),
                    Label(self.tabla_bar.scrollable_frame, text=f" {row['Costo']} ", anchor=E, borderwidth=1,
                          relief="solid",
                          bg="white")
                ]

                for j, i in enumerate(drow):
                    i.grid(row=index, column=j, sticky=NSEW)
                self.__table_data.append(drow)

    def __on_provincia_change(self, event=None):
        listado = self.controller.get_lugares(self.__provincias[self.__current_provincia.get()])
        self.__current_place.set(listado[0])
        self.__options_place["values"] = listado
        self.__on_change(event)

    def __menubar(self):
        menubar = Menu(self.root)
        menu_addicional = Menu(menubar, tearoff=0)
        menu_semanal = Menu(menu_addicional, tearoff=0)
        menu_semanal.add_command(label="Actividades Culturales", command=lambda: ActividadesCulturalesSemanal(self.root,self.controller))
        menu_addicional.add_cascade(label="Semanal", menu=menu_semanal)
        menu_mensual = Menu(menu_addicional, tearoff=0)
        menu_mensual.add_command(label="Eventos", command=lambda : Evento_Mensual(self.root,self.controller))
        menu_addicional.add_cascade(label="Mensual", menu=menu_mensual)
        menubar.add_cascade(label="Consultas adicionales", menu=menu_addicional)
        self.root.config(menu=menubar)

    def on_closing(self):
        if messagebox.askokcancel("Salir", "??Quieres salir del programa?"):
            self.root.destroy()
