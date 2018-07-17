# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создание копии указанного файла")
    print("rm <file_name> - удаление указанного файл")
    print("cd <full_path or relative_path> - изенение текущей директории на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('директория {} уже существует'.format(name))


def ping():
    print("pong")


def copy_file():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if os.path.isfile(name):
        new_file_name = "dupl_" + name
        if os.path.isfile(new_file_name):
            ans = input('Копия данного файла уже есть. Затереть ее новой? (Y/N)?\n')
            if ans == 'Y' or ans == 'y':
                shutil.copy(name, new_file_name)
                print('файл {} скопирован'.format(name))
            else:
                print('файл {} не скопирован'.format(name))
        else:
            shutil.copy(name, new_file_name)
            print('файл {} скопирован'.format(name))
    else:
        print('{} не может быть скопирован'.format(name))


def delete_file():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if os.path.isfile(name):
        ans = input('Вы уверены, что хотите удалить файл (Y/N)?:\n')
        if ans == 'Y' or ans == 'y':
            os.remove(name)
            print('файл {} удален'.format(name))
        else:
            print('удаление файла {} отменено'.format(name))
    else:
        print('нет такого файла {}'.format(name))


def change_dir():
    dir_path = os.path.join(os.getcwd(), name)
    os.chdir(dir_path)
    print('Текущая директория -', os.getcwd())


def present_working_dir():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": delete_file,
    "cd": change_dir,
    "ls": present_working_dir
}

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
