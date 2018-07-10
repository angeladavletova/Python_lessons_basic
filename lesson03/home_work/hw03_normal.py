# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = 1
    b = 1

    for i in range(3, m + 1):
        b += a
        a, b = b, a
        if i >= n:
            print(a)

fibonacci(6, 10)

# 1 1 2 3 5 8 13 21 34 55
# 1 2 3 4 5 6 7  8  9  10

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for i in range(len(origin_list) - 1, 0, -1):
        for j in range(i):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]

lst =  [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(lst)
print(lst)
-------------------------------------------
def sort_to_max(origin_list):
    pass

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_func(condition, iter):
    filter_iter = []
    for i in iter:
        if condition(i):
            filter_iter.append(i)
    return filter_iter
lst = [2, 10, -10, 8, 2, 0, 14]
print('List', lst)
print('My filter function:', filter_func(lambda x: x > 5, lst))
#print('Filter', list(filter(lambda x: x > 5, lst)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def are_parallel(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2 == 0 #условие параллельности векторов (x1, y1) и (x2, y2)

def is_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4):
    return (are_parallel(x2 - x1, y2 - y1, x3 - x4, y3 - y4) and are_parallel(x3 - x2, y2 - y3, x4 - x1, y4 - y1)) \
        or (are_parallel(x3 - x1, y3 - y1, x2 - x4, y2 - y4) and are_parallel(x2 - x3, y2 - y3, x1 - x4, y1 - y4))

print(is_parallelogram(0, 0, 1, 1, 2, 1, 1, 0))
