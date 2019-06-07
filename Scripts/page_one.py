import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
from tkinter.filedialog import asksaveasfilename
import pickle as pk
import pandas as pd
import matplotlib.pyplot as plt
from popup_text import PopupWindowGet1_1
from library import ShowTable
from library import ShowTable1
from popup_text2 import PopupWindowGet1_2
from popup_add import PopupWindowAdd
from popup_change import PopupWindowChange
from popup_func import PopupWindowFuncChoose
from parametres import path_graph, change_warning, save_warning, delete_warning


fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size


class PageOne(tk.Frame):
    def __init__(self, parent, controller, data=None):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.data = data
        self.save_flag = False

        self.frm1 = ttk.Frame(self, width=695)
        self.frm1.pack(side='left', fill='y')

        self.frm2 = ttk.Frame(self, width=240)
        self.frm2.pack(side='right', fill='both')

        self.add_button = ttk.Button(self, text='Добавить сущность')
        self.add_button.place(x=765, y=20, width=200, height=30)
        self.add_button['command'] = self.add_item

        self.change_button = ttk.Button(self,
                                        text='Изменить выбранную сущность')
        self.change_button.place(x=765, y=60, width=200, height=30)
        self.change_button['command'] = self.change_item

        self.delete_button = ttk.Button(self,
                                        text='Удалить выбранную сущность')
        self.delete_button.place(x=765, y=100, width=200, height=30)
        self.delete_button['command'] = self.delete_item

        ttk.Label(self, text='Выбор текстового отчета').place(x=795, y=170)

        self.combobox1 = ttk.Combobox(self, values=['Простой текстовый отчет',
                                                    'Статистический отчет',
                                                    'Сводная таблица'],
                                      state='readonly', width=30)
        self.combobox1.place(x=765, y=190)

        self.combo_button1 = ttk.Button(self, text='Составить')
        self.combo_button1.place(x=825, y=220)
        self.combo_button1['command'] = self.get1

        ttk.Label(self, text='Выбор графического отчета').place(x=790, y=280)

        self.combobox2 = ttk.Combobox(self, values=['Столбчатая диаграмма',
                                                    'Гистограмма',
                                                    'Диаграмма Бокса-Вискера',
                                                    'Диаграмма рассеивания'],
                                      state='readonly', width=30)
        self.combobox2.place(x=765, y=300)

        self.combo_button2 = ttk.Button(self, text='Составить')
        self.combo_button2.place(x=825, y=330)
        self.combo_button2['command'] = self.get2

        self.combo_button3 = ttk.Button(self, text='Сохранить')
        self.combo_button3.place(x=825, y=360)
        self.combo_button3['command'] = self.save_graph

        self.save_button = ttk.Button(self, text='Сохранить')
        self.save_button.place(x=765, y=450, width=200, height=30)
        self.save_button['command'] = self.save_data

        self.back_button = ttk.Button(self, text='Назад')
        self.back_button.place(x=765, y=410, width=200, height=30)
        self.back_button['command'] = lambda: controller.show_frame('StartPage')

        self.table = ttk.Treeview(self.frm1, show="headings",
                                  selectmode="browse", height=25)
        self.table["columns"] = ('surname', 'name', 'mat_mark', 'rus_mark',
                                 'dop_exam', 'dop_mark', 'city', 'region')

        self.table.column("surname", width=95)
        self.table.column("name", width=90)
        self.table.column("mat_mark", width=80, anchor=tk.CENTER)
        self.table.column("rus_mark", width=60, anchor=tk.CENTER)
        self.table.column("dop_exam", width=105)
        self.table.column("dop_mark", width=80, anchor=tk.CENTER)
        self.table.column("city", width=115)
        self.table.column("region", width=115)

        self.table.heading("surname", text='Фамилия')
        self.table.heading("name", text='Имя')
        self.table.heading("mat_mark", text='Математика')
        self.table.heading("rus_mark", text='Русский')
        self.table.heading("dop_exam", text='Доп. предмет')
        self.table.heading("dop_mark", text='Доп. баллы')
        self.table.heading("city", text='Город')
        self.table.heading("region", text='Округ')

        scrolltable = tk.Scrollbar(self.frm1, command=self.table.yview)
        self.table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(fill=tk.BOTH)

    def save_graph(self):
        self.save_flag = True
        combo_value = self.combobox2.get()
        if combo_value == '':
            mb.showwarning('Warning', 'Выберите вид отчета')
        elif combo_value == 'Столбчатая диаграмма':
            self.graph1()
            plt.close()
        elif combo_value == 'Гистограмма':
            self.graph2()
            plt.close()
        elif combo_value == 'Диаграмма Бокса-Вискера':
            self.graph3()
            plt.close()
        elif combo_value == 'Диаграмма рассеивания':
            self.graph4()
            plt.close()

    def get1(self):
        combo_value = self.combobox1.get()
        if combo_value == '':
            mb.showwarning('Warning', 'Выберите вид отчета')
        elif combo_value == 'Простой текстовый отчет':
            item = PopupWindowGet1_1()
            self.master.wait_window(item.top)
            sel_code = 0
            if item.mat_max != -1:
                sel = (self.data['Математика'] >= item.mat_min) &\
                      (self.data['Математика'] <= item.mat_max)
                sel_code = 1
            if item.rus_max != -1:
                sel = sel & (self.data['Русский язык'] >= item.rus_min) &\
                      (self.data['Русский язык'] <= item.rus_max)
                sel_code = 1
            if item.dop_max != -1:
                sel = sel & (self.data['Доп. баллы'] >= item.dop_min) &\
                      (self.data['Доп. баллы'] <= item.dop_max)
                sel_code = 1
            if sel_code:
                df = self.data.loc[sel, item.cols]
                ShowTable(df)

        elif combo_value == 'Статистический отчет':
            item = PopupWindowGet1_2()
            self.master.wait_window(item.top)
            if item.atr:
                ShowTable1(pd.DataFrame(self.data[item.atr].describe()))
            else:
                ShowTable1(self.data.describe())

        elif combo_value == 'Сводная таблица':
            item = PopupWindowFuncChoose()
            self.master.wait_window(item.top)
            if item.atr == 0:
                func = 'mean'
            else:
                func = 'std'
            ShowTable1(pd.pivot_table(self.data, index='Город',
                                      columns='Доп. предмет',
                                      values='Доп. баллы',
                                      aggfunc=func))

    def get2(self):
        combo_value = self.combobox2.get()
        if combo_value == '':
            mb.showwarning('Warning', 'Выберите вид отчета')
        elif combo_value == 'Столбчатая диаграмма':
            self.graph1()
        elif combo_value == 'Гистограмма':
            self.graph2()
        elif combo_value == 'Диаграмма Бокса-Вискера':
            self.graph3()
        elif combo_value == 'Диаграмма рассеивания':
            self.graph4()

    def graph1(self):
        fig = plt.figure()
        axes = fig.add_axes([0.1, 0.3, .6, .6])
        plt.title('Столбчатая диаграмма')
        cat = self.data["Округ"].unique()
        grep = pd.DataFrame([])
        for c in cat:
            cross = pd.crosstab(self.data.loc[self.data['Округ'] == c,
                                              'Доп. предмет'], c)
            grep = pd.merge(grep, cross, how='outer', left_index=True,
                            right_index=True)
        grep.T.plot(kind='bar', ax=axes)
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        if self.save_flag:
            plt.savefig(path_graph+'BarPlot.png')
            self.save_flag = False
        else:
            plt.show()

    def graph2(self):
        self.data.hist('Доп. баллы', by='Доп. предмет', bins=10)
        plt.tight_layout()
        if self.save_flag:
            plt.savefig(path_graph+'Histogram.png')
            self.save_flag = False
        else:
            plt.show()

    def graph3(self):
        self.data.boxplot('Доп. баллы', by='Доп. предмет')
        plt.title('')
        plt.tight_layout()
        if self.save_flag:
            plt.savefig(path_graph+'BoxPlot.png')
            self.save_flag = False
        else:
            plt.show()

    def graph4(self):
        xmin, xmax = 0, 100
        ymin, ymax = 0, 100
        fig, ax_lst = plt.subplots(2, 3)
        fig.subplots_adjust(.1, .1, .8, .8, wspace=1, hspace=.5)
        fig.suptitle('Анализ связи баллов по матемтике и'
                     ' по русскому языку по городам')
        i = 0
        for val in list(self.data['Округ'].unique()):
            print(val)
            x = self.data.loc[self.data['Округ'] == val, 'Русский язык']
            y = self.data.loc[self.data['Округ'] == val, 'Математика']
            ax_lst[i//3][i % 3].set_xlim(left=xmin, right=xmax)
            ax_lst[i//3][i % 3].set_ylim(bottom=ymin, top=ymax)
            ax_lst[i//3][i % 3].scatter(x, y)
            ax_lst[i//3][i % 3].set_title(val)
            ax_lst[i//3][i % 3].set_xlabel("Русский язык")
            ax_lst[i//3][i % 3].set_ylabel("Математика")
            i += 1

        if self.save_flag:
            plt.savefig(path_graph+'ScatterPlot.png')
            self.save_flag = False
        else:
            plt.show()

    def delete_item(self):
        iid = self.table.focus()
        print(iid)
        if iid:
            pos = self.table.index(iid)
            self.table.delete(iid)
            self.data = self.data.drop([pos])
            self.data.index = range(len(self.data))
            print(self.data)
        else:
            mb.showwarning("Warning",
                           delete_warning)

    def add_item(self):
        item = PopupWindowAdd()
        print(self.data)
        self.master.wait_window(item.top)
        self.table.insert('', 'end', values=(item.surname, item.name,
                                             int(item.mat), int(item.rus),
                                             item.dopex,
                                             int(item.dopmark), item.city,
                                             item.region))
        self.data = self.data.append({'Фамилия': item.surname,
                                      'Имя': item.name,
                                      'Математика': int(item.mat),
                                      'Русский язык': int(item.rus),
                                      'Доп. предмет': item.dopex,
                                      'Доп. баллы': int(item.dopmark),
                                      'Город': item.city,
                                      'Округ': item.region},
                                     ignore_index=True)
        print(self.data)

    def change_item(self):
        iid = self.table.focus()

        if iid:
            val = self.table.item(iid)
            item = PopupWindowChange(val['values'])
            self.master.wait_window(item.top)
            pos = self.table.index(iid)
            print(pos)

            self.data.loc[pos, 'Фамилия'] = item.surname
            self.data.loc[pos, 'Имя'] = item.name
            self.data.loc[pos, 'Математика'] = int(item.mat)
            self.data.loc[pos, 'Русский язык'] = int(item.rus)
            self.data.loc[pos, 'Доп. предмет'] = item.dopex
            self.data.loc[pos, 'Доп. баллы'] = int(item.dopmark)
            self.data.loc[pos, 'Город'] = item.city
            self.data.loc[pos, 'Округ'] = item.region

            print(self.data.iloc[pos])

            self.table.insert('', pos, values=(item.surname, item.name,
                                               int(item.mat), int(item.rus),
                                               item.dopex, int(item.dopmark),
                                               item.city, item.region))
            self.table.delete(iid)
        else:
            mb.showwarning("Warning",
                           change_warning)

    def save_data(self):
        if self.table.get_children():
            file_name = asksaveasfilename()
            file_name = str(file_name)
            file = open(file_name, 'wb')
            pk.dump(self.data, file)
            file.close()
        else:
            mb.showwarning('Warning', save_warning)
