import os
import tkinter as tk
from tkinter import Tk
from tkinter import *
from tkinter import filedialog
import os.path
import re
import tkinter.messagebox as mb


gui_win = Tk()
gui_win.title('Переименование файлов')
gui_win.geometry('1000x1000')
gui_win.grid_rowconfigure(0, weight = 1)
gui_win.grid_columnconfigure(0, weight = 1)


def directory():
    # пользователь выбирает необходимую папку и мы сразу записываем абсолютный путь в переменную
    label_files.config(text = dirpath1())
    if dirpath_global == '':
        show_error('Вы не выбрали директорию')
    else:
        pols_name_btn.pack(pady=5)
        pols_name_btn_dir.pack(pady=5)
        filter_files_btn.pack(pady=5)
        choose_files_btn.pack(pady=5)
        reset_choose_files_btn.pack(pady=5)
        mass_rename_btn.pack(pady=5)
          

def dirpath1():
    global dirpath_global
    dirpath = filedialog.askdirectory(initialdir = r"F:\python\pythonProject", title = "Выберите директорию")
    if dirpath != '':
        dir_change_lbl.config(text="""Текущая выбранная директория: """ + '"' + dirpath + '"')
        files1 = str(filter_dir(dirpath))
        files1.replace('{', '').replace('}', '')
        dirpath_global = dirpath
        return files1


def filter_dir(a):
    # подсчет количества папок и файлов и вывод их списка
    global file_list_global
    dirpath = a
    files = os.listdir(path=dirpath)
    filecount = 0
    foldercount = 0
    filelist = []
    folderlist = []
    filelist = []
    folderlist = []
    for i in range(len(files)):
        file = files[i]
        if os.path.isfile(dirpath + '\\' + file):
            filecount += 1
            filelist.append(file)
        else:
            foldercount += 1
            folderlist.append(file)
    file_list_global = filelist
    end_list = ("Файлов: " + str(filecount) + "; " + "Папок: " + str(foldercount) + "; \n" + "Файлы: " + str(filelist) + "; \n" + "Папки: " + str(folderlist) + ";")
    return end_list


def filter_dir_dop(dirpath, filter_value, file_simv, is_mass_rename):


    def sorted_nicely(l): 
        convert = lambda text: int(text) if text.isdigit() else text 
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
        return sorted(l, key = alphanum_key)
    

    def sorted_nicely_reverse(l): 
        convert = lambda text: int(text) if text.isdigit() else text 
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
        return sorted(l, key = alphanum_key, reverse=True)


    def filter_choosing(a, b):
        end = False
        i = 0
        while not end:
            if i >= (len(a) - 1):
                if b not in a[len(a) - 1]:
                    a.pop(len(a) - 1)
                break
            if b not in a[i]:
                a.pop(i)
            elif i >= (len(a) - 1):
                break
            else:
                i += 1
        return a


    global file_list_global, filter_file_simv_global
    files = os.listdir(path=dirpath)
    filecount = 0
    foldercount = 0
    filelist = []
    folderlist = []
    filelist = []
    folderlist = []
    for i in range(len(files)):
        file = files[i]
        if os.path.isfile(dirpath + '\\' + file):
            filecount += 1
            filelist.append(file)
        else:
            foldercount += 1
            folderlist.append(file)
    file_list_global = filelist
    if filter_value == 0:
        filelist = sorted_nicely(filelist)
        folderlist = sorted_nicely(folderlist)
    elif filter_value == 1:
        filelist = sorted_nicely_reverse(filelist)
        folderlist = sorted_nicely_reverse(folderlist)
    if file_simv[0] == 1:
        filelist = filter_choosing(filelist, file_simv[1])
    if is_mass_rename == True:
        return filelist
    end_list = ("Файлов: " + str(filecount) + "; " + "Папок: " + str(foldercount) + "; \n" + "Файлы: " + str(filelist) + "; \n" + "Папки: " + str(folderlist) + ";")
    return end_list


