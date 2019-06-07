import pickle as pk
import tkinter as tk
from tkinter import ttk
from parametres import path_text
from tkinter import messagebox as mb
from parametres import get_file_warning


def load_data(path):
    filename = open(path, 'rb')
    data, reg = pk.load(filename)
    filename.close()
    return data, reg


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


class ShowTable():
    def __init__(self, data):
        self.top = tk.Toplevel()
        self.top.geometry('+550+200')
        self.top.resizable(0, 0)
        self.data = data
        self.cols = tuple(self.data.columns)

        self.table = ttk.Treeview(self.top, show="headings",
                                  selectmode="browse")
        self.table["columns"] = self.cols

        for col in self.cols:
            self.table.column(col, width=115)
            self.table.heading(col, text=col)

        scrolltable = tk.Scrollbar(self.top, command=self.table.yview)
        self.table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(fill=tk.BOTH)

        for i in range(len(self.data)):
            d = dict(self.data.iloc[i])
            t = []
            for column in self.cols:
                t.append(d[column])
            self.table.insert('', 'end', values=t)

        ttk.Button(self.top, text='Сохранить', command=self.save).pack(pady=5)
        ttk.Button(self.top, text='Выйти',
                   command=self.top.destroy).pack(pady=5)

    def save(self):
        item = PopupFileName()
        self.top.wait_window(item.top)
        path = path_text+item.filename+'.xlsx'

        self.data.to_excel(path, index=True)


class ShowTable1():
    def __init__(self, data):
        self.top = tk.Toplevel()
        self.top.geometry('+250+200')
        self.top.resizable(0, 0)
        self.data = data
        self.cols = tuple(self.data.columns)

        self.table = ttk.Treeview(self.top, show="headings",
                                  selectmode="browse")
        self.table["columns"] = ('index',)+self.cols

        self.table.column('index', width=95)
        self.table.heading('index', text='')
        for col in self.cols:
            self.table.column(col, width=115)
            self.table.heading(col, text=col)

        scrolltable = tk.Scrollbar(self.top, command=self.table.yview)
        self.table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(fill=tk.BOTH)

        for i in range(len(self.data)):
            d = dict(self.data.iloc[i])
            t = [self.data.index[i]]
            for column in self.cols:
                t.append(d[column])
            self.table.insert('', 'end', values=t)

        ttk.Button(self.top, text='Сохранить', command=self.save).pack(pady=5)
        ttk.Button(self.top, text='Выйти',
                   command=self.top.destroy).pack(pady=5)

    def save(self):
        item = PopupFileName()
        self.top.wait_window(item.top)
        path = path_text+item.filename+'.xlsx'

        self.data.to_excel(path, index=True)
