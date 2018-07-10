# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import math
from fractions import Fraction

s = input('Введите выражение (например, -12 5/6 - 1/6 + -3/4): \n')
#s = '-12 5/6 - 1/6 + -3/4'

def get_first_frac(s):
    a = s.partition(' ')
    n = 0
    if a[2] != '' and a[2][0].isdigit():
        n = int(a[0])
        a = a[2].partition(' ')
    s = a[2]
    a = a[0].partition('/')
    x = int(a[0])
    y = int(a[2])

    if n != 0:
        x = int(n * y + math.copysign(x, n))
    return [[x, y], s]

res = [0, 1]
curr = [[], s]
sign = 1
while len(curr[1]) > 0:
    if curr[1].startswith('+ '):
        curr[1] = curr[1][2:]
        sign = 1
    elif curr[1].startswith('- '):
        curr[1] = curr[1][2:]
        sign = -1
    curr = get_first_frac(curr[1])
    res = [res[0] * curr[0][1] + sign * res[1] * curr[0][0], res[1] * curr[0][1]]

n = int(math.copysign(abs(res[0]) // res[1], res[0]))
num = res[0] - n * res[1]
if n and num:
    print('Ответ:', n, Fraction(abs(res[0] - n * res[1]), res[1]))
elif n:
    print('Ответ:', n)
else:
    print('Ответ:', Fraction(res[0], res[1]))
    
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

def read_file2(folder, file_name, i):
    path = os.path.join(folder, file_name)
    d = dict()
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.split(' ')
            line = list(filter(len, line))
            line[-1] = line[-1].replace('\n', '')
            if line[i].isdigit() or line[i].find('.') != -1:
                d[line[0] + ' ' + line[1]] = float(line[i])
    return d

hours_worked = read_file2('data', 'hours_of', 2)
salary = read_file2('data', 'workers', 2)
standard_hours = read_file2('data', 'workers', 4)

actual_salary = dict()
for key, value in hours_worked.items():
    if value <= standard_hours[key]:
        actual_salary[key] = round(value * salary[key] / standard_hours[key], 2)
    else:
        actual_salary[key] = round(2 * int(value - standard_hours[key]) * salary[key] / \
                                   standard_hours[key] + salary[key], 2)

path = os.path.join('data', 'payroll.txt')
with open(path, 'w', encoding='UTF-8') as f:
    f.write('Имя Фамилия Фактическая_зарплата\n')
    for key, value in actual_salary.items():
        f.write('{} {}\n'.format(key, str(value)))

print('Результаты в файле payroll.txt')
        
# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

def write_file(folder, line):
    path_out = os.path.join(folder, 'fruits_' + str(line[0]))
    with open(path_out, 'a', encoding='UTF-8') as f:
        f.write(line + '\n')

def read_file(folder, file_name):
    path = os.path.join(folder, file_name)
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            if not line.isspace(): #строка не состоит из неотображаемых символов
                line = line.capitalize()
                write_file('data', line)

read_file('data', 'fruits.txt')
