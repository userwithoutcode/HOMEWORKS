
def get_file():
  with open('h2.2.txt') as f:
    cook_b = {}
    for line in f:
      tmp = line.upper().strip()
      contains = []
      for i in range(int(f.readline())):
        ingredient = f.readline().split("|")
        ing_list = list(map(str.strip, ingredient))
        contains.append({'ingridient_name': ing_list[0], 'quantity': int(ing_list[1]), 'measure': ing_list[2]})
        cook_b[tmp] = contains
      f.readline()

  return cook_b

cook_b = get_file()

import yaml
with open('h_yaml_2.2.yml', 'w') as f:
  yaml.dump(cook_b, f, allow_unicode=True)
