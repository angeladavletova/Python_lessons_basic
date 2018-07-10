# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = str(number)
    dot_index = number.find('.')
    rounded_number = float(number[:dot_index + ndigits + 1])
    if int(number[dot_index + ndigits + 1]) >= 5:
        return rounded_number + 1/(10 ** ndigits)
    else:
        return rounded_number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    len_ticket_number = len(str(ticket_number))
    if len_ticket_number != 6:
        return 'Некорректный не номер билета!'
    str_ticket_number = str(ticket_number)

    left_number = 0
    right_number = 0
    for i in range(3):
        left_number += int(str_ticket_number[i])
        right_number += int(str_ticket_number[i + 3])

    if left_number == right_number:
        return 'Счастливый билет!'
    else:
        return 'Несчастливый билет'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

