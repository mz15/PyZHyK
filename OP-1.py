#! Все для Линуксоидов)))

shelp='''
HELP ME!!!

В создании этой програмы принимали участие:
Плешков Андрей
Жукова Оксана
Кравчук Павел

Это не работает, это ПыЖиК.

P.C. ДОБАВИТЬ СЛОВ!!!
      ''' # Это хелпер проги...
          #! ДОПИСАТЬ. И разобраться, как там изменять шрифты и все такое прочее.

s = [['Борботько','Санкт-Петербург','89067778734','12.04.1996'],
     ['Воробьева','Санкт-Петербург','84035793405','28.02.1996'],
     ['Жукова','Таганрог','89819532406','25.11.1995'],
     ['Зименко','Санкт-Петербург','89476389479','18.12.1995'],
     ['Кравчук','Мурманск','89086068965','12.12.1995'],
     ['Плешков','Пушкин','89078970896','09.05.1996'],
     ['Бурков','Чебоксары','84123454051','01.02.1996'],
     ['Гончар','Москва','89834565544','15.11.1995'],
     ['Гашков','Пермь','89061111911','30.10.1996'],
     ['Неменчинский','Красноярск','89086068965','12.12.1995'],
     ['Фурсов','Санкт-Петербург','89052220917','12.03.1997']]

# Список...
#! Это должно храниться в файле!

alfm = '''йцукенгшщзхъфывапролджэячсмитьбю'''   # Алфавит строчных символов
alfb = '''ЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТБЮ'''     # Алфавит заглавных символов
alfz = '''- '''                                 # Алфавит специальных знаков

alf0 = '''0123456789''' # Алфавит цифр

def prfg(line):     # Функция проверки фамилии и города
    log = False
    if len(line)>0:
        if line[0] in alfb:
            log = True
            z = 0
            i = 1
            while i<(len(line)-1):
                if ((line[i] in alfm) or (line[i] == "'")) and (z == 0):
                    i += +1
                elif (line[i] in alfz) and (z == 0):
                    i += +1
                    z = 1
                elif (line[i] in alfb) and (z == 1):
                    i += +1
                    z = 0
                else:
                    line = ''
                    log = False
    
    return(log)

def prte(line):     # Функция проверки номера телефона !ПЕРЕДЕЛАТЬ!
    log = False
    if len(line) == 11:
        i = 0
        while (i<len(line)) and (line[i] in alf0):
            i += 1
        if i == len(line):
            log = True
            
    return(log)

def prda(line):     # Функция проверки даты рождения
    q1 = [1,3,5,7,8,10,12]
    q2 = [4,6,9,11]
    log = False
    if len(line) == 10:
        if (line[2] == '.') and (line[5] == '.'):
            if (line[0] in alf0) and (line[1] in alf0):
                if (line[3] in alf0) and (line[4] in alf0):
                    if (line[6] in alf0) and (line[7] in alf0) and (line[8] in alf0) and (line[9] in alf0):
                        q = int(line[9])+10*(int(line[8])+10*(int(line[7])+10*(int(line[6]))))
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

def Exit():      # А эта замячательная вещь закрывает прогу.
    ok.destroy() # Разрушаем главное окно, после него прога сама закроется

# Переделать функцию выхода: типа, а не хотите ли вы это сохранить?

def Help():                                              # Это та функция, что вызывает хелер
    vsok = Toplevel(ok)                                  # Создается зависимое окно
    vsok.title("Help")                                   # Называю его почеловечески...
    lab = Label(vsok, text = shelp, font = "Courier 14") # Куда, что, каким шрифтом. Именно так.
    lab.pack()                                           # Пакуем, а то не появится.

def chet():
    li=123

def poisk(event):
    p = ent.get()
    ent.delete(0,END)
    v = []
    i = 0
    for i in range(0,len(s)):
        k = 0
        while k<4:
            if p in s[i][k]:
                v += [i]
                k = 4
            k += 1

    vu(s,v)


