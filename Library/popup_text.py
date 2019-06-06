import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb


class PopupWindowGet1_1():
    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry('300x400+550+200')
        self.top.resizable(0, 0)

        self.f1 = ttk.Frame(self.top)
        self.f1.pack(expand=1, fill='both')

        ttk.Label(self.f1, text='Выберите отображаемые\nстолбцы:',
                  font=('Helvetica', 16)).pack(side='top', pady=10)

        self.SurVar = tk.IntVar()
        self.NameVar = tk.IntVar()
        self.MatVar = tk.IntVar()
        self.RusVar = tk.IntVar()
        self.DopexVar = tk.IntVar()
        self.DopemarkVar = tk.IntVar()
        self.CityVar = tk.IntVar()

        f2 = ttk.Frame(self.f1)
        f2.pack(side='top', fill='both')

        self.C1 = tk.Checkbutton(f2, text="Фамилия",
                                 font=('Helvetica', 12),
                                 variable=self.SurVar, onvalue=1, offvalue=0)
        self.C2 = tk.Checkbutton(f2, text="Имя",
                                 font=('Helvetica', 12),
                                 variable=self.NameVar, onvalue=1, offvalue=0)
        self.C3 = tk.Checkbutton(f2,
                                 text="Математика",
                                 font=('Helvetica', 12),
                                 variable=self.MatVar, onvalue=1, offvalue=0)
        self.C4 = tk.Checkbutton(f2, text="Русский язык",
                                 font=('Helvetica', 12),
                                 variable=self.RusVar, onvalue=1, offvalue=0)
        self.C5 = tk.Checkbutton(f2, text="Доп. предмет",
                                 font=('Helvetica', 12),
                                 variable=self.DopexVar, onvalue=1, offvalue=0)
        self.C6 = tk.Checkbutton(f2, text="Доп. баллы",
                                 font=('Helvetica', 12),
                                 variable=self.DopemarkVar,
                                 onvalue=1, offvalue=0)
        self.C7 = tk.Checkbutton(f2, text="Город",
                                 font=('Helvetica', 12),
                                 variable=self.CityVar, onvalue=1, offvalue=0)

        self.C1.grid(row=0, column=0, sticky='W', padx=20, pady=5)
        self.C2.grid(row=1, column=0, sticky='W', padx=20, pady=5)
        self.C3.grid(row=2, column=0, sticky='W', padx=20, pady=5)
        self.C4.grid(row=3, column=0, sticky='W', padx=20, pady=5)
        self.C5.grid(row=4, column=0, sticky='W', padx=20, pady=5)
        self.C6.grid(row=5, column=0, sticky='W', padx=20, pady=5)
        self.C7.grid(row=6, column=0, sticky='W', padx=20, pady=5)

        ttk.Button(self.f1, text='Далее', command=self.next).pack(pady=10)

    def next(self):
        self.cols = []
        if self.SurVar.get():
            self.cols.append(self.C1['text'])
        if self.NameVar.get():
            self.cols.append(self.C2['text'])
        if self.MatVar.get():
            self.cols.append(self.C3['text'])
        if self.RusVar.get():
            self.cols.append(self.C4['text'])
        if self.DopexVar.get():
            self.cols.append(self.C5['text'])
        if self.DopemarkVar.get():
            self.cols.append(self.C6['text'])
        if self.CityVar.get():
            self.cols.append(self.C7['text'])

        if self.cols:

            self.f1.pack_forget()

            f3 = ttk.Frame(self.top)
            f3.pack(expand=1, fill='both')

            ttk.Label(f3, text='Выберите критерии',
                      font=('Helvetica', 16)).pack(side='top', pady=25)

            f4 = ttk.Frame(f3)
            f4.pack(side='top', fill='both')

            ttk.Label(f4, text='Математика',
                      font=('Helvetica', 12)).grid(row=0, column=0,
                                                   columnspan=2, pady=10,
                                                   padx=10, sticky='W')
            ttk.Label(f4, text='От',
                      font=('Helvetica', 12)).grid(row=1, column=0,
                                                   pady=10, padx=10,
                                                   sticky='W')

            self.w1 = ttk.Spinbox(f4, from_=20, to=100, width=5)
            self.w1.grid(row=1, column=1)

            ttk.Label(f4, text='до',
                      font=('Helvetica', 12)).grid(row=1, column=3, pady=10,
                                                   padx=10, sticky='W')

            self.w2 = ttk.Spinbox(f4, from_=20, to=100, width=5)
            self.w2.grid(row=1, column=4)

            ttk.Label(f4, text='Русский язык',
                      font=('Helvetica', 12)).grid(row=2, column=0,
                                                   columnspan=2, pady=10,
                                                   padx=10, sticky='W')
            ttk.Label(f4, text='От',
                      font=('Helvetica', 12)).grid(row=3, column=0,
                                                   pady=10, padx=10,
                                                   sticky='W')

            self.w3 = ttk.Spinbox(f4, from_=20, to=100, width=5)
            self.w3.grid(row=3, column=1)

            ttk.Label(f4, text='до',
                      font=('Helvetica', 12)).grid(row=3, column=3,
                                                   pady=10, padx=10,
                                                   sticky='W')

            self.w4 = ttk.Spinbox(f4, from_=20, to=100, width=5)
            self.w4.grid(row=3, column=4)

            ttk.Label(f4, text='Доп. предмет',
                      font=('Helvetica', 12)).grid(row=4, column=0,
                                                   columnspan=2, pady=10,
                                                   padx=10, sticky='W')
            ttk.Label(f4, text='От',
                      font=('Helvetica', 12)).grid(row=5, column=0,
                                                   pady=10, padx=10,
                                                   sticky='W')

            self.w5 = ttk.Spinbox(f4, from_=20, to=100, width=5)
            self.w5.grid(row=5, column=1)

            ttk.Label(f4, text='до',
                      font=('Helvetica', 12)).grid(row=5, column=3,
                                                   pady=10, padx=10,
                                                   sticky='W')

            self.w6 = ttk.Spinbox(f4, from_=20, to=100, width=5)
            self.w6.grid(row=5, column=4)

            ttk.Button(f3, text='Создать', command=self.done).pack(pady=20)
        else:
            mb.showwarning('Warning', 'Выберите столбцы', parent=self.top)

    def done(self):
        self.mat_max = self.rus_max = self.dop_max = -1
        self.mat_min = self.rus_min = self.dop_min = -1
        err_code = 0
        if (any(not(char.isdigit()) for char in self.w1.get()))or\
           (any(not(char.isdigit()) for char in self.w2.get()))or\
           (any(not(char.isdigit()) for char in self.w3.get()))or\
           (any(not(char.isdigit()) for char in self.w4.get()))or\
           (any(not(char.isdigit()) for char in self.w5.get()))or\
           (any(not(char.isdigit()) for char in self.w6.get())):
            mb.showwarning('Warning', 'Данные должны включать только числа',
                           parent=self.top)

        else:
            if (self.w1.get())and(self.w2.get())and\
               (int(self.w1.get()) <= int(self.w2.get()))and\
               (int(self.w2.get()) <= 100):
                self.mat_min = int(self.w1.get())
                self.mat_max = int(self.w2.get())
                print(type(self.mat_max))
                print(self.mat_min, self.mat_max)
            elif not (self.w1.get() or self.w2.get()):
                self.mat_min = 0
                self.mat_max = 100
            else:
                mb.showwarning('Warning',
                               'Данные о математике введены неверно',
                               parent=self.top)
                self.mat_min = -1
                self.mat_max = -1
                err_code = 1

            if (self.w3.get())and(self.w4.get())and\
               (int(self.w3.get()) <= int(self.w4.get())):
                self.rus_min = int(self.w3.get())
                self.rus_max = int(self.w4.get())
                print(self.rus_min, self.rus_max)
            elif not (self.w3.get() or self.w4.get()):
                self.rus_min = 0
                self.rus_max = 100
            else:
                mb.showwarning('Warning',
                               'Данные о русском языке введены неверно',
                               parent=self.top)
                self.rus_min = -1
                self.rus_max = -1
                err_code = 1

            if (self.w5.get())and(self.w6.get())and\
               (int(self.w5.get()) <= int(self.w6.get())):
                self.dop_min = int(self.w5.get())
                self.dop_max = int(self.w6.get())
                print(self.dop_min, self.dop_max)
            elif not (self.w5.get() or self.w6.get()):
                self.dop_min = 0
                self.dop_max = 100
            else:
                mb.showwarning('Warning',
                               'Данные о доп. предмете введены неверно',
                               parent=self.top)
                self.dop_min = -1
                self.dop_max = -1
                err_code = 1

            if not err_code:
                self.top.destroy()
