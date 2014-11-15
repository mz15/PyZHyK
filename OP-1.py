info_help = '''
Если вы хотите найти в базе данных информацию о ком-нибудь
'''     # Это будет храниться в файле!
        # P.C. ДОБАВИТЬ СЛОВ!!!
        # Это не работает, это ПыЖиК.
        # Это хелпер проги... его еще пилить и пилить
        #! ДОПИСАТЬ. И разобраться, как там изменять шрифты и все такое прочее.

info_about = '''
Программа "ПыЖиК" является справочником, в котором можно найти человека, его дату рождения, номер телефона и город.

В создании этой програмы принимали участие:
Плешков Андрей
Жукова Оксана
Кравчук Павел
'''      # Это будет храниться в файле!

database = [
    ['Борботько', 'Санкт-Петербург', '89067778734', '12.04.1996'],
    ['Воробьева', 'Санкт-Петербург', '84035793405', '28.02.1996'],
    ['Жукова', 'Таганрог', '89819532406', '25.11.1995'],
    ['Зименко', 'Санкт-Петербург', '89476389479', '18.12.1995'],
    ['Кравчук', 'Мурманск', '89086068965', '12.12.1995'],
    ['Плешков', 'Пушкин', '89078970896', '09.05.1996'],
    ['Бурков', 'Чебоксары', '84123454051', '01.02.1996'],
    ['Гончар', 'Москва', '89834565544', '15.11.1995'],
    ['Гашков', 'Пермь', '89061111911', '30.10.1996'],
    ['Неменчинский', 'Красноярск', '89086068965', '12.12.1995'],
    ['Фурсов', 'Санкт-Петербург', '89052220917', '12.03.1997']
]   #! Это должно храниться в файле!

#Pre Next 4 lines contain all the characters used in the database
lowercases = '''йцукенгшщзхъфывапролджэячсмитьбю'''
uppercases = '''ЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТБЮ'''
numerals = '''0123456789'''
sign = '''- '''

def check_name_citi(line):
    log = False
    if len(line)>0:
        if line[0] in uppercases:
            log = True
            z = 0
            i = 1
            while i<(len(line)-1):
                if ((line[i] in lowercases) or (line[i] == "'")) and (z == 0):
                    i += +1
                elif (line[i] in sign) and (z == 0):
                    i += +1
                    z = 1
                elif (line[i] in uppercases) and (z == 1):
                    i += +1
                    z = 0
                else:
                    line = ''
                    log = False
    
    return(log)

def check_phone(line):
    log = False
    if (len(line) == 11) and (line[0] == '8'):
        i = 1
        while (i<len(line)) and (line[i] in numerals):
            i += 1
        if i == len(line):
            log = True
            
    return(log)

def check_DOB(line):
    q1 = [1,3,5,7,8,10,12]
    q2 = [4,6,9,11]
    log = False
    if len(line) == 10:
        if (line[2] == '.') and (line[5] == '.'):
            if (line[0] in numerals) and (line[1] in numerals):
                if (line[3] in numerals) and (line[4] in numerals):
                    if (line[6] in numerals) and (line[7] in numerals) and (line[8] in numerals) and (line[9] in numerals):
                        q = int(line[9]) + 10*(int(line[8]) + 10*(int(line[7]) + 10*(int(line[6]))))
                        if 1900<q<2014:
                            if (int(line[4])+10*(int(line[3]))) in q1:
                                if (int(line[1])+10*(int(line[0])))<32:
                                    log = True
                                    
                            elif (int(line[4])+10*(int(line[3]))) in q2:
                                if (int(line[1])+10*(int(line[0])))<31:
                                    log = True

                            elif (int(line[4])+10*(int(line[3]))) == 2:
                                if (((int(line[1])+10*(int(line[0])))<30) and (q%4 == 0)) or (((int(line[1])+10*(int(line[0])))<29) and (q%4 != 0)):
                                    log = True

                                    
                                    if q%4 == 0:
                                        q = True
                                    else:
                                        q = False

    return(log)

def exit():
    main_window.destroy()

def help():
    window = Toplevel(main_window)
    window.title("Справка")
    lab = Label(window, text = info_help, font = "Courier 14")
    lab.pack()

def about():
    window = Toplevel(main_window)
    window.title("О программе")
    lab = Label(window, text = info_about, font = "Courier 14")
    lab.pack()    

def found(event):
    p = line_found.get()
    line_found.delete(0,END)
    v = []
    i = 0
    for i in range(0,len(database)):
        k = 0
        while k<4:
            if p in database[i][k]:
                v += [i]
                k = 4
            k += 1

    vu(database,v)
    
