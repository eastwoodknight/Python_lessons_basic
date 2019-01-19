# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

# create folders 
for i in range(9):
    try:
        os.mkdir('dir_' + str(i + 1))
    except FileExistsError:
        pass
    
# remove folders
for i in range(9):
    try:
        os.rmdir('dir_' + str(i + 1))
    except FileNotFoundError:
        pass
    
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print(list(i for i in os.listdir() if os.path.isdir(i)))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
filename = sys.argv[0]
with open(filename, 'rb') as f:
    filename = os.path.basename(filename)
    name = filename.split('.py')[0] + '_copy'
    with open(name + '.py', 'wb') as f1:
        f1.write(f.read())