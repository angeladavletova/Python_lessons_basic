# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt
from enum import Enum

class Triangle_point(Enum):
    A = 0
    B = 1
    C = 2

    def get_opposite_points(self):
        return [point for point in Triangle_point if point != self]

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.set(x1, y1, x2, y2, x3, y3)

    def calculate_distance(self, points):
        return sqrt((self._x[points[0]] - self._x[points[1]]) ** 2 + (self._y[points[0]] - self._y[points[1]]) ** 2)

    def calculate_perimeter(self):
        perimeter = 0
        for point in Triangle_point:
            perimeter += self.lengths[point]
        return perimeter

    def calculate_area(self):
        semiperimeter = self.calculate_perimeter() / 2
        return sqrt(semiperimeter * (semiperimeter - self.lengths[Triangle_point.A])
                    * (semiperimeter - self.lengths[Triangle_point.B]) \
                    * (semiperimeter - self.lengths[Triangle_point.C]))

    def calculate_heights(self, point):
        area = self.calculate_area()
        return 2 * area / self.lengths[point]

    def set(self, x1, y1, x2, y2, x3, y3):
        # все данные инкапсулированы
        self._x = {Triangle_point.A: x1, Triangle_point.B: x2, Triangle_point.C: x3}
        self._y = {Triangle_point.A: y1, Triangle_point.B: y2, Triangle_point.C: y3}
        # сторона a напротив вершины A, для b и c аналогично
        self.lengths = {}
        for point in Triangle_point:
            self.lengths[point] = self.calculate_distance(point.get_opposite_points())

triangle1 = Triangle(0, 0, 0, 1, 1, 0) # x1, y1, x2, y2, x3, y3 (координаты точек A, B, C подряд)
print('Длина высоты треугольника из вершин A =', triangle1.calculate_heights(Triangle_point.A))
# изменяем треугольник
triangle1.set(0, 0, 0, 2, 2, 0)
print('Площадь треугольника S =', triangle1.calculate_area())
print('Периметр треугольника P =', triangle1.calculate_perimeter())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt
from enum import Enum

class Quadrilateral_point(Enum):
    A = 0
    B = 1
    C = 2
    D = 3

    def get_next(self):
        return Quadrilateral_point((self.value + 1) % 4)

def calculate_area_trapeze(a, b, c, d):
    return 0.5 * (a + b) * sqrt(c ** 2 - 0.25 * (((b - a) ** 2 + c ** 2 - d ** 2) / (b - a)) ** 2)

class Isosceles_trapeze:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.set(x1, y1, x2, y2, x3, y3, x4, y4)

    def are_parall(self, point1, point2, point3, point4):
        return (self._x[point1] - self._x[point2]) * (self._y[point3] - self._y[point4]) \
               - (self._y[point1] - self._y[point2]) * (self._x[point3] - self._x[point4]) == 0

    def is_trapeze(self):
        return self.are_parall(Quadrilateral_point.A, Quadrilateral_point.B, Quadrilateral_point.C, Quadrilateral_point.D) \
            or self.are_parall(Quadrilateral_point.B, Quadrilateral_point.C, Quadrilateral_point.D, Quadrilateral_point.A)

    def calculate_perimeter(self):
        perimeter = 0
        for point in Quadrilateral_point:
            perimeter += self.lengths[point]
        return perimeter

    def calculate_area(self):
        if self.are_parall(Quadrilateral_point.A, Quadrilateral_point.B, Quadrilateral_point.C, Quadrilateral_point.D):
            return calculate_area_trapeze(self.lengths[Quadrilateral_point.A], self.lengths[Quadrilateral_point.C],
              self.lengths[Quadrilateral_point.D], self.lengths[Quadrilateral_point.B])
        elif self.are_parall(Quadrilateral_point.B, Quadrilateral_point.C, Quadrilateral_point.D, Quadrilateral_point.A):
            return calculate_area_trapeze(self.lengths[Quadrilateral_point.B], self.lengths[Quadrilateral_point.D],
              self.lengths[Quadrilateral_point.A], self.lengths[Quadrilateral_point.C])

    def is_isosceles_trapeze(self):
        return self.is_trapeze() and (self.lengths[Quadrilateral_point.A] == self.lengths[Quadrilateral_point.C]
                                      or self.lengths[Quadrilateral_point.B] == self.lengths[Quadrilateral_point.D])

    def calculate_distance(self, point1, point2):
        return sqrt((self._x[point1] - self._x[point2]) ** 2 + (self._y[point1] - self._y[point2]) ** 2)

    def set(self, x1, y1, x2, y2, x3, y3, x4, y4):
        # все данные инкапсулированы
        self._x = {Quadrilateral_point.A: x1, Quadrilateral_point.B: x2, Quadrilateral_point.C: x3,
                   Quadrilateral_point.D: x4}
        self._y = {Quadrilateral_point.A: y1, Quadrilateral_point.B: y2, Quadrilateral_point.C: y3,
                   Quadrilateral_point.D: y4}
        # длины сторон от заданной точки до следующей по очереди
        self.lengths = {}
        for point in Quadrilateral_point:
            self.lengths[point] = self.calculate_distance(point, point.get_next())

# в конструктор точки необходимо вводить по кругу
# (не важно с какой точки начинать и в какую сторону двигаться)
# первая точка обозначается A, вторая - B и т.д.

trapeze1 = Isosceles_trapeze(1, 1, 5, 1, 10, 0, 0, 0) # НЕ равнобедренная трапеция
trapeze2 = Isosceles_trapeze(0, 0, 1, 1, 2, 1, 3, 0) # равнобедренная трапеция
print('Действительно ли является первая трапеция трапецией?', trapeze1.is_trapeze())
print('Является ли первая трапеция равнобедренно?', trapeze1.is_isosceles_trapeze())
print('Действительно ли является вторая трапеция трапецией?', trapeze2.is_trapeze())
print('Является ли вторая трапеция равноедренной?', trapeze2.is_isosceles_trapeze())
print('Длина стороны из точки A в первой трапеции =', trapeze1.lengths[Quadrilateral_point.A])
print('Площадь первой трапеции S =', trapeze1.calculate_area())
print('Периметр второй трапеции P =', trapeze2.calculate_perimeter())

