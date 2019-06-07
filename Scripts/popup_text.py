"""
Модуль для создания простого текстового отчета
Авторы: Зайцев С., Умбрас Е. БИВ182
"""
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
from parametres import popup_size1, popup_font1, popup_font2
from parametres import popup_text_warning1, popup_text_warning2
from parametres import popup_text_warning_mat, popup_text_warning_rus
from parametres import popup_text_warning_dop


class PopupWindowGet1():
    """
    Класс для создания окна конфигурации текстового отчета
    Автор: Зайцев С., Умбрас Е.
    """
    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry(popup_size1+'+550+200')
        self.top.resizable(0, 0)
        self.top.title('Текстовый отчет')

        self.frame1 = ttk.Frame(self.top)
        self.frame1.pack(expand=1, fill='both')

        ttk.Label(self.frame1, text='Выберите отображаемые\nстолбцы:',
                  font=popup_font1).pack(side='top', pady=8)

        self.sur_var = tk.IntVar()
        self.name_var = tk.IntVar()
        self.mat_var = tk.IntVar()
        self.rus_var = tk.IntVar()
        self.dopex_var = tk.IntVar()
        self.dopemark_var = tk.IntVar()
        self.city_var = tk.IntVar()
        self.region_var = tk.IntVar()

        frame2 = ttk.Frame(self.frame1)
        frame2.pack(side='top', fill='both')

        self.check1 = tk.Checkbutton(frame2, text="Фамилия",
                                     font=popup_font2,
                                     variable=self.sur_var, onvalue=1,
                                     offvalue=0)
        self.check2 = tk.Checkbutton(frame2, text="Имя",
                                     font=popup_font2,
                                     variable=self.name_var, onvalue=1,
                                     offvalue=0)
        self.check3 = tk.Checkbutton(frame2,
                                     text="Математика",
                                     font=popup_font2,
                                     variable=self.mat_var, onvalue=1,
                                     offvalue=0)
        self.check4 = tk.Checkbutton(frame2, text="Русский язык",
                                     font=popup_font2,
                                     variable=self.rus_var, onvalue=1,
                                     offvalue=0)
        self.check5 = tk.Checkbutton(frame2, text="Доп. предмет",
                                     font=popup_font2,
                                     variable=self.dopex_var, onvalue=1,
                                     offvalue=0)
        self.check6 = tk.Checkbutton(frame2, text="Доп. баллы",
                                     font=popup_font2,
                                     variable=self.dopemark_var,
                                     onvalue=1, offvalue=0)
        self.check7 = tk.Checkbutton(frame2, text="Город",
                                     font=popup_font2,
                                     variable=self.city_var, onvalue=1,
                                     offvalue=0)
        self.check8 = tk.Checkbutton(frame2, text="Округ",
                                     font=popup_font2,
                                     variable=self.region_var, onvalue=1,
                                     offvalue=0)

        self.check1.grid(row=0, column=0, sticky='W', padx=20, pady=5)
        self.check2.grid(row=1, column=0, sticky='W', padx=20, pady=5)
        self.check3.grid(row=2, column=0, sticky='W', padx=20, pady=5)
        self.check4.grid(row=3, column=0, sticky='W', padx=20, pady=5)
        self.check5.grid(row=4, column=0, sticky='W', padx=20, pady=5)
        self.check6.grid(row=5, column=0, sticky='W', padx=20, pady=5)
        self.check7.grid(row=6, column=0, sticky='W', padx=20, pady=5)
        self.check8.grid(row=7, column=0, sticky='W', padx=20, pady=5)

        ttk.Button(self.frame1, text='Далее', command=self.next).pack(pady=10)

    def next(self):
        """
        Функция для создания фрейма выбора значений атрибутов
        Авторы: Зайцев С., Умбрас Е
        """
        self.cols = []
        if self.sur_var.get():
            self.cols.append(self.check1['text'])
        if self.name_var.get():
            self.cols.append(self.check2['text'])
        if self.mat_var.get():
            self.cols.append(self.check3['text'])
        if self.rus_var.get():
            self.cols.append(self.check4['text'])
        if self.dopex_var.get():
            self.cols.append(self.check5['text'])
        if self.dopemark_var.get():
            self.cols.append(self.check6['text'])
        if self.city_var.get():
            self.cols.append(self.check7['text'])
        if self.region_var.get():
            self.cols.append(self.check8['text'])

        if self.cols:

            self.frame1.pack_forget()

            frame3 = ttk.Frame(self.top)
            frame3.pack(expand=1, fill='both')

            ttk.Label(frame3, text='Выберите критерии',
                      font=popup_font2).pack(side='top', pady=25)

            frame4 = ttk.Frame(frame3)
            frame4.pack(side='top', fill='both')

            ttk.Label(frame4, text='Математика',
                      font=popup_font2).grid(row=0, column=0,
                                             columnspan=2, pady=10,
                                             padx=10, sticky='W')
            ttk.Label(frame4, text='От',
                      font=popup_font2).grid(row=1, column=0,
                                             pady=10, padx=10,
                                             sticky='W')

            self.spin1 = ttk.Spinbox(frame4, from_=20, to=100, width=5)
            self.spin1.grid(row=1, column=1)

            ttk.Label(frame4, text='до',
                      font=popup_font2).grid(row=1, column=3, pady=10,
                                             padx=10, sticky='W')

            self.spin2 = ttk.Spinbox(frame4, from_=20, to=100, width=5)
            self.spin2.grid(row=1, column=4)

            ttk.Label(frame4, text='Русский язык',
                      font=popup_font2).grid(row=2, column=0,
                                             columnspan=2, pady=10,
                                             padx=10, sticky='W')
            ttk.Label(frame4, text='От',
                      font=popup_font2).grid(row=3, column=0,
                                             pady=10, padx=10,
                                             sticky='W')

            self.spin3 = ttk.Spinbox(frame4, from_=20, to=100, width=5)
            self.spin3.grid(row=3, column=1)

            ttk.Label(frame4, text='до',
                      font=popup_font2).grid(row=3, column=3,
                                             pady=10, padx=10,
                                             sticky='W')

            self.spin4 = ttk.Spinbox(frame4, from_=20, to=100, width=5)
            self.spin4.grid(row=3, column=4)

            ttk.Label(frame4, text='Доп. предмет',
                      font=popup_font2).grid(row=4, column=0,
                                             columnspan=2, pady=10,
                                             padx=10, sticky='W')
            ttk.Label(frame4, text='От',
                      font=popup_font2).grid(row=5, column=0,
                                             pady=10, padx=10,
                                             sticky='W')

            self.spin5 = ttk.Spinbox(frame4, from_=20, to=100, width=5)
            self.spin5.grid(row=5, column=1)

            ttk.Label(frame4, text='до',
                      font=popup_font2).grid(row=5, column=3,
                                             pady=10, padx=10,
                                             sticky='W')

            self.spin6 = ttk.Spinbox(frame4, from_=20, to=100, width=5)
            self.spin6.grid(row=5, column=4)

            ttk.Button(frame3, text='Создать', command=self.done).pack(pady=35)
        else:
            mb.showwarning('Warning', popup_text_warning1, parent=self.top)

    def done(self):
        """
        Функция получения значений полей выбора
        Автор: Зайцев С., Умбрас Е.
        """
        self.mat_max = self.rus_max = self.dop_max = -1
        self.mat_min = self.rus_min = self.dop_min = -1
        err_code = 0
        if (any(not(char.isdigit()) for char in self.spin1.get()))or\
           (any(not(char.isdigit()) for char in self.spin2.get()))or\
           (any(not(char.isdigit()) for char in self.spin3.get()))or\
           (any(not(char.isdigit()) for char in self.spin4.get()))or\
           (any(not(char.isdigit()) for char in self.spin5.get()))or\
           (any(not(char.isdigit()) for char in self.spin6.get())):
            mb.showwarning('Warning', popup_text_warning2,
                           parent=self.top)

        else:
            if (self.spin1.get())and(self.spin2.get())and\
               (int(self.spin1.get()) <= int(self.spin2.get()))and\
               (int(self.spin2.get()) <= 100):
                self.mat_min = int(self.spin1.get())
                self.mat_max = int(self.spin2.get())
            elif not (self.spin1.get() or self.spin2.get()):
                self.mat_min = 0
                self.mat_max = 100
            else:
                mb.showwarning('Warning',
                               popup_text_warning_mat,
                               parent=self.top)
                self.mat_min = -1
                self.mat_max = -1
                err_code = 1

            if (self.spin3.get())and(self.spin4.get())and\
               (int(self.spin3.get()) <= int(self.spin4.get())):
                self.rus_min = int(self.spin3.get())
                self.rus_max = int(self.spin4.get())
            elif not (self.spin3.get() or self.spin4.get()):
                self.rus_min = 0
                self.rus_max = 100
            else:
                mb.showwarning('Warning',
                               popup_text_warning_rus,
                               parent=self.top)
                self.rus_min = -1
                self.rus_max = -1
                err_code = 1

            if (self.spin5.get())and(self.spin6.get())and\
               (int(self.spin5.get()) <= int(self.spin6.get())):
                self.dop_min = int(self.spin5.get())
                self.dop_max = int(self.spin6.get())
            elif not (self.spin5.get() or self.spin6.get()):
                self.dop_min = 0
                self.dop_max = 100
            else:
                mb.showwarning('Warning',
                               popup_text_warning_dop,
                               parent=self.top)
                self.dop_min = -1
                self.dop_max = -1
                err_code = 1

            if not err_code:
                self.top.destroy()
