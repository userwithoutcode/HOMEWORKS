#Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
#l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
#s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
#a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
      
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
      
      
def get_name_by_numbers():
  p = (input('Введите номер документа: '))
  for document in documents:
    # if people['number'] in input_list:
    #   print(input_list[people['name']])
    if document["number"] == p:
      print(document['name'])
    # elif document["number"] == p for document in add_new_document():
    #   print(document['name'])
    
def get_shelfs():
  s = (input('Введите номер документa: '))
  for shelf, doc in directories.items():
    if s in doc:
      print(shelf)

def get_list_doc():
  for document in documents:
    print (document['type'], document["number"],  document['name'])
    
def add_new_document():
  t = (input('Введите тип документа:  '))
  d = (input('Введите номер документа: '))
  n = (input('Введите имя человека: '))
  s = (input('Введите номер полки: '))
  new_doc = {"type": t, "number": d, "name": n}
  documents.append(new_doc)
  directories[s] = [d]
  print(documents)
  print(directories)
  return documents

def input_a_letter():
  c = (input("Введите команду: people, list, shelf, add\nВведите для завершения программы: quit\n"))
  return c

def choose_input_list():
  while True:
    command = input_a_letter()
    if command == 'people':
      get_name_by_numbers()
    elif command == 'shelf':
      get_shelfs()
    elif command == 'list':
      get_list_doc()
    elif command == 'add':
      add_new_document()
    elif command == 'quit':
      break
    
    
choose_input_list()
