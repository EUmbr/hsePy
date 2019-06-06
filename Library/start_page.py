import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd
from load import load_data


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        ttk.Label(self, text='Открытая База Результатов Олимпиад',
                  font=("GothicE", 24, "bold")).place(x=45, y=60)

        btn1 = ttk.Button(self, text='Открыть Базу Данных')
        btn1['command'] = self.show_base
        btn1.place(x=280, y=170, width=300, height=50)

        btn2 = ttk.Button(self, text='Создать Базу Данных')
        btn2['command'] = lambda: controller.show_frame("PageOne")
        btn2.place(x=280, y=250, width=300, height=50)

        btn2 = ttk.Button(self, text='Выход')
        btn2['command'] = self.end_progam
        btn2.place(x=280, y=400, width=300, height=50)

    def show_base(self):
        path = askopenfilename()
        path = str(path)
        if path != "":
            data = load_data(path)
            self.data = pd.DataFrame(data).transpose()
            self.data.index = range(1000)
            self.data = self.data.astype({'Фамилия': str,
                                          'Имя': str, 'Математика': int,
                                          'Русский язык': int,
                                          'Доп. предмет': str,
                                          'Доп. баллы': int, 'Город': str})
            data_region = [['Москва', 'Центральный'],
                           ['Нижний Новгород', 'Приволжский'],
                           ['Челябинск', 'Уральский'],
                           ['Омск', 'Сибирский'],
                           ['Волгоград', 'Южный'],
                           ['Новосибирск', 'Сибирский'],
                           ['Казань', 'Приволжский'],
                           ['Екатеринбург', 'Уральский'],
                           ['Самара', 'Приволжский'],
                           ['Пермь', 'Приволжский'],
                           ['Санкт-Петербург', 'Северо-Западный'],
                           ['Уфа', 'Приволжский'],
                           ['Воронеж', 'Центральный'],
                           ['Ростов-на-Дону', 'Южный'],
                           ['Красноярск', 'Сибирский']]
            self.region = pd.DataFrame(data_region, columns=('Город', 'Округ'))
            print(self.region)
            self.controller.frames["PageOne"].data = self.data
        self.controller.show_frame('PageOne', data=data)

    def end_progam(self):
        self.quit()
