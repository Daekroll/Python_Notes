import csv
from datetime import date

def openNotes():
    with open("Notes.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            notes.append(row)  
def printNotes(array):
    for i in array:
       printNote(i)

def printNote(listok):
    print(f"id: {listok[0]}\n"
             +f"Заголовок: {listok[1]}\n"
             +f"Текст: {listok[2]}\n"
             +f"Дата создания: {listok[3]}\n")
    
def addNotes():
    identificator = int(notes[-1][0])+1
    data = date.today()
    data = data.strftime("%d.%m.%Y")
    a = input("Введите заголовок: ")
    b = input("Введите текст заметки: ")
    temp = [identificator, a, b, data]
    notes.append(temp)

def closeNotes():
    with open("Notes.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        file_writer.writerows(notes)

def changeNote(listok):
    data = date.today()
    data = data.strftime("%d.%m.%Y")
    change = input("Хотите изменить заголовок?\n"
          +"1.Да\n"
          +"2. Нет\n")
    if change=="1":
        a = input("Введите новый заголовок: ")
    else:
        a = listok[1]
    change = input("Хотите изменить текст заметки?\n"
          +"1.Да\n"
          +"2. Нет\n")
    if change=="1":
        b = input("Введите новый текст заметки: ")
    else:
        b = listok[2]
    temp = [listok[0], a, b, data]
    for i in range(len(notes)):
        if notes[i][0]==temp[0]:
            notes[i] = temp

def deleteNote(listok):
    for i in notes:
        if listok==i:
            notes.remove(i)

def findNoteByDate():
    print("Формат вводимых данных дд.мм.гггг!")
    date1=input("Введите дату: ")
    temp = list()
    for i in notes:
        if i[3] == date1:
            temp.append(i)
    if len(temp) > 1:
        printNotes(temp)
        idNotes = input("Введите id нужной заметки: ")
        for i in temp:
            if i[0] == idNotes:
                temp1=i
                printNote(temp1)
    elif len(temp) == 0:
        print("Заметка не найдена!")
        exit
    else:
        temp1 = temp[0]
        printNote(temp1)
    a = input("Действия: \n"
            +"1.Редактировать\n"
            +"2.Удалить\n"
            +"3.Вернуться\n")
    if a=="1":
        changeNote(temp1)
    if a=="2":
        deleteNote(temp1)


msg = "1. Показать заметки\n"+"2. Добавить заметку\n"+"3. Найти заметку\n"+"4. Закончить работу\n"
notes = list()
def NoteBook():
    openNotes()
    while(True):
    
        print(msg)
        a = int(input("Введите номер действия: \n"))
        if a>4 or a<1:
            print("Введены некорректные данные!\n"
                +"Попробуйте снова\n")
        if a==1:
            printNotes(notes)
        if a==2:
            addNotes()
        if a==3:
            findNoteByDate()
        if a==4:
            closeNotes()
            print("Bye bye!")
            break



