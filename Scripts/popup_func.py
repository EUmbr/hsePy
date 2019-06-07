import tkinter as tk
from tkinter import ttk
from parametres import popup_getfunc_size, popup_font1


class PopupWindowFuncChoose():
    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry(popup_getfunc_size+'+550+200')
        self.top.resizable(0, 0)
        self.top.title('Сводная таблица')

        frame1 = ttk.Frame(self.top)
        frame1.pack(expand=1, fill='both')

        ttk.Label(frame1, text='Выберите функцию агрегации:',
                  font=popup_font1).pack(side='top', pady=10)

        frame2 = ttk.Frame(frame1)
        frame2.pack(side='top', fill='both')

        self.var = tk.IntVar()

        self.r1 = ttk.Radiobutton(frame2, text="Среднее значение",
                                  variable=self.var,
                                  value=0)
        self.r2 = ttk.Radiobutton(frame2,
                                  text="Среднеквадратическое отклонение",
                                  variable=self.var, value=1)

        self.r1.grid(row=0, column=0, sticky='W', padx=20, pady=5)
        self.r2.grid(row=1, column=0, sticky='W', padx=20, pady=5)

        ttk.Button(frame1, text='Создать', command=self.done).pack(pady=20)

    def done(self):
        self.atr = self.var.get()
        self.top.destroy()
