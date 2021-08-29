from calendar import monthrange
from tkinter import *
from datetime import date, datetime
from tkinter import ttk

today = date.today()


class AnswerTime:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return f"{self.hora}:{self.minuto}"

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

        Label(self,text="/").grid(row=0, column=1)

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
        self.month_combobox.grid(row=0,column=2)

        Label(self, text="/").grid(row=0, column=3)


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
        self.year_spinbox.grid(row=0, column=4,sticky=NS)
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

class WidgetTiempo(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        hoy = datetime.now()
        hora = str(hoy.hour)
        if len(hora)==1:
            hora = '0'+hora
        minuto = str(hoy.minute)
        if len(minuto)==1:
            minuto = '0'+minuto
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.__hora = StringVar(value=hora)
        self.hora_cb = ttk.Combobox(self, state="readonly", textvariable=self.__hora,width=4, justify=CENTER,values=[str(i) if i>9 else f'0{i}' for i in range(0,24)])
        self.hora_cb.grid(row=0, column=0,sticky=NS)
        Label(self, text=":").grid(row=0, column=1)
        self.__minuto = StringVar(value=minuto)
        self.minuto_cb = ttk.Combobox(self, state="readonly",textvariable=self.__minuto,width=4, justify=CENTER, values=[str(i) if i>9 else f'0{i}' for i in range(0, 60)])
        self.minuto_cb.grid(row=0, column=2,sticky=NS)

    def get_time(self):
        return AnswerTime(int(self.hora_cb.get()),int(self.minuto_cb.get()))

    def set_on_change(self,target):
        self.hora_cb.bind("<<ComboboxSelected>>", lambda e: target(e))
        self.minuto_cb.bind("<<ComboboxSelected>>", lambda e: target(e))