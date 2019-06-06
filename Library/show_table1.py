import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename


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
        self.filename = asksaveasfilename(defaultextension=".xlsx",
                                          filetypes=(("xlsx file", "*.xlsx"),
                                                     ("All Files", "*.*")))
        self.data.to_excel(self.filename, index=False)
