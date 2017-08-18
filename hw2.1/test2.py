with open('test2.txt') as f:
	recipe = {}
	contains = []
	new_list = []
	for line in f:
		tmp = line.upper().strip()
		for s in range(int(f.readline().strip())):
		 	e = f.readline().strip().split('|')
		 	ing_list = list(map(str.strip, e))
		 	contains = {'ingridient_name': ing_list[0], 'quantity': ing_list[1], 'measure': e[2]}
		 	new_list.append(contains)
		recipe[tmp] = new_list
		print(recipe)
		 	# contains_new.append(ing_list)
		    # print(contains)
		 	# contains.append(ing_list)
		 	# print(contains[0])
		# recipe[tmp] = contains
		# print(contains[0])

		# list = f.readline().strip().split(' | ')
  #       # ing_list = list(map(str.strip, ing_list))
  #       print(list)
		# for s in range(int(f.readline().strip())):
		# 	e = f.readline().strip().split(' | ')
		# 	new_list.append(e)
		# 	recipe[tmp] = [e]
		# print(recipe)