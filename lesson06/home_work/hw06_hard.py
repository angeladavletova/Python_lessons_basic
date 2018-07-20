# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class employee:
    def __init__(self, str):
        str = str.replace('\n', '').split()
        self.name = str[0] + ' ' + str[1]
        self.salary = float(str[2])
        self.clock_rate = float(str[4])

def read_file(folder, file_name, skip_lines, line_handler):
    path = os.path.join(folder, file_name)
    with open(path, 'r', encoding='UTF-8') as f:
        line_number = 0
        for line in f:
            if line_number >= skip_lines:
                line_handler(line)
            line_number += 1

employees_lst = []
read_file('data', 'workers', 1, lambda x: employees_lst.append(employee(x)))

hours_worked = {}
def write_to_dict(str):
    str = str.replace('\n', '').split()
    hours_worked[str[0] + ' ' + str[1]] = float(str[2])

read_file('data', 'hours_of', 1, write_to_dict)

def calculate_salary(empl, name):
    if hours_worked[name] <= empl.clock_rate:
        actual_salary.append([name, round(hours_worked[name] * empl.salary / empl.clock_rate, 2)])
    else:
        actual_salary.append([name, round(2 * (hours_worked[name] - empl.clock_rate) * empl.salary / \
                                         empl.clock_rate + empl.salary, 2)])

actual_salary = []
for name in hours_worked.keys():
    same_employee = [empl for empl in employees_lst if empl.name == name]
    count_same_employee = len(same_employee)
    if count_same_employee > 1:
        print('Ошибка. Cотрудника с именем {} не единственный'.format(name))
        continue
    if count_same_employee == 0:
        print('Ошибка. Не найден сотрудник с именем ', name)
        continue
    calculate_salary(same_employee[0], name)


def write_file(folder, file_name, header):
    path = os.path.join(folder, file_name)
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(header + '\n')
        for el in actual_salary:
            f.write('{} {}\n'.format(el[0], str(el[1]) ) )

write_file('data', 'payroll.txt', 'Имя Фамилия Фактическая_зарплата')
print('Результаты в файле payroll.txt')
