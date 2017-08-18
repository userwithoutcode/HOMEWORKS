import os
from pprint import pprint

def get_all_files():
    all_files_list = []
    for file in os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Migrations')):
        all_files_list.append(file)
    return all_files_list

all_files = get_all_files()
while True:
    len_all_files = len(all_files)
    if len_all_files == 0:
        break
    new_all_files = all_files[:len_all_files - 1]
    all_files = new_all_files

def get_files():
    all_files_list = get_all_files()
    insert_list = []
    for element in all_files_list:
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Migrations', element), 'r', encoding="latin-1") as f:
            file = f.read()
            if command in file:
                insert_list.append(element)

    return insert_list

get_files()


def input_request():
    while True:
        command = input('Введите слово или значение')
        if command in get_files():
            pprint(insert_list)
            print(len(insert_list))

        if command == "quit":
            break

input_request()