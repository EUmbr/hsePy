import tkinter as tk
from tkinter import ttk
from parametres import popup_size2, popup_font1


class PopupWindowGet1_2():
    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry(popup_size2+'+550+200')
        self.top.resizable(0, 0)
        self.top.title('Статистический отчет')

        self.f1 = ttk.Frame(self.top)
        self.f1.pack(expand=1, fill='both')

        ttk.Label(self.f1, text='Выберите атрибут',
                  font=popup_font1).pack(side='top', pady=25)

        f2 = ttk.Frame(self.f1)
        f2.pack(side='top', fill='both')

        self.var = tk.IntVar()
        self.var.set(0)

        self.r1 = ttk.Radiobutton(f2, text="Математика", variable=self.var,
                                  value=0)
        self.r2 = ttk.Radiobutton(f2, text="Русский язык", variable=self.var,
                                  value=1)
        self.r3 = ttk.Radiobutton(f2, text="Доп. предмет", variable=self.var,
                                  value=2)
        self.r4 = ttk.Radiobutton(f2, text="Доп. баллы", variable=self.var,
                                  value=3)
        self.r5 = ttk.Radiobutton(f2, text="Город", variable=self.var, value=4)
        self.r6 = ttk.Radiobutton(f2, text="Округ", variable=self.var,
                                  value=5)
        self.r7 = ttk.Radiobutton(f2, text="Все числовые атрибуты",
                                  variable=self.var, value=6)

        self.r1.grid(row=0, column=0, sticky='W', padx=20, pady=5)
        self.r2.grid(row=1, column=0, sticky='W', padx=20, pady=5)
        self.r3.grid(row=2, column=0, sticky='W', padx=20, pady=5)
        self.r4.grid(row=3, column=0, sticky='W', padx=20, pady=5)
        self.r5.grid(row=4, column=0, sticky='W', padx=20, pady=5)
        self.r6.grid(row=5, column=0, sticky='W', padx=20, pady=5)
        self.r7.grid(row=6, column=0, sticky='W', padx=20, pady=5)

        ttk.Button(self.f1, text='Создать', command=self.done).pack(pady=20)

    def done(self):
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
