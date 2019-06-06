import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from parametres import get_file_warning


class PopupFileName():
    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry('+550+200')
        self.top.resizable(0, 0)
        ttk.Label(self.top, text='Введите имя файла').pack(pady=10)
        self.entry = ttk.Entry(self.top)
        self.entry.pack(padx=10, pady=10)
        btn = ttk.Button(self.top, text='Готово', command=self.done)
        btn.pack(pady=10)

    def done(self):
        filename = self.entry.get()
        if filename.isalnum():
            self.filename = filename
            self.top.destroy()
        else:
            mb.showwarning('Warning',
                           get_file_warning)