def create_window_pols_name_file():


    def file_rename_pols():
        global old_file_1, new_file_1, dirpath_global
        old_file_1 = dirpath_global + '\\' + old_file.get()
        new_file_1 = dirpath_global + '\\' + new_file.get()
        if old_file not in file_list_global:
            show_error('Указанного файла не существует в данной директории')
            window.destroy()
        elif (new_file == '') or ('.' not in new_file):
            show_error('Неправильно указано новое имя файла')
        else:
            os.rename(abs_path(old_file_1), new_file_1)
            label_files.config(text = filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 0))
            window.destroy()
    

    window = tk.Toplevel(gui_win)
    # Добавление элементов в window
    old_file_lbl = tk.Label(window, text='Введите название файла который хотите переименовать, в формате "название файла.расширение"')
    old_file_lbl.pack(pady=5)
    old_file = tk.Entry(window)
    old_file.pack()
    new_file_lbl = tk.Label(window, text='Введите новое имя файла, в формате "название файла.расширение"')
    new_file_lbl.pack(pady=5)
    new_file = tk.Entry(window)
    new_file.pack()
    btn = tk.Button(window, text='Применить', command=file_rename_pols)
    btn.pack(pady=20)


def create_window_pols_name_dir():

    def dir_rename_pols():
        global old_file_1, new_file_1, dirpath_global
        old_file_1 = old_file.get()
        new_file_1 = new_file.get()
        os.rename(abs_path(old_file_1), new_file_1)
        label_files.config(text = filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 0))
        window.destroy()
    
    window = tk.Toplevel(gui_win)
    # Добавление элементов в window
    old_file_lbl = tk.Label(window, text='Введите название директории которую хотите переименовать')
    old_file_lbl.pack(pady=5)
    old_file = tk.Entry(window)
    old_file.pack()
    new_file_lbl = tk.Label(window, text='Введите новое имя директории')
    new_file_lbl.pack(pady=5)
    new_file = tk.Entry(window)
    new_file.pack()
    btn = tk.Button(window, text='Применить', command=dir_rename_pols)
    btn.pack(pady=20)


def create_window_filter_all():
    def change_1():
        global dirpath_global, filter_value_global, filter_file_simv_global
        filter_value_global = var.get()
        label_files.config(text=filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 0))
        window_1.destroy()
        

    window_1 = tk.Toplevel(gui_win)
    var = IntVar()
    var.set(0)
    r1 = Radiobutton(window_1, text='По возрастанию', variable=var, value=0)
    r2 = Radiobutton(window_1, text='По убыванию', variable=var, value=1)
    r1.pack()
    r2.pack()
    change = Button(window_1, text='Изменить и выйти', command=change_1)
    change.pack()


def create_window_choose_files():
    def file_simv():
        global dirpath_global, filter_file_simv_global
        a = type_file_1.get()
        filter_file_simv_global = [1, a]
        label_files.config(text=filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 0))
        window_2.destroy()


    window_2 = tk.Toplevel(gui_win)
    lbl1 = Label(window_2, text='Показывать файлы только с введённой ниже комбинацией символов:', font=('italic 10'))
    lbl1.pack()
    type_file_1 = Entry(window_2)
    type_file_1.pack()
    btn1 = Button(window_2, text='Применить', command=file_simv)
    btn1.pack()


def reset_choosing():
    global dirpath_global, filter_file_simv_global
    filter_file_simv_global = [0, '']
    label_files.config(text = filter_dir_dop(dirpath_global, 0, [0, ''], 0))


