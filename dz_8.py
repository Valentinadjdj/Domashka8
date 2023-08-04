#Урок 8. Работа с файлами
#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
#для изменения и удаления данных

import os

filename = "tell.txt"

def load_data():
    if os.path.isfile(filename):
        with open(filename, encoding="utf-8") as f:
            r = f.readlines()
            s = []
            for line in r:
                s.append(line.split())
                
        return s
    s = []
    
    return s

def input_data(s):
    first_name = input("Введите фамилиию: ")
    last_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    tel = input("Введите номер телефона: ")
    with open(filename, "a",encoding="UTF-8")as f:
        f.write(f"{first_name}{last_name}{patronymic}{tel}\n")
    s.append([first_name, last_name, patronymic, tel])
    return s

def search_data(s, object):
    for line in s:
        if object in line or object.capitalize() in line:
            return " ".join(line)
        return "Таких данных нет!"

def show_data(s):
    for line in s:
        print(" ".join(line))
        
def modify_data(r, object):
    remove_data(r, object)
    input_data(r)
    return

def remove_data(r, object):
    if object in r:
        r.pop(r.index(object))
    with open(filename, "w", encoding="UTF-8") as f:
        for line in r:
            f.write(f"{' '.join(line)}\n")


if __name__ == "__main__":
    s = load_data()
    while True:
        action = input("1 - Добавить данные\n 2 - Поиск данных\n 3 - Просмотр данных\n 4 - Выход\n")
        if action == "1":
            s = input_data(s)
        elif action =="2":
            search_name = input("Данные для поиска: ")
            result = search_data(s,search_name)
            print(" ".join(result))
            if result != "Таких данных нет!":
                newdata = input("1 - Изменить данные \n 2 - Удалить данный \n 3 - Вернуться в начало \n")
                if newdata =="1":
                    modify_data(s,result)
                    s = load_data()
                elif  newdata =="2":
                    remove_data(s,result)
                    s= load_data()
                elif newdata =="3":
                    continue
                elif newdata =="4":
                    print("ПОКА!")
                else:
                    print("Некорректные данные!")
                    continue
        elif action =="3":
            show_data(s)
            #result = search_data(s,search_name)
            #print(" ".join(result))
        elif action =="4":
            print("Выход!")
            break
        else:
            exit
                