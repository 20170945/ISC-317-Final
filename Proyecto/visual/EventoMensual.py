from datetime import date
from tkinter import *
from tkinter import ttk

from visual.ScrollableFrame import ScrollableFrame
from visual.widgets.datetime import WidgetFecha


class Evento_Mensual(Toplevel):
    def __init__(self, target, controlador):
        super().__init__(target)
        self.__parent = target
        self.controller = controlador
        self.__provincias = self.controller.get_provincias()
        self.title("Eventos importantes por mes")
        self.grab_set()
        self.minsize(800, 600)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.__table_data = []

        frame_lugar = Frame(self)
        frame_lugar.grid(row=0, column=0, padx=10, pady=(10, 0), sticky=EW)
        frame_lugar.grid_columnconfigure(1, weight=1)
        frame_lugar.grid_columnconfigure(3, weight=1)



        Label(frame_lugar, text="Provincia:").grid(row=0, column=0, sticky=W)

        self.__current_provincia = StringVar(value="Seleccione la ubicación.")
        self.__options_provincia = ttk.Combobox(frame_lugar, textvariable=self.__current_provincia, state="readonly",
                                                values=sorted(list(self.__provincias.keys())))
        self.__options_provincia.grid(row=0, column=1, padx=(5, 0), sticky=EW)
        self.__options_provincia.bind("<<ComboboxSelected>>", self.__on_provincia_change)

        Label(frame_lugar, text="Lugar:").grid(row=0, column=2, sticky=W)
        self.__current_place = StringVar()
        self.__options_place = ttk.Combobox(frame_lugar, textvariable=self.__current_place, state="readonly")
        self.__options_place.grid(row=0, column=3, padx=(5, 0), sticky=EW)
        self.__options_place.bind("<<ComboboxSelected>>", self.__on_change)

        frame_presupuesto = Frame(self)
        frame_presupuesto.grid(row=1, column=0, padx=10, pady=(10, 0), sticky=EW)
        frame_presupuesto.grid_columnconfigure(1, weight=1)
        Label(frame_presupuesto, text="Presupuesto:").grid(row=0, column=0, sticky=W)

        vcmd = (self.register(lambda P: (str.isdigit(P) or P == "")), '%P')

        self.__presupuesto_var = StringVar()
        self.__presupuesto = Entry(frame_presupuesto, validate='all', textvariable=self.__presupuesto_var,
                                   validatecommand=vcmd, justify=RIGHT)
        self.__presupuesto_var.trace_add("write", lambda a,b,c:self.__on_change())

        self.__presupuesto.grid(row=0, column=1, padx=(5, 0), sticky=EW)

        frame_fecha = Frame(self)
        frame_fecha.grid(row=2, column=0, pady=(10,0), padx=10, sticky=NSEW)
        frame_fecha.grid_columnconfigure(1, weight=1)

        Label(frame_fecha, text="Fecha:").grid(row=0, column=0, sticky=W)

        self.__fecha = WidgetFecha(frame_fecha, dia=False)
        self.__fecha.grid(row=0, column=1, sticky=W)
        self.__fecha.set_on_change(self.__on_change)

        frame_calif = Frame(self)
        frame_calif.grid(row=3, column=0, padx=10, pady=(10,0), sticky=EW)
        self.__calif_bar = []
        Label(frame_calif, text="Calificaciones:").grid(row=0, column=0, sticky=W)
        for index, i in enumerate(range(1, 6)):
            self.__calif_bar.append(StringVar(value=i))
            Checkbutton(frame_calif, text=i, variable=self.__calif_bar[index],
                        onvalue=str(i), offvalue="", borderwidth=1, relief="solid",
                        command=self.__on_change).grid(row=0, column=index + 1, sticky=W)

        self.eventos_table = ScrollableFrame(self)
        self.eventos_table.grid(row=4, column=0, pady=(5,0), sticky=NSEW)

        self.eventos_table.scrollable_frame.grid_columnconfigure(0, weight=8)
        # peliculas.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.eventos_table.scrollable_frame.grid_columnconfigure(2, weight=1)
        self.eventos_table.scrollable_frame.grid_columnconfigure(3, weight=1)
        Label(self.eventos_table.scrollable_frame, text=" Evento ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=0,
                                    sticky=EW)
        Label(self.eventos_table.scrollable_frame, text=" Calificación ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=1,
                                    sticky=EW)
        Label(self.eventos_table.scrollable_frame, text=" Costo ", borderwidth=2, relief="solid",
              justify=CENTER, bg="light gray").grid(row=0,
                                                    column=2,
                                                    sticky=EW)
        Label(self.eventos_table.scrollable_frame, text=" Fecha ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=3,
                                    sticky=EW)

        Button(self, text=" Volver ", command=self.destroy).grid(row=5, column=0, padx=(0, 10), pady=(5, 10), sticky=E)

        self.mainloop()

    def __on_provincia_change(self, event=None):
        listado = self.controller.get_lugares(self.__provincias[self.__current_provincia.get()])
        self.__current_place.set(listado[0])
        self.__options_place["values"] = listado
        self.__on_change(event)

    def __on_change(self, event=None):
        fecha = self.__fecha.get_fecha()
        costo = self.__presupuesto.get()
        # self.__current_place lugar
        calificaciones = set([i.get() for i in self.__calif_bar if i.get() != ""])
        if len(costo) == 0:
            costo = None
        provincia = self.__provincias[self.__current_provincia.get()]
        for row in self.__table_data:
            for col in row:
                col.destroy()
        self.__table_data.clear()
        if provincia is not None:
            for index, row in enumerate(self.controller.get_eventos_en_mes(provincia, self.__current_place.get(), fecha, calificaciones,
                                              costo), start=1):
                drow = [
                    Label(self.eventos_table.scrollable_frame, text=f" {row[0].decode('utf-8')} ", anchor=W, borderwidth=1, relief="solid",
                          bg="white"),
                    Label(self.eventos_table.scrollable_frame, text=f" {row[6]} ", justify=CENTER, borderwidth=1,
                          relief="solid",
                          bg="white"),
                    Label(self.eventos_table.scrollable_frame, text=f" {row[3]} ", anchor=E, borderwidth=1,
                          relief="solid",
                          bg="white"),
                    Label(self.eventos_table.scrollable_frame, text=f" {date(row[4].args[0],row[4].args[1],row[4].args[2])} ", justify=CENTER, borderwidth=1,
                          relief="solid",
                          bg="white")
                ]
                for j, i in enumerate(drow):
                    i.grid(row=index, column=j, sticky=NSEW)
                self.__table_data.append(drow)