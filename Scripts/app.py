"""
Модуль содержит класс для создания окна приложения
Автор: Умбрас Е.Д. БИВ182
"""
import tkinter as tk
from tkinter import ttk
from start_page import StartPage
from parametres import main_width, main_height, theme_name
from page_one import PageOne


class SampleApp(tk.Tk):
    """
    Класс, который создает главное окно
    Автор: Умбрас Е.Д. БИВ182
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        width = width//2
        height = height//2
        width = width - 400
        height = height - 250
        self.geometry('{}x{}+{}+{}'.format(main_width, main_height,
                                           width, height))
        self.resizable(0, 0)
        self.style = ttk.Style()

        self.style.theme_use(theme_name)
        self.title('База Данных')
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
        """
        Показывает фрейм с заданным именем page_name
        Автор: Умбрас Е.Д. БИВ182
        """
        if data is None:
            for i in self.frames['PageOne'].table.get_children():
                self.frames['PageOne'].table.delete(i)
        else:
            for i in self.frames['PageOne'].table.get_children():
                self.frames['PageOne'].table.delete(i)
            for i in range(len(data)):
                values = (data.iloc[i]['Фамилия'],
                          data.iloc[i]['Имя'],
                          data.iloc[i]['Математика'],
                          data.iloc[i]['Русский язык'],
                          data.iloc[i]['Доп. предмет'],
                          data.iloc[i]['Доп. баллы'],
                          data.iloc[i]['Город'],
                          data.iloc[i]['Округ'])
                self.frames['PageOne'].table.insert('', 'end', values=values)

        frame = self.frames[page_name]
        frame.tkraise()
