import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb


class PopupWindowChange():
    def __init__(self, values):
        self.values = values
        self.top = tk.Toplevel()
        self.top.geometry('300x400+550+200')
        self.top.resizable(0, 0)

        frame1 = ttk.Frame(self.top)
        frame1.pack(expand=1, fill='both')

        ttk.Label(frame1, text='Измените данные:',
                  font=('Helvetica', 16)).pack(side='top', pady=10)

        frame2 = ttk.Frame(frame1)
        frame2.pack(side='top', fill='both')
        ttk.Label(frame2, text='Фамилия',
                  font=('Helvetica', 12)).grid(row=0, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Имя',
                  font=('Helvetica', 12)).grid(row=1, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Математика',
                  font=('Helvetica', 12)).grid(row=2, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Русский язык',
                  font=('Helvetica', 12)).grid(row=3, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Доп. предмет',
                  font=('Helvetica', 12)).grid(row=4, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Доп. баллы',
                  font=('Helvetica', 12)).grid(row=5, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Город',
                  font=('Helvetica', 12)).grid(row=6, column=0,
                                               pady=10, padx=10,
                                               sticky='W')

        self.surname_entry = ttk.Entry(frame2, width=27)
        self.surname_entry.insert('end', self.values[0])
        self.surname_entry.grid(row=0, column=1)
        self.name_entry = ttk.Entry(frame2, width=27)
        self.name_entry.insert('end', self.values[1])
        self.name_entry.grid(row=1, column=1)
        self.mat_entry = ttk.Entry(frame2, width=27)
        self.mat_entry.insert('end', self.values[2])
        self.mat_entry.grid(row=2, column=1)
        self.rus_entry = ttk.Entry(frame2, width=27)
        self.rus_entry.insert('end', self.values[3])
        self.rus_entry.grid(row=3, column=1)
        self.dopex_entry = ttk.Entry(frame2, width=27)
        self.dopex_entry.insert('end', self.values[4])
        self.dopex_entry.grid(row=4, column=1)
        self.dopmark_entry = ttk.Entry(frame2, width=27)
        self.dopmark_entry.insert('end', self.values[5])
        self.dopmark_entry.grid(row=5, column=1)
        self.city_entry = ttk.Entry(frame2, width=27)
        self.city_entry.insert('end', self.values[6])
        self.city_entry.grid(row=6, column=1)

        butt = ttk.Button(frame1, text='Готово')
        butt.pack(side='top', pady=10)
        butt['command'] = self.done

    def done(self):
        surname = self.surname_entry.get()
        if not surname.isalpha():
            mb.showwarning('Warning', 'Данные введены неверно',
                           parent=self.top)
            return

        name = self.name_entry.get()
        if not name.isalpha():
            mb.showwarning('Warning', 'Данные введены неверно',
                           parent=self.top)
            return

        mat = self.mat_entry.get()
        if (not mat.isdigit()) or int(mat) < 1 or\
                (int(mat) > 100):
            mb.showwarning('Warning', 'Данные введены неверно',
                           parent=self.top)
            return

        rus = self.rus_entry.get()
        if (not rus.isdigit()) or int(rus) < 1 or\
                (int(rus) > 100):
            mb.showwarning('Warning', 'Данные введены неверно',
                           parent=self.top)
            return

        dopex = self.dopex_entry.get()
        if any(char.isdigit() for char in dopex):
            mb.showwarning('Warning', 'Данные введены неверно',
                           parent=self.top)
            return

        dopmark = self.dopmark_entry.get()
        if (not dopmark.isdigit()) or int(dopmark) < 1 or\
                (int(dopmark) > 100):
            mb.showwarning('Warning', 'Данные введены неверно',
                           parent=self.top)
            return

        city = self.city_entry.get()
        if any(char.isdigit() for char in city):
            mb.showwarning('Warning', 'Данные введены неверно',
                           parent=self.top)
            return

        self.top.destroy()
