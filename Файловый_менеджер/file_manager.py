import os, shutil, sys
from config import main_folder

def print_work_folder():
    global current_directory
    print('/'+'/'.join(current_directory[1:]))


def path_reader(path, mode = True):
    global current_directory
    path = [item  for el in path.split('\\') for item in el.split('/')]
    if path[0] == '.':
        path = list(current_directory + path[1:])
    elif path[0] == '..':
        if len(current_directory) > 1:
            path = list(current_directory[:-1] + path[1:])
        else:
            path = list(current_directory + path[1:])
    elif path[0] == '':
        path[0] = main_folder
    else:
        path = list(current_directory + path)
    secondary = '/'+'/'.join(path[1:]) if mode else path
    return os.path.join(*path), secondary


def make_folder(*names, recursive = False):
    for name in names:
        path = path_reader(name)
        try:
            os.makedirs(path[0]) if recursive else os.mkdir(path[0]) 
        except FileExistsError:
            print(f'Директория уже существует: {path[1]}')
        except FileNotFoundError:
            print(f'Неверный путь: {path[1]}')


def make_folder_recursion(*names):
    make_folder(*names, recursive = True)


def remove_folder(*names, recursive = False):
    for name in names:
        path = path_reader(name)
        try:
            if recursive:
                tree = list(os.walk(path[0]))[::-1]
                for objects in tree:
                    for item in objects[1]:
                        os.rmdir(os.path.join(objects[0],item))
                    for item in objects[2]:
                        os.remove(os.path.join(objects[0],item))
                os.rmdir(objects[0])
            else:
                os.rmdir(path[0])
        except FileNotFoundError:
            print(f'Неверный путь {path[1]}')
        except OSError:
            print(f'Folder isn\'n empty {path[1]} (используйте remove_folder_recursion)')


def remove_folder_recursion(*names):
    remove_folder(*names, recursive = True)


def go_to_folder(name):
    global current_directory
    path = path_reader(name, mode = False)
    if os.path.exists(path[0]):
        current_directory = list(path[1])
    else:
        print('Нет такого файла или директории')


def create_file(*names):
    for name in names:
        path = path_reader(name)
        try:
            with open(path[0], 'x'):
                pass
        except FileExistsError:
            pass


def write_file(name):
    path = path_reader(name)
    print("Ctrl-Z (Windows) или Ctrl-D (Unix) для закрытия")
    try:
        with open(path[0], 'a') as file:
            while True:
                try:
                    file.write(input()+'\n')
                except EOFError:
                    break
    except FileExistsError:
        print(f'File doesn\'t exist {path[1]}')


def read_file(*names):
    for name in names:
        path = path_reader(name)
        try:
            with open(path[0], 'r') as file:
                    for line in file.readlines():
                        print(line, end = '')
        except FileExistsError:
            print(f'File doesn\'t exist {path[1]}')


def remove_file(*names):
    for name in names:
        path = path_reader(name)
        try:
            os.remove(path[0])
        except FileNotFoundError:
            print(f'Неверный путь {path[1]}')


def copy_file_to_folder(from_,to_):
    from_ = path_reader(from_)
    to_ = path_reader(to_)
    if sys.platform == 'win32':
        os.system(f'copy "{from_[0]}" "{to_[0]}"')
    else:
        os.system(f'cp -r {from_[0]} {to_[0]}')

def replace_file(from_, to_):
    from_ = path_reader(from_)
    to_ = path_reader(to_)
    try:
        os.replace(from_[0], to_[0])
    except FileNotFoundError:
        print(f'Неверный путь {from_[1], to_[1]}')


def rename(name, new_name):
    name = path_reader(name)
    new_name = path_reader(new_name)
    try:
        os.rename(name[0], new_name[0])
    except FileNotFoundError:
        print(f'Неверный путь {name[1], new_name[1]}')


def print_help_string():
    help_string = r''''print_work_folder' -- Напечать рабочую папку
'make_folder [folder_name] [folder_name] ..' -- Создание папок
'make_folder_recursion [folder_name] [folder_name] ..' -- Создание папок рекурсивными
'remove_folder [folders_name] [folder_name] ..' -- Удаление папки
'remove_folder_recursion [folder_name] [folder_name] ..' -- Удаление рекурсивных папок
'go_to_folder [folder_name]' -- перейти в папку, изменить текущую папку
'create_file [file_name] [file_name] ..' -- создание файлов
'write_file [file_name]' -- запись в файл, ввод строки потока
'read_file [file_name] [file_name] ..' -- отображение файлов
'remove_file [file_name] [file_name] ..' -- удаление файлов
'copy_file_to_folder [file_from] [file_to]' -- скопировать имя_файла в папку/новый_файл
'replace_file [file_folder] [file_folder]' -- заменить файл/папку на другой файл/папку
'rename [file_folder]' -- переименовать файл или папку
'exit' -- выход
'help' -- чтобы получить список команд'''
    print(help_string)

def command_prompt():
    global current_directory
    commands = {
        'print_work_folder':print_work_folder,
        'make_folder':make_folder,
        'make_folder_recursion':make_folder_recursion,
        'remove_folder':remove_folder,
        'remove_folder_recursion':remove_folder_recursion,
        'go_to_folder':go_to_folder,
        'create_file':create_file,
        'write_file':write_file,
        'read_file':read_file,
        'remove_file':remove_file,
        'copy_file_to_folder':copy_file_to_folder,
        'replace_file':replace_file,
        'rename':rename,
        'help':print_help_string
    }

    while True:
        command = input('command_prompt:/'+'/'.join(current_directory[1:])+'$ ').split()
        if command[0] == 'exit':
            break
        try:
            commands[command[0]](*command[1:])
        except KeyError:
            print('Команда недоступна. Используйте "help", чтобы увидеть лист команд')
        except PermissionError:
            print('В разрешении отказано')


current_directory = [main_folder]
command_prompt()