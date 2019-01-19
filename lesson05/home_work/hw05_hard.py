# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def cd():
    try:
        print(os.chdir(dir_name))
        print('Перешёл.')
    except FileNotFoundError as e:
        print('Не удаётся перейти', e)
    
def rm():
    check = input('Do want to delete the file? y/n {} -> '.format(dir_name))
    if check.lower() != 'y':
        return
        
    try:
        print(os.remove(dir_name))
        print('Удалил.')
    except FileNotFoundError as e:
        print('Не удаётся удалить', e)
    
    
def cp():
    with open(dir_name, 'rb') as f:
        name = dir_name.replace('.', '_copy.')
        with open(name, 'wb') as f1:
            f1.write(f.read())
    print('Файл скопирован.')

def ls():
    try:
        print(os.getcwd())
        print('Перешёл.')
    except FileNotFoundError as e:
        print('Не удаётся посмотреть', e)
        
def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cd": cd,
    "rm": rm,
    "cp": cp,
    "ls": ls,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")