"""
Модуль со универсальными функциями и классами
Автор: Умбрас Е.Д. БИВ182
"""
import pickle as pk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from parametres import path_text
from parametres import get_file_warning


def load_data(path):
    """
    Функция для загрузки БД из pickle-файла
    Принимает:      path - путь к файлу
    Возващает:      data - первый справочник
                    reg - второй справочник
    Автор: Ушаков В. БИВ182
    """
    filename = open(path, 'rb')
    data, reg = pk.load(filename)
    filename.close()
    return data, reg


class PopupFileName():
    """
    Класс, который создает окно ввода имени файла
    Автор: Умбрас Е.Д. БИВ182
    """
    def __init__(self):
        """
        Функция инициализации, создает новое окно Toplevel
        """
        self.top = tk.Toplevel()
        self.top.geometry('+550+200')
        self.top.resizable(0, 0)
        ttk.Label(self.top, text='Введите имя файла').pack(pady=10)
        self.entry = ttk.Entry(self.top)
        self.entry.pack(padx=10, pady=10)
        btn = ttk.Button(self.top, text='Готово', command=self.done)
        btn.pack(pady=10)

    def done(self):
        """
        Функция нажатия на кнопку, получает имя файла из Entry
        Автор: Умбрас Е.Д. БИВ182
        """
        filename = self.entry.get()
        if filename.isalnum():
            self.filename = filename
            self.top.destroy()
        else:
            mb.showwarning('Warning',
                           get_file_warning)


class ShowTable():
    """
    Класс для вывода датафрейма в виде таблицы без индексов
    Автор: Умбрас Е.Д. БИВ182
    """
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
            row = dict(self.data.iloc[i])
            val = []
            for column in self.cols:
                val.append(row[column])
            self.table.insert('', 'end', values=val)

        ttk.Button(self.top, text='Сохранить', command=self.save).pack(pady=5)
        ttk.Button(self.top, text='Выйти',
                   command=self.top.destroy).pack(pady=5)

    def save(self):
        """
        Функция сохранения таблицы в .xlsx файл
        Автор: Умбрас Е.Д. БИВ182
        """
        item = PopupFileName()
        self.top.wait_window(item.top)
        path = path_text+item.filename+'.xlsx'

        self.data.to_excel(path, index=False)


class ShowTable1():
    """
    Класс для вывода датафрейма в виде таблицы с индексами
    Автор: Умбрас Е.Д. БИВ182
    """
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
            row = dict(self.data.iloc[i])
            val = [self.data.index[i]]
            for column in self.cols:
                val.append(row[column])
            self.table.insert('', 'end', values=val)

        ttk.Button(self.top, text='Сохранить', command=self.save).pack(pady=5)
        ttk.Button(self.top, text='Выйти',
                   command=self.top.destroy).pack(pady=5)

    def save(self):
        """
        Функция сохранения таблицы в .xlsx файл
        Автор: Умбрас Е.Д. БИВ182
        """
        item = PopupFileName()
        self.top.wait_window(item.top)
        path = path_text+item.filename+'.xlsx'

        self.data.to_excel(path, index=True)