def dob():

    def out(event):
        vsok.destroy()
    
    def proverka(event):

        pr1 = envs1.get()
        pr2 = envs2.get()
        pr3 = envs3.get()
        pr4 = envs4.get()
        d = []
        global s

        z = True
        
        if prfg(pr1) == True:
            d += [pr1]
        else:
            envs1.delete(0,END)
            envs1.insert(END,"Не верно")
            z = False

        if (prfg(pr2) == True) and z:
            d += [pr2]
        else:
            envs2.delete(0,END)
            envs2.insert(END,"Не верно")
            z = False
            
        if (prte(pr3) == True) and z:
            d += [pr3]
        else:
            envs3.delete(0,END)
            envs3.insert(END,"Не верно")
            z = False
                    
        if (prda(pr4) == True) and z:
            d += [pr4]
        else:
            envs4.delete(0,END)
            envs4.insert(END,"Не верно")
            z = False

        if z:
            s += [d]
            vsok.destroy()
                        
            p = []
            for i in range(0,len(s)):
                p += [i]

            vu(s,p)

   
    vsok = Toplevel(ok)
    vsok.title("Добавление записи")
    vsok.minsize(width = 365,height = 150)
    vsok.maxsize(width = 365,height = 150)

    fra1 = Frame(vsok, bg="lightblue")
    fra2 = Frame(vsok, bg="lightblue")
    fra3 = Frame(vsok, bg="lightblue")
    fra4 = Frame(vsok, bg="lightblue")
    fra5 = Frame(vsok, bg="lightblue")

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

def uzm():
    c=123

def cle():
    c=123

def vu(s,p):

    lis.delete(0,END)

    k = len(str(len(s)))
    z = (k-1)*' '+'№'
    z += 10*' '+'Фамилия'
    z += 18*' '+'Город'
    z += 7*' '+'Номер телефона'
    z += 2*' '+'Дата рождения'
    la2.configure(text=z)
    ent.configure(width=k+70)
    lis.configure(width=k+76)
    for i in p:
        lk = (k-len(str(i+1)))*' '+str(i+1)
        lk += (17-len(s[i][0]))*' '+s[i][0]
        lk += (23-len(s[i][1]))*' '+s[i][1]
        lk += (21-len(s[i][2]))*' '+s[i][2]
        lk += 5*' '+s[i][3]
        lis.insert(END,lk)

    
    
from tkinter import *   # Подключаем модуль GUI

ok = Tk()   # Задаем главное окно
 
m = Menu(ok)        # Делаем в нем менюшку верхнюю
ok.title("ПыЖиК")   # Наименование главного окна
ok.config(menu=m)   # Связываем меню и окно

fm = Menu(m)        # Создается пункт меню с размещением на основном меню m
m.add_cascade(label="File",menu=fm)             # Щелк и выпало менюшка...
#!fm.add_command(label="Open...",command=Open)   Потом или никогда
#!fm.add_command(label="New",command = New)      Потом или никогда
#!fm.add_command(label="Save...",command = Save) Потом или никогда
fm.add_command(label="Exit",command=Exit)       # Щелк, и все закрылось!

om = Menu(m) # Создается пункт меню с размещением на основном меню m
m.add_cascade(label="Add enrry",command=dob) # Это добавление записи
hm = Menu(m) # Создается пункт меню с размещением на основном меню m
m.add_command(label="Help",command=Help) # Это хелпер

la1 = Label(ok,text="Поиск:", font="Courier 14")                    # Выводит "Поиск: "
ent = Entry(ok,width=71, font="Courier 14")                         # Сама строка поиска.
la2 = Label(ok,text='',font="Courier 14")                           # Строка на наименований столбцов.
lis = Listbox(ok,selectmode=SINGLE,font="Courier 14",width=77)      # Вывод самых записей

p = []
for i in range(0,len(s)):
    p +=[i]

vu(s,p)

scr = Scrollbar(ok,command=lis.yview)   # Создаем полоску прокрутки
lis.configure(yscrollcommand=scr.set)   # Сустанавливаем связь между полоской прокрутки и списком

la1.grid(row=0,column=0)                            # В В Э Е
ent.grid(row=0,column=1,columnspan=2)               # Ы С Т Р
la2.grid(row=1,column=0,columnspan=2)               # В Е О Е
lis.grid(row=2,column=0,rowspan=6,columnspan=3)     # О Й Й C
scr.grid(row=2,column=4,rowspan=6)                  # Д     И

ent.bind("<Return>",poisk)

#ok.maxsize(width = 880,height = 250)
ok.minsize(width = 880,height = 250)
ok.mainloop()   # Что-то, что все-таки создает наше окно

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
