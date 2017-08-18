# python3 find_procedure.py
#       Введите строку: INSERT
#       ... большой список файлов ...
#       Всего: 301
#       Введите строку: APPLICATION_SETUP
#       ... большой список файлов ...
#       Всего: 26
#       Введите строку: A400M
#       ... большой список файлов ...
#       Всего: 17
#       Введите строку: 0.0
#       Migrations/000_PSE_Application_setup.sql
#       Migrations/100_1-32_PSE_Application_setup.sql
#       Всего: 2
#       Введите строку: 2.0
#       Migrations/000_PSE_Application_setup.sql
#       Всего: 1


import os
from pprint import pprint


def get_all_files():
    all_files_list = []
    for file in os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Migrations')):
        all_files_list.append(file)
    return all_files_list


def get_files():
    all_files_list = get_all_files()
    while True:
        print('Введите строку для поиска: ')
        files_founded_list = []
        search_name = input()

        for file_name in all_files_list:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Migrations', file_name), 'r',
                      encoding="latin-1") as f:
                file = f.read()
            if search_name in file:
                files_founded_list.append(file_name)
        count = len(files_founded_list)

        all_files_list = files_founded_list

        for files in files_founded_list:
            print(files)
        print('Всего: {}'.format(count))

get_files()