from calendar import monthrange
from tkinter import *
from datetime import date
from tkinter import ttk

today = date.today()

class WidgetFecha(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        hoy = date.today()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        current_value = StringVar(value=0)

        self.__day = StringVar(value=hoy.day)
        vday = (self.register(lambda P: (str.isdigit(P) and len(P) <= 2) or P == ""), '%P')
        self.day_spinbox = Spinbox(
            self,
            from_=1,
            to=31,
            textvariable=self.__day,
            wrap=True,
            validate=ALL,
            validatecommand=vday,
            justify=RIGHT,
            width=5
        )
        self.day_spinbox.grid(row=0, column=0,sticky=NS)

        self.month_combobox =ttk.Combobox(self, state="readonly", justify=CENTER,
                                      values=[
                                          "Enero",
                                          "Febrero",
                                          "Marzo",
                                          "Abril",
                                          "Mayo",
                                          "Junio",
                                          "Julio",
                                          "Agosto",
                                          "Septiembre",
                                          "Octubre",
                                          "Noviembre",
                                          "Diciembre"
                                      ])
        self.month_combobox.current(hoy.month-1)
        self.month_combobox.grid(row=0,column=1)


        self.__year = StringVar(value=hoy.year)
        vyear = (self.register(lambda P:(str.isdigit(P) and len(P)<=4) or P==""), '%P')
        self.year_spinbox = Spinbox(
            self,
            from_=1,
            to=9999,
            textvariable=self.__year,
            wrap=True,
            validate=ALL,
            validatecommand=vyear,
            justify=RIGHT,
            width=7
        )
        self.year_spinbox.grid(row=0, column=2,sticky=NS)
        self.set_day_limit()

    def get_fecha(self):
        year = self.__year.get()
        day = self.__day.get()
        fecha = None
        try:
            fecha = date(int(year),self.month_combobox.current()+1,int(day))
        except:
            print("Error en creacion de la fecha")
        return fecha

    def set_day_limit(self):
        year = self.__year.get()
        if year=="":
            return
        max_day = monthrange(int(year),self.month_combobox.current()+1)[1]
        self.day_spinbox["to"]=max_day
        day = self.__day.get()
        if day == "" or int(day) < 1:
            self.__day.set(1)
            day = 1
        if int(day)>max_day:
            self.__day.set(max_day)




    def set_on_change(self, target):
        self.__day.trace("w", lambda name, index, mode, sv=self.__day: target())
        self.month_combobox.bind("<<ComboboxSelected>>", lambda e:(self.set_day_limit(),target(e)))
        self.__year.trace("w", lambda name, index, mode, sv=self.__year: (self.set_day_limit(),target()))

