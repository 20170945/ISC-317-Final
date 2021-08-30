from tkinter import *
from tkinter import ttk

from visual.ScrollableFrame import ScrollableFrame


class Lista_Peliculas(Toplevel):
    def __init__(self, target, cinema_title, datos):
        super().__init__(target)
        self.__parent = target
        self.title(f"Películas en [{cinema_title}]")
        self.grab_set()
        self.minsize(800, 300)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        Button(self, text=" Volver ", command=self.destroy).grid(row=1, column=0, padx=(0, 10), pady=(5, 10), sticky=E)
        peliculas = ScrollableFrame(self)
        peliculas.grid(row=0, column=0, sticky=NSEW)

        peliculas.scrollable_frame.grid_columnconfigure(0, weight=6)
        # peliculas.scrollable_frame.grid_columnconfigure(1, weight=1)
        peliculas.scrollable_frame.grid_columnconfigure(2, weight=1)
        peliculas.scrollable_frame.grid_columnconfigure(3, weight=1)
        peliculas.scrollable_frame.grid_columnconfigure(4, weight=1)
        peliculas.scrollable_frame.grid_columnconfigure(5, weight=1)
        Label(peliculas.scrollable_frame, text=" Título ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=0,
                                    sticky=EW)
        Label(peliculas.scrollable_frame, text=" Calificación ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=1,
                                    sticky=EW)
        Label(peliculas.scrollable_frame, text=" Horario ", borderwidth=2, relief="solid", justify=CENTER,
              bg="light gray").grid(row=0,
                                    column=2,
                                    sticky=EW)
        Label(peliculas.scrollable_frame, text=" Duración ", borderwidth=2, relief="solid",
              justify=CENTER, bg="light gray").grid(row=0,
                                                    column=3,
                                                    sticky=EW)
        Label(peliculas.scrollable_frame, text=" Precio ", borderwidth=2, relief="solid",
              justify=CENTER, bg="light gray").grid(row=0,
                                                    column=4,
                                                    sticky=EW)
        Label(peliculas.scrollable_frame, text=" Generos ", borderwidth=2, relief="solid",
              justify=CENTER, bg="light gray").grid(row=0,
                                                    column=5,
                                                    sticky=EW)

        def check_dd(number):
            if number > 9:
                return number
            return f'0{number}'

        for index, row in enumerate(datos, start=1):
            Label(peliculas.scrollable_frame, text=f" {row[0].decode('utf-8')} ", anchor=W, borderwidth=1,
                  relief="solid",
                  bg="white").grid(row=index, column=0, sticky=NSEW)
            Label(peliculas.scrollable_frame, text=f" {row[2]} ", justify=CENTER, borderwidth=1,
                  relief="solid",
                  bg="white").grid(row=index, column=1, sticky=NSEW)
            horarios = Frame(peliculas.scrollable_frame, borderwidth=1,
                             relief="solid",
                             bg="white")
            horarios.grid_columnconfigure(0, weight=1)
            horarios.grid(row=index, column=2, sticky=NSEW)
            for index_h, horario in enumerate(row[4]):
                Label(horarios, text=f" {check_dd(horario.args[0])}:{check_dd(horario.args[1])} ", justify=CENTER,
                      borderwidth=1,
                      relief="solid",
                      bg="white").grid(row=index_h, column=0, sticky=NSEW)
                horarios.grid_rowconfigure(index_h, weight=1)
            Label(peliculas.scrollable_frame, text=f" {check_dd(row[5].args[0])}:{check_dd(row[5].args[1])} ",
                  justify=CENTER, borderwidth=1,
                  relief="solid",
                  bg="white").grid(row=index, column=3, sticky=NSEW)
            Label(peliculas.scrollable_frame, text=f" {row[1]} ", justify=RIGHT, borderwidth=1,
                  relief="solid",
                  bg="white").grid(row=index, column=4, sticky=NSEW)

            generos = Frame(peliculas.scrollable_frame, borderwidth=1,
                             relief="solid",
                             bg="white")
            generos.grid_columnconfigure(0, weight=1)
            generos.grid(row=index, column=5, sticky=NSEW)
            for index_g, genero in enumerate(row[6]):
                Label(generos, text=f" {str(genero).replace('_', ' ').title()} ", justify=CENTER,
                      borderwidth=1,
                      relief="solid",
                      bg="white").grid(row=index_g, column=0, sticky=NSEW)
                generos.grid_rowconfigure(index_g, weight=1)

        self.mainloop()