def DOB():

    def out(event): #переименовать
        window.destroy()
    
    def proverka(event): #переименовать

        pr1 = envs1.get()
        pr2 = envs2.get()
        pr3 = envs3.get()
        pr4 = envs4.get()
        d = []
        global database

        z = True
        
        if check_name_citi(pr1) == True:
            d += [pr1]
        else:
            envs1.delete(0,END)
            envs1.insert(END,"Не верно")
            z = False

        if (check_name_citi(pr2) == True) and z:
            d += [pr2]
        else:
            envs2.delete(0,END)
            envs2.insert(END,"Не верно")
            z = False
            
        if (check_phone(pr3) == True) and z:
            d += [pr3]
        else:
            envs3.delete(0,END)
            envs3.insert(END,"Не верно")
            z = False
                    
        if (check_DOB(pr4) == True) and z:
            d += [pr4]
        else:
            envs4.delete(0,END)
            envs4.insert(END,"Не верно")
            z = False

        if z:
            database += [d]
            window.destroy()
                        
            p = []
            for i in range(0,len(database)):
                p += [i]

            vu(database,p)

   
    window = Toplevel(main_window)
    window.title("Добавление записи")
    window.minsize(width = 365,height = 150)
    window.maxsize(width = 365,height = 150)

    fra1 = Frame(window, bg="lightblue")
    fra2 = Frame(window, bg="lightblue")
    fra3 = Frame(window, bg="lightblue")
    fra4 = Frame(window, bg="lightblue")
    fra5 = Frame(window, bg="lightblue")

    fra1.pack()
    fra2.pack()
    fra3.pack()
    fra4.pack()
    fra5.pack()
    
    lavs1 = Label(fra1, text = "Фамилия: ", font = "Courier 14")
    envs1 = Entry(fra1, width = 25, font = "Courier 14")
    lavs1.grid(row=0,column=0)
    envs1.grid(row=0,column=1)

    lavs2 = Label(fra2, text = "Город: ", font = "Courier 14")
    envs2 = Entry(fra2, width = 27, font = "Courier 14")
    lavs2.grid(row=1,column=0)
    envs2.grid(row=1,column=1)

    lavs3 = Label(fra3, text = "Номер телефона: ", font = "Courier 14")
    envs3 = Entry(fra3, width = 18, font = "Courier 14")
    lavs3.grid(row=2,column=0)
    envs3.grid(row=2,column=1)

    lavs4 = Label(fra4, text = "Дата рождения: ", font = "Courier 14")
    envs4 = Entry(fra4, width = 19, font = "Courier 14")
    lavs4.grid(row=3,column=0)
    envs4.grid(row=3,column=1)

    bu1 = Button(fra5, text = "Добавить", font = "Courier 14")
    bu2 = Button(fra5, text = " Отмена ", font = "Courier 14")
    bu1.grid(row=4,column=0)
    bu2.grid(row=4,column=1)
    
    bu1.bind("<Button-1>",proverka)
    bu2.bind("<Button-1>",out)

def vu(database,p): #переименовать

    output.delete(0,END)

    k = len(str(len(database)))
    z = (k-1)*' '+'№'
    z += 10*' '+'Фамилия'
    z += 18*' '+'Город'
    z += 7*' '+'Номер телефона'
    z += 2*' '+'Дата рождения'
    line_columns.configure(text=z)
    line_found.configure(width=k+70)
    output.configure(width=k+76)
    for i in p:
        lk = (k-len(str(i+1)))*' '+str(i+1)
        lk += (17-len(database[i][0]))*' '+database[i][0]
        lk += (23-len(database[i][1]))*' '+database[i][1]
        lk += (21-len(database[i][2]))*' '+database[i][2]
        lk += 5*' '+database[i][3]
        output.insert(END,lk)

    
    
from tkinter import *

main_window = Tk()
main_window.title("ПыЖиК")
main_menu = Menu(main_window)
main_window.config(menu=main_menu)

first_menu = Menu(main_menu)
main_menu.add_cascade(label="Файл",menu=first_menu)
first_menu.add_command(label="Выход",command=exit)
second_menu = Menu(main_menu)
main_menu.add_cascade(label="Добавить запись",command=DOB)

third_menu = Menu(main_menu)
main_menu.add_command(label="Справка",command=help)

fourth_menu = Menu(main_menu)
main_menu.add_command(label="О программе",command=about)

poiskk = Label(main_window,text="Поиск:", font="Courier 14")
line_found = Entry(main_window,width=71, font="Courier 14")
line_columns = Label(main_window,text='',font="Courier 14")
output = Listbox(main_window,selectmode=SINGLE,font="Courier 14",width=77)

p = []
for i in range(0,len(database)):
    p +=[i]

vu(database,p)

scr = Scrollbar(main_window,command=output.yview)   # Создаем полоску прокрутки УДАЛИТЬ
output.configure(yscrollcommand=scr.set)   # устанавливаем связь между полоской прокрутки и списком УДАЛИТЬ

poiskk.grid(row=0,column=0)                             # В В Э Е ВСЕ УДАЛИТЬ
line_found.grid(row=0,column=1,columnspan=2)            # Ы С Т Р
line_columns.grid(row=1,column=0,columnspan=2)          # В Е О Е
output.grid(row=2,column=0,rowspan=6,columnspan=3)      # О Й Й C
scr.grid(row=2,column=4,rowspan=6)                      # Д     И

line_found.bind("<Return>",found)

main_window.maxsize(width = 890,height = 275)
main_window.minsize(width = 890,height = 275)
main_window.mainloop()

# Хотелось бы переписать все классами
# Понять как менять шрифт
# Доделать #!
# Зделать тут табличку
# Цветоподсветка входящих элементов при поиске
# Переделать меню добавления записи
# И убрать этот цикл! Тут без него можно обойтись!
# Цветоподсветка неподходящих элементов при вводе новой записи
# При нажатии enter в окне добавления записи...
# format потом будт
# ################################