def create_window_mass_rename_files():


    def mass_rename_files():
        global dirpath_global, filter_value_global, filter_file_simv_global
        old_name = ent1.get()
        new_name = ent2.get()
        file_list = filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 1)
        for file_name in file_list:
            file_name_old = file_name
            if old_name in file_name:
                file_name = file_name.replace(old_name, new_name)
                os.rename(dirpath_global + '\\' + file_name_old, dirpath_global + '\\' + file_name)
        label_files.config(text=filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 0))
        window_3.destroy()
    

    def mass_remove_files():
        global dirpath_global, filter_value_global, filter_file_simv_global
        name = ent3.get()
        required_file_name = ent5.get()
        file_list = filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 1)
        for file_name in file_list:
            file_name_old = file_name
            if name in file_name and required_file_name in file_name:
                file_name = file_name.replace(name, '')
                os.rename(dirpath_global + '\\' + file_name_old, dirpath_global + '\\' + file_name)
        label_files.config(text=filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 0))
        window_3.destroy()


    def mass_add_files():
        global dirpath_global, filter_value_global, filter_file_simv_global
        name = ent4.get()
        required_file_name = ent6.get()
        file_list = filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 1)
        for file_name in file_list:
            file_name_old = file_name
            if required_file_name in file_name:
                file_name = name + file_name
                os.rename(dirpath_global + '\\' + file_name_old, dirpath_global + '\\' + file_name)
        label_files.config(text=filter_dir_dop(dirpath_global, filter_value_global, filter_file_simv_global, 0))
        window_3.destroy()


    window_3 = tk.Toplevel(gui_win)
    lbl1 = Label(window_3, text='Введите ту часть, которую хотите переименовать', font=('italic 10'))
    lbl1.pack()
    ent1 = Entry(window_3)
    ent1.pack()
    lbl2 = Label(window_3, text='Введите ту часть, на которую хотите заменить', font=('italic 10'))
    lbl2.pack()
    ent2 = Entry(window_3)
    ent2.pack()
    btn = Button(window_3, text='Применить', command=mass_rename_files)
    btn.pack()
    lbl6 = Label(window_3, text='Введите ту часть файлов, которую должны содержать файлы, с которыми вы проведёте операцию ниже \n Оставьте поле пустым если хотите применить ко всем файлам', font=('italic 10'))
    lbl6.pack(pady=20)
    ent5 = Entry(window_3)
    ent5.pack()
    lbl3 = Label(window_3, text='Введите ту часть, которую вы хотите удалить', font=('italic 10'))
    lbl3.pack()
    ent3 = Entry(window_3)
    ent3.pack()
    btn1 = Button(window_3, text='Применить', command=mass_remove_files)
    btn1.pack()
    lbl5 = Label(window_3, text='Введите ту часть файлов, которую должны содержать файлы, с которыми вы проведёте операцию ниже \n Оставьте поле пустым если хотите применить ко всем файлам', font=('italic 10'))
    lbl5.pack(pady=20)
    ent6 = Entry(window_3)
    ent6.pack()
    lbl4 = Label(window_3, text='Введите ту часть, которую вы хотите добавить', font=('italic 10'))
    lbl4.pack()
    ent4 = Entry(window_3)
    ent4.pack()
    btn2 = Button(window_3, text='Применить', command=mass_add_files)
    btn2.pack()


def abs_path(file_name):
    path = os.path.abspath(file_name)
    return path


def show_error(msg):
    mb.showerror("Ошибка", msg)


old_file_1 = ''
new_file_1 = ''
dirpath_global = ''
file_list_global = ''
filter_value_global = 0
filter_file_simv_global = [0, '']


dir_change_lbl = Label(gui_win, text = "Текущая директория не выбрана", font = ('italic 10'))
dir_change_lbl.pack(pady = 20)

dir_change_btn = Button(gui_win, text = 'Изменить директорию', command = directory)
dir_change_btn.pack()

label_files = Label(gui_win, text = '', font = ('italic 10'), wraplength=500)
label_files.pack(pady = 20)

pols_name_btn = Button(gui_win, text='Переименовать один файл вручную', command=create_window_pols_name_file)
pols_name_btn.pack_forget()

pols_name_btn_dir = Button(gui_win, text='Переименовать одну папку вручную', command=create_window_pols_name_dir)
pols_name_btn_dir.pack_forget()

filter_files_btn = Button(gui_win, text='Сортировка', command=create_window_filter_all)
filter_files_btn.pack_forget()

choose_files_btn = Button(gui_win, text='Выбрать нужные файлы', command=create_window_choose_files)
choose_files_btn.pack_forget()

reset_choose_files_btn = Button(gui_win, text='Сбросить фильтр нужных файлов', command=reset_choosing)
reset_choose_files_btn.pack_forget()

mass_rename_btn = Button(gui_win, text='Массовое переименование файлов', command=create_window_mass_rename_files)
mass_rename_btn.pack_forget()

gui_win.mainloop()