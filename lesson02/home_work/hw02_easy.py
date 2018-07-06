# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

def numiration_list (list):
    max_len = 0
    len_list = len(list)
    
    for i in range(len_list):
       max_len = max(max_len, len(list[i]) + len(str(i + 1)))

    for i in range(len_list):
        setting = '{} {:>' + str (max_len - len(str(i + 1))) + '}'
        print(setting.format(i + 1, list[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

def delete_element(list1, list2):
    k = 0
    i = 0
    list2 = set(list2)
    len_list1 = len(list1)
    while i < len_list1:
        if list1[i] in list2:
            k += 1
        else:
            list1[i - k] = list1[i]
        i += 1
    del list1[len_list1 - k :]

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

def transform_list(a):
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i / 4)
        else:
            b.append(i * 2)
    return b
