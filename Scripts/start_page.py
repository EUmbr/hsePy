"""
Модуль для создания стартовой страницы
Авторы: Умбрас Е., Попов Н. БИВ182
"""
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd
from library import load_data
from parametres import title_font


class StartPage(tk.Frame):
    """
    Класс для создания и настройки стартовой страницы
    """
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        ttk.Label(self, text='Открытая База Результатов Олимпиад',
                  font=title_font).place(x=110, y=60)

        btn1 = ttk.Button(self, text='Открыть Базу Данных')
        btn1['command'] = self.show_base
        btn1.place(x=337, y=170, width=300, height=50)

        btn2 = ttk.Button(self, text='Создать Базу Данных')
        btn2['command'] = lambda: controller.show_frame("PageOne")
        btn2.place(x=337, y=250, width=300, height=50)

        btn2 = ttk.Button(self, text='Выход')
        btn2['command'] = self.end_progam
        btn2.place(x=337, y=400, width=300, height=50)

    def show_base(self):
        """
        Функция кнопки для вывода базы данных на экран
        Авторы: Умбрас. Е, Попов Н. БИВ182
        """
        path = askopenfilename()
        path = str(path)
        if path != "":
            fio, reg = load_data(path)
            data = pd.merge(reg, fio, on='Город')
            data = data.sort_values(by='Фамилия')

            self.controller.frames["PageOne"].data = data
        self.controller.show_frame('PageOne', data=data)

    def end_progam(self):
        """
        Функция кнопки для завершения программы
        Автор: Умбрас Е. БИВ182
        """
        self.quit()
