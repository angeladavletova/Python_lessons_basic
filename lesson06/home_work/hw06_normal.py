# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name, surname, patronymic, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_date = birth_date
    def get_full_name(self):
        return self.name + ' ' + self.surname + ' ' + self.patronymic
    def get_surname_initials(self):
        return self.surname + ' ' + self.name[0] + '.' + self.patronymic[0] + '.'
    def set_name(self, new_name):
        self.name = new_name

class Teacher(Person):
    def __init__(self, name, surname, patronymic, birth_date, school, teach_subject):
        Person.__init__(self, name, surname, patronymic, birth_date)
        self.school = school
        self.teach_subject = teach_subject

class Class_room:
    def __init__(self, class_room, teachers):
        self._class_room = {'class_num': int(class_room.split()[0]), 'class_char': class_room.split()[1]}
        self.teachers_dict = {t.teach_subject: t for t in teachers}

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

class Student(Person):
    def __init__(self, name, surname, patronymic, birth_date, school, class_room, parents):
        Person.__init__(self, name, surname, patronymic, birth_date)
        self.school = school
        self.class_room = class_room
        self.parents = parents

    def next_class(self):
        self._class_room['class_num'] += 1

teachers = [Teacher('Нина', 'Петрова', 'Геннадьвна', '11.11.1980', '2 лицей', 'математика'),
            Teacher('Любовь', 'Васильева', 'Анатольевна', '10.12.1981', '2 лицей', 'русский язык'),
            Teacher('Екатерина', 'Федорова', 'Ивановна', '01.10.1979', '2 лицей', 'литература'),
            Teacher('Любовь', 'Иванова', 'Викторовна', '14.02.1981', '2 лицей', 'математика'),

            Teacher('Надежда', 'Львова', 'Васильевна', '10.05.1977', '8 гимназия', 'русский язык'),
            Teacher('Петр', 'Николаев', 'Анатльевич', '18.02.1971', '8 гимназия', 'математика'),
            Teacher('Сергей', 'Егоров', 'Петрович', '19.09.1970', '8 гимназия', 'русский язык'),
            Teacher('Анна', 'Сергеева', 'Андреева', '11.10.1982', '8 гимназия', 'литература')]

class_rooms = [Class_room('5 А', [teachers[0], teachers[1], teachers[2]]),
              Class_room('7 А', [teachers[3], teachers[1], teachers[2]]),
              Class_room('3 Д', [teachers[5], teachers[4], teachers[2]]),
              Class_room('5 В', [teachers[5], teachers[6], teachers[7]])]

parents = [Person("Павел", "Алевсеев", "Сергеевич", '12.11.1979'),
           Person("Инна", "Александрова", "Павловна", '03.11.1979'),
           Person('Петр', 'Николаев', 'Анатльевич', '18.02.1971'),
           Person('Анна', 'Сергеева', 'Андреева', '11.10.1982')]

students = [Student("Александр", "Иванов", "Андреевич", '10.11.1998', "2 лицей", class_rooms[0], [parents[0], parents[1]]),
            Student("Петр", "Сидоров", "Александрович", '10.01.2004', "2 лицей", class_rooms[0], [parents[0], parents[1]]),
            Student("Анна", "Андреева", "Петровна", '12.11.1999', "2 лицей", class_rooms[1], [parents[2]]),
            Student("Иван", "Петров", "Александрович", '10.11.1999', "2 лицей", class_rooms[1], [parents[0], parents[1]]),
            Student("Сергей", "Сергеев", "Иванович", '11.11.1999', "8 гимназия", class_rooms[2], []),
            Student("Павел", "Алевсеев", "Сергеевич", '04.11.2003', "8 гимназия", class_rooms[2], []),
            Student("Инна", "Александрова", "Павловна", '03.11.1999', "8 гимназия", class_rooms[3], [parents[0], parents[1]]),
            Student("Мария", "Яковлева", "Алексеевна", '11.11.1999', "8 гимназия", class_rooms[3], [])]

# 1. Получить полный список всех классов школы

print('1. Полный список всех классов школы')
for cl in class_rooms:
    print(cl.class_room)

print()

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")

def get_list_students(class_room):
    return [st.get_surname_initials() for st in students if st.class_room == class_room]

print('2. Список всех учеников в', class_rooms[0].class_room)
print(get_list_students(class_rooms[0]))
print()

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)

print('3. Список всех предметов ученика', students[0].get_surname_initials())
for subject in students[0].class_room.teachers_dict.keys():
    print(subject)
    
#print(students[0].class_room.teachers_dict.keys())
print()

# 4. Узнать ФИО родителей указанного ученика
print('4. ФИО родителей ученика', students[0].get_surname_initials())
for parent in students[0].parents:
    print(parent.get_full_name())

print()

# 5. Получить список всех Учителей, преподающих в указанном классе

print('5. Список учителей в классе', class_rooms[0].class_room)
for teacher in class_rooms[0].teachers_dict.values():
    print(teacher.get_full_name())
