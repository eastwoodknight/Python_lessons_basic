# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os

def cd():
    name = input('Input dir name -> ')
    try:
        print(os.chdir(name))
        print('Перешёл.')
    except FileNotFoundError as e:
        print('Не удаётся перейти', e)
    
def ls():
    name = input('Input path -> ')
    try:
        print(os.listdir(name))
        print('Перешёл.')
    except FileNotFoundError as e:
        print('Не удаётся посмотреть', e)
    
    
def rmdir():
    name = input('Input dir name -> ')
    try:
        print(os.rmdir(name))
        print('Перешёл.')
    except FileNotFoundError as e:
        print('Не удаётся посмотреть', e)
    
    
def mkdir():
    name = input('Input dir name -> ')
    try:
        print(os.mkdir(name))
        print('Перешёл.')
    except FileNotFoundError as e:
        print('Не удаётся посмотреть', e)
    
op_dict = {
           'cd': cd,
           'ls': ls,
           'rmdir': rmdir,
           'mkdir': mkdir
           }
         
if __name__ == '__main__':
    while 1:
        print("""
              HELP, COMMANDS:
              1. cd - change dir
              2. ls - show a list containing the names of the files in the directory
              3. rmdir - remove the directory
              4. mkdir - create the directory
              """)
        
        command = input('Input command -> ').strip()
        if command not in op_dict:
            print('FINISH')
            break
        
        op_dict[command]()