"""
Модуль для создания простого текстового отчета
Авторы: Зайцев С., Умбрас Е., Ушаков В. БИВ182
"""
import tkinter as tk
from tkinter import ttk
from parametres import popup_size2, popup_font1


class PopupWindowGet2():
    """
    Класс для создания окна конфигурации статистического отчета
    Автор: Зайцев С., Умбрас Е., Ушаков В. БИВ182
    """
    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry(popup_size2+'+550+200')
        self.top.resizable(0, 0)
        self.top.title('Статистический отчет')

        self.frame1 = ttk.Frame(self.top)
        self.frame1.pack(expand=1, fill='both')

        ttk.Label(self.frame1, text='Выберите атрибут',
                  font=popup_font1).pack(side='top', pady=25)

        frame2 = ttk.Frame(self.frame1)
        frame2.pack(side='top', fill='both')

        self.var = tk.IntVar()
        self.var.set(0)

        self.radio1 = ttk.Radiobutton(frame2, text="Математика",
                                      variable=self.var, value=0)
        self.radio2 = ttk.Radiobutton(frame2, text="Русский язык",
                                      variable=self.var, value=1)
        self.radio3 = ttk.Radiobutton(frame2, text="Доп. предмет",
                                      variable=self.var, value=2)
        self.radio4 = ttk.Radiobutton(frame2, text="Доп. баллы",
                                      variable=self.var, value=3)
        self.radio5 = ttk.Radiobutton(frame2, text="Город",
                                      variable=self.var, value=4)
        self.radio6 = ttk.Radiobutton(frame2, text="Округ", variable=self.var,
                                      value=5)
        self.radio7 = ttk.Radiobutton(frame2, text="Все числовые атрибуты",
                                      variable=self.var, value=6)

        self.radio1.grid(row=0, column=0, sticky='W', padx=20, pady=5)
        self.radio2.grid(row=1, column=0, sticky='W', padx=20, pady=5)
        self.radio3.grid(row=2, column=0, sticky='W', padx=20, pady=5)
        self.radio4.grid(row=3, column=0, sticky='W', padx=20, pady=5)
        self.radio5.grid(row=4, column=0, sticky='W', padx=20, pady=5)
        self.radio6.grid(row=5, column=0, sticky='W', padx=20, pady=5)
        self.radio7.grid(row=6, column=0, sticky='W', padx=20, pady=5)

        ttk.Button(self.frame1, text='Создать', command=self.done).pack(pady=20)

    def done(self):
        """
        Функция получения значений полей выбора
        Автор: Зайцев С., Умбрас Е., Ушаков В. БИВ182
        """
        if self.var.get() == 0:
            self.atr = 'Математика'
        elif self.var.get() == 1:
            self.atr = 'Русский'
        elif self.var.get() == 2:
            self.atr = 'Доп. предмет'
        elif self.var.get() == 3:
            self.atr = 'Доп. баллы'
        elif self.var.get() == 4:
            self.atr = 'Город'
        elif self.var.get() == 5:
            self.atr = 'Округ'
        elif self.var.get() == 6:
            self.atr = ''
        self.top.destroy()
