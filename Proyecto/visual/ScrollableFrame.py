from tkinter import *
from tkinter import ttk


class ScrollableFrame(ttk.Frame):  # https://blog.teclado.com/tkinter-scrollable-frames/
    def __init__(self, container, horizontal_s=False, vertical_s=True, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.__canvas = Canvas(self, width=1)
        self.scrollable_frame = Frame(self.__canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.__canvas.configure(
                scrollregion=self.__canvas.bbox("all")
            )
        )
        self.__canvas.bind('<Enter>', self.__bound_to_mousewheel)
        self.__canvas.bind('<Leave>', self.__unbound_to_mousewheel)

        self.__canvas.bind(
            "<Configure>", self.__canvas_resize
        )

        if horizontal_s:
            hsb = Scrollbar(self, orient=HORIZONTAL, command=self.__canvas.xview)
            self.__canvas.configure(xscrollcommand=hsb.set)
            hsb.grid(row=1, column=0, sticky=EW)

        if vertical_s:
            vsb = Scrollbar(self, orient=VERTICAL, command=self.__canvas.yview)
            self.__canvas.configure(yscrollcommand=vsb.set)
            vsb.grid(row=0, column=1, sticky=NS)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.__canvas.create_window((0, 0), window=self.scrollable_frame, anchor=NW, tags="frame")
        self.__canvas.grid(row=0, column=0, sticky=NSEW)

    def __bound_to_mousewheel(self, event):
        self.__canvas.bind_all("<MouseWheel>", self.__y_scrolling)

    def __canvas_resize(self, event):
        self.__canvas.itemconfig('frame', width=self.__canvas.winfo_width()-2)

    def __unbound_to_mousewheel(self, event):
        self.__canvas.unbind_all("<MouseWheel>")

    def __y_scrolling(self, event):
        if self.__canvas.yview() != (0.0, 1.0):
            self.__canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def reset_scroll(self):
        self.__canvas.yview_moveto(0)
        self.__canvas.xview_moveto(0)
