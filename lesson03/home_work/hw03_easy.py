# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    n, digits = str(number).split('.')
    digits = list(digits[:ndigits + 1])

    l = len(digits)
    if l > 1:
        if int(digits[-1]) > 5:
            digits = str(int(''.join(digits[:-1])) + 1)
            digits = list(digits)

        if len(digits) == l:
            n = str(int(n) + 1)
            digits = '0' * ndigits 
    else:
        if int(digits[-1]) > 5:
            n = str(int(n) + 1)
            
    return n + '.' + ''.join(digits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    digits = [int(i) for i in str(ticket_number)]
    n = len(digits) // 2
    return sum(digits[:n]) == sum(digits[n:])

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
