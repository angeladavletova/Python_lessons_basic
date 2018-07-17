# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
    
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
from os.path import isfile
import shutil

def create_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Успешно создано')
    except FileExistsError:
        print('Невозможно создать', dir_name)

def delete_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.removedirs(dir_path)
        #os.rmdir(dir_path)
        print('Успешно удалено')
    except FileNotFoundError:
        print('Невозможно удалить', dir_name)

def main():
    #Задача-1.1
    for i in range(1, 10):
        create_dir('dir_' + str(i))
    #Задача-1.2
    for i in range(1, 10):
        delete_dir('dir_' + str(i))
        
    #Задача-2
    print('Папки текущей директории:', [dir for dir in os.listdir(os.getcwd()) if os.path.isdir(dir)]) #not isfile(dir)])
    
    #Задача-3
    shutil.copy(__file__, __file__ + '.dupl')

if __name__ == "__main__":
    main()
