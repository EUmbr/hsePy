import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
from parametres import popup_size1, popup_font1, popup_font2, warning


class PopupWindowAdd():
    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry(popup_size1+'+550+200')
        self.top.resizable(0, 0)
        self.top.title('Добавление элемента')

        frame1 = ttk.Frame(self.top)
        frame1.pack(expand=1, fill='both')

        ttk.Label(frame1, text='Заполните данные:',
                  font=popup_font1).pack(side='top', pady=10)

        frame2 = ttk.Frame(frame1)
        frame2.pack(side='top', fill='both')
        ttk.Label(frame2, text='Фамилия',
                  font=popup_font2).grid(row=0, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Имя',
                  font=popup_font2).grid(row=1, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Математика',
                  font=popup_font2).grid(row=2, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Русский язык',
                  font=popup_font2).grid(row=3, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Доп. предмет',
                  font=popup_font2).grid(row=4, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Доп. баллы',
                  font=popup_font2).grid(row=5, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Город',
                  font=popup_font2).grid(row=6, column=0,
                                               pady=10, padx=10,
                                               sticky='W')
        ttk.Label(frame2, text='Округ',
                  font=popup_font2).grid(row=7, column=0,
                                               pady=10, padx=10,
                                               sticky='W')

        self.surname_entry = ttk.Entry(frame2, width=27)
        self.surname_entry.grid(row=0, column=1)
        self.name_entry = ttk.Entry(frame2, width=27)
        self.name_entry.grid(row=1, column=1)
        self.mat_entry = ttk.Entry(frame2, width=27)
        self.mat_entry.grid(row=2, column=1)
        self.rus_entry = ttk.Entry(frame2, width=27)
        self.rus_entry.grid(row=3, column=1)
        self.dopex_entry = ttk.Entry(frame2, width=27)
        self.dopex_entry.grid(row=4, column=1)
        self.dopmark_entry = ttk.Entry(frame2, width=27)
        self.dopmark_entry.grid(row=5, column=1)
        self.city_entry = ttk.Entry(frame2, width=27)
        self.city_entry.grid(row=6, column=1)
        self.region_entry = ttk.Entry(frame2, width=27)
        self.region_entry.grid(row=7, column=1)

        butt = ttk.Button(frame1, text='Готово')
        butt.pack(side='top', pady=10)
        butt['command'] = self.done

    def done(self):
        self.surname = self.surname_entry.get()
        if not self.surname.isalpha():
            mb.showwarning('Warning', warning,
                           parent=self.top)
            return

        self.name = self.name_entry.get()
        if not self.name.isalpha():
            mb.showwarning('Warning', warning,
                           parent=self.top)
            return

        self.mat = self.mat_entry.get()
        if (not self.mat.isdigit()) or\
                (int(self.mat) < 1 or int(self.mat) > 100):
            mb.showwarning('Warning', warning,
                           parent=self.top)
            return

        self.rus = self.rus_entry.get()
        if (not self.rus.isdigit()) or int(self.rus) < 1 or\
           (int(self.rus) > 100):
            mb.showwarning('Warning', warning,
                           parent=self.top)
            return

        self.dopex = self.dopex_entry.get()
        if any(char.isdigit() for char in self.dopex):
            mb.showwarning('Warning', warning,
                           parent=self.top)
            return

        self.dopmark = self.dopmark_entry.get()
        if (not self.dopmark.isdigit()) or int(self.dopmark) < 1 or\
                (int(self.dopmark) > 100):
            mb.showwarning('Warning', warning,
                           parent=self.top)
            return

        self.city = self.city_entry.get()
        if any(char.isdigit() for char in self.city):
            mb.showwarning('Warning', warning,
                           parent=self.top)
            return
        self.region = self.region_entry.get()
        if any(char.isdigit() for char in self.region):
            mb.showwarning('Warning', warning,
                           parent=self.top)
            return

        self.top.destroy()
