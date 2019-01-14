# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    i, j = 1, 1
    arr = []
    while 1:
        i, j = i + j, i
        if i > n:
            arr.append(i)
        if i >= m:
            break
    return arr

print(fibonacci(1, 4), fibonacci(3, 7))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(arr):
    if len(arr) <= 1:
        return arr
    else:
        return sort_to_max([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               sort_to_max([x for x in arr[1:] if x >= arr[0]])
        
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(f, arr):
    return [i for i in arr if f(i)]

a = [False, 0, -1 , True, 1, 0]
print(list(filter(bool, a)), my_filter(bool, a))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
A1, A2, A3, A4 = sorted(A1, A2, A3, A4, key=lambda x: x[1])

if (A3[1] == A4[1] and A1[1] == A2[1] and \
    abs(A3[0] - A4[0]) == abs(A1[0] - A2[0])):
    print('Параллелограмм!')
else:
    print('Не параллелограмм!')


