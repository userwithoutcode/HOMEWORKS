
def get_file():
  with open('homework_2.1.txt') as f:
    cook_book = {}
    for line in f:
      dish_name = line.upper().strip()
      contains = []
      for i in range(int(f.readline())):
        ingredient = f.readline().split("|")
        ing_list = list(map(str.strip, ingredient))
        contains.append({'ingridient_name': ing_list[0], 'quantity': int(ing_list[1]), 'measure': ing_list[2]})
      cook_book[dish_name] = contains
      f.readline()
    return cook_book

def get_shop_list_by_dishes(cook_book, dishes, person_count):
  # cook_book = get_file()
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
# for shop_list_item in shop_list.values():
#   print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))
  for shop_list_item in shop_list.values():
    print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))

def create_shop_list():
  cook_book = get_file()
  dishes = input('Введите блюда в расчете на одного человека').upper().split(', ')
  person_count = int(input('Введите количество человек'))
  shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()


