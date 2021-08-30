from datetime import date, timedelta
from tkinter import *
from tkinter import ttk

from visual.ScrollableFrame import ScrollableFrame
from visual.widgets.datetime import WidgetFecha


class ActividadesCulturalesSemanal(Toplevel):
    def __init__(self, target, controlador):
        super().__init__(target)
        self.__parent = target
        self.controller = controlador
        self.title("Actividades culturales por semana")
        self.grab_set()
        self.minsize(800, 600)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.__table_data = []

        frame_presupuesto = Frame(self)
        frame_presupuesto.grid(row=1, column=0, padx=10, pady=(10, 0), sticky=EW)
        frame_presupuesto.grid_columnconfigure(1, weight=1)
        Label(frame_presupuesto, text="Presupuesto:").grid(row=0, column=0, sticky=W)

        vcmd = (self.register(lambda P: (str.isdigit(P) or P == "")), '%P')

        self.__presupuesto_var = StringVar()
        self.__presupuesto = Entry(frame_presupuesto, validate='all', textvariable=self.__presupuesto_var,
                                   validatecommand=vcmd, justify=RIGHT)
        self.__presupuesto_var.trace_add("write", lambda a, b, c: self.__on_change())

        self.__presupuesto.grid(row=0, column=1, padx=(5, 0), sticky=EW)

        frame_fecha = Frame(self)
        frame_fecha.grid(row=2, column=0, pady=(10, 0), padx=10, sticky=NSEW)

        Label(frame_fecha, text="Fecha:").grid(row=0, column=0, sticky=W)

        self.__fecha = WidgetFecha(frame_fecha)
        self.__fecha.grid(row=0, column=1, sticky=W)
        self.__fecha.set_on_change(self.__on_change)

        Label(frame_fecha, text="Semana:").grid(row=0, column=2, padx=(15, 0), sticky=W)
        self.__msg = Label(frame_fecha)
        self.__msg.grid(row=0, column=3, sticky=W)

        frame_calif = Frame(self)
        frame_calif.grid(row=3, column=0, padx=10, pady=(10, 0), sticky=EW)
        self.__calif_bar = []
        Label(frame_calif, text="Calificaciones:").grid(row=0, column=0, sticky=W)
        for index, i in enumerate(range(1, 6)):
            self.__calif_bar.append(StringVar(value=i))
            Checkbutton(frame_calif, text=i, variable=self.__calif_bar[index],
                        onvalue=str(i), offvalue="", borderwidth=1, relief="solid",
                        command=self.__on_change).grid(row=0, column=index + 1, sticky=W)

        self.actividad_cult_table = ScrollableFrame(self)
        self.actividad_cult_table.grid(row=4, column=0, pady=(5, 0), sticky=NSEW)

        self.actividad_cult_table.scrollable_frame.grid_columnconfigure(0, weight=8)
        self.actividad_cult_table.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.actividad_cult_table.scrollable_frame.grid_columnconfigure(2, weight=1)
        self.actividad_cult_table.scrollable_frame.grid_columnconfigure(3, weight=1)
        # self.actividad_cult_table.scrollable_frame.grid_columnconfigure(4, weight=1)
        self.actividad_cult_table.scrollable_frame.grid_columnconfigure(5, weight=1)
        self.actividad_cult_table.scrollable_frame.grid_columnconfigure(6, weight=1)
        Label(self.actividad_cult_table.scrollable_frame, text=" Actividad ", borderwidth=2, relief="solid",
              justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=0,
                                    sticky=EW)
        Label(self.actividad_cult_table.scrollable_frame, text=" Provincia ", borderwidth=2, relief="solid",
              justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=1,
                                    sticky=EW)
        Label(self.actividad_cult_table.scrollable_frame, text=" Lugar ", borderwidth=2, relief="solid",
              justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=2,
                                    sticky=EW)
        Label(self.actividad_cult_table.scrollable_frame, text=" Tipo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=3,
                                    sticky=EW)
        Label(self.actividad_cult_table.scrollable_frame, text=" Calificación ", borderwidth=2, relief="solid",
              justify=CENTER, bg="light gray").grid(row=0,
                                                    column=4,
                                                    sticky=EW)
        Label(self.actividad_cult_table.scrollable_frame, text=" Fecha ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=5,
                                    sticky=EW)
        Label(self.actividad_cult_table.scrollable_frame, text=" Costo ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=6,
                                    sticky=EW)

        Button(self, text=" Volver ", command=self.destroy).grid(row=5, column=0, padx=(0, 10), pady=(5, 10), sticky=E)

        fecha_inicio = self.__fecha.get_fecha()
        while fecha_inicio.weekday() != 6:
            fecha_inicio -= timedelta(days=1)
        fecha_fin = fecha_inicio + timedelta(days=6)
        self.__msg['text'] = f"{fecha_inicio} hasta {fecha_fin}"
        self.__on_change()
        self.mainloop()

    def __on_change(self, event=None):
        fecha_inicio = self.__fecha.get_fecha()
        while fecha_inicio.weekday() != 6:
            fecha_inicio -= timedelta(days=1)
        fecha_fin = fecha_inicio + timedelta(days=6)
        self.__msg['text'] = f"{fecha_inicio} hasta {fecha_fin}"
        fechas = [fecha_inicio + timedelta(days=i) for i in range(7)]
        costo = self.__presupuesto.get()
        calificaciones = set([i.get() for i in self.__calif_bar if i.get() != ""])
        if len(costo) == 0:
            costo = None
        for row in self.__table_data:
            for col in row:
                col.destroy()
        self.__table_data.clear()

        for index, row in enumerate(
                self.controller.get_actividad_cultales_en_rango(fechas, costo, calificaciones), start=1):
            drow = [
                Label(self.actividad_cult_table.scrollable_frame, text=f" {row[0].decode('utf-8')} ", anchor=W,
                      borderwidth=1, relief="solid",
                      bg="white"),
                Label(self.actividad_cult_table.scrollable_frame, text=f" {str(row[1].args[0]).replace('_',' ').title()} ", justify=CENTER, borderwidth=1,
                      relief="solid",
                      bg="white"),
                Label(self.actividad_cult_table.scrollable_frame, text=f" {row[1].args[1].decode('utf-8')} ", anchor=E, borderwidth=1,
                      relief="solid",
                      bg="white"),
                Label(self.actividad_cult_table.scrollable_frame,
                      text=f" {row[2].decode('utf-8')} ", justify=CENTER, borderwidth=1,
                      relief="solid",
                      bg="white"),
                Label(self.actividad_cult_table.scrollable_frame,
                      text=f" {row[5]} ", justify=CENTER, borderwidth=1,
                      relief="solid",
                      bg="white"),
                Label(self.actividad_cult_table.scrollable_frame,
                      text=f" {date(row[4].args[0], row[4].args[1], row[4].args[2])} ", justify=CENTER, borderwidth=1,
                      relief="solid",
                      bg="white"),
                Label(self.actividad_cult_table.scrollable_frame,
                      text=f" {row[3]} ", justify=CENTER, borderwidth=1,
                      relief="solid",
                      bg="white")
            ]
            for j, i in enumerate(drow):
                i.grid(row=index, column=j, sticky=NSEW)
            self.__table_data.append(drow)
