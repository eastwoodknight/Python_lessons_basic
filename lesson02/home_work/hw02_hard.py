# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
exec(equation.replace('x', ' * x'))
print(equation, '| x = ', x, '->', 'y = ', y)


print('-' * 10)
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

def check_dd(dd):
    return (len(dd) == 2) and (int(dd) >= 1) and (int(dd) <= 31)

def check_mm(mm):
    return (len(mm) == 2) and (int(mm) >= 1) and (int(mm) <= 12)

def check_yyyy(yyyy):
    return (len(yyyy) == 4) and (int(yyyy) >= 1) and (int(yyyy) <= 9999)

date = input('Input date in a format dd.mm.yyyy (like 01.10.1989)-> ')
dd, mm, yyyy = date.split('.')
print('check dd:', check_dd(dd))
print('check mm:', check_mm(mm))
print('check yyyy:', check_yyyy(yyyy))

print('-' * 10) 
# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

n = int(input('Input room number -> '))
i = 1
while n > 0:
    n -= i ** 2
    i += 1
i = i - 1 # because we always skip one extra floor

print('n, i:', n, i)
room = range(i - 1, -1, -1)[(-n) % i] if n != 0 else i - 1
floor = i * (i + 1) // 2 - (-n) // i

print('Floor, room(*): ', floor, room)
print(':-) In da tower of Python we count from 0 on each floor.') 
print('But for ya it may seems like this: ')
print('Floor, room:', floor, room + 1)

solution = '''
SOLUTION:
Let's take a look onto some sequences:
----------------------
ROOMS:
            6   9   12
    2   4   
1           7   10  13 
    3   5   
            8   11  14
----------------------
BLOCKS(let's call 'em i)
1   2       3           
----------------------
FLOOR
1   2   3   4   5   6   
MAX FLOOR on each BLOCK
1       3           6       -> MAX FLOOR = i * (i + 1) // 2
                              Coincidence? Not think so!
                              So why not try ...
----------------------
MAX ROOM on each BLOCK
1       5           14      -> looks pretty like
                               MAX_ROOM(i) = MAX_ROOM(i-1) + i ** 2
                            -> for now what if we try
                               this ROOMS - MAX ROOM on each BLOCK:
----------------------
ROOMS - MAX ROOM on each floor
(let's call it n)
            -8  -5  -2
    -3  -1    
0           -7  -4  -1
    -2  0   
            -6  -3  0       -> actually it looks like 
                               we can get room number
                               using %, // and i
----------------------
i:
1   2       3
---------------------
room number:
            0   0   0
    0   0
0           1   1   1
    1   1
            2   2   2       -> if n!= 0: 
                                   range(i - 1, -1, -1)[(-n) % i]       
                               else:
                                   i - 1
                               Coincedence? :-)

                            -> now we can have our current floor
----------------------
ROOMS - MAX ROOM on each floor
(let's call it n)
            -8  -5  -2
    -3  -1
0           -7  -4  -1
    -2  0
            -6  -3  0       
----------------------
i:
1   2       3
---------------------
floor:
            4   5   6
    2   3
1           4   5   6       
    2   3                      !note MAX_FLOOR = i * (i + 1) //2  
            4   5   6       -> floor = MAX_FLOOR - (-n) // i

Programming sometimes is lika a poetry.
Hope you enjoy it! :-)
Happy New Year!
'''
