import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from start_page import StartPage
from page_one import PageOne


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18,
                                      weight="bold", slant="italic")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        width = width//2
        height = height//2
        width = width - 400
        height = height - 250
        self.geometry('860x500+{}+{}'.format(width, height))
        self.resizable(0, 0)
        self.style = ttk.Style()

        self.style.theme_use('vista')
        self.title('App')
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(parent=container, controller=self)
        self.frames["StartPage"] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        frame = PageOne(parent=container, controller=self)
        self.frames["PageOne"] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name, data=None):
        '''Show a frame for the given page name'''
        if data:
            for i in self.frames['PageOne'].table.get_children():
                self.frames['PageOne'].table.delete(i)
            for val in data.values():
                self.frames['PageOne'].table.insert('', 'end',
                                                    values=tuple(val.values()))
        else:
            for i in self.frames['PageOne'].table.get_children():
                self.frames['PageOne'].table.delete(i)
        frame = self.frames[page_name]
        frame.tkraise()
