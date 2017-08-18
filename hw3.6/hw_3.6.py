class Animals:
    type_of_product = None
    sound = None
    name = None

    def __init__(self, name):
        self.name = name

    def sound_of_animal(self):
        print('I can say {}'.format(self.sound))

    def type_of_products(self):
        print('You can enjoy my {}'.format(self.type_of_product))

    def say_your_name(self):
        print('Hello my dear little ones, My name {}'.format(self.name))


# Парнокопытные
class Artiodactyls(Animals):
    description_1 = 'hooves'
    description_2 = 'horns'
    type_of_product = 'meat'
    sound = 'example'
    name = 'example'
    color = 'example'

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


# Пернатые
class Birds(Animals):
    description_1 = 'wings'
    description_2 = 'beak'
    type_of_product = 'egg'
    sound = 'example'
    name = 'example'
    color = 'example'

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


class Cows(Artiodactyls):
    type_of_product = 'meat and milk'
    sound = 'MUUUUUUUUUUUUUUU'


class Goats(Artiodactyls):
    type_of_product = 'Diet Milk'
    sound = 'MEEEEEEEEE'


class Sheeps(Artiodactyls):
    type_of_product = 'meat and wool'
    sound = 'Be Be Beeee'


class Pigs(Artiodactyls):
    type_of_product = 'meat and lard'
    sound = 'Hru Hru Hru'


class Duck(Birds):
    type_of_product = 'Meat'
    sound = 'Krya Krya Krya'


class Goose(Birds):
    type_of_product = 'feather'
    sound = 'Ga Ga Ga'


class Chicken(Birds):
    type_of_product = 'meat and egg'
    sound = 'Ko Ko Ko'


cow_1 = Cows('Marfa', 'black&white')
goat_1 = Goats('Volodya', 'white')
sheep_1 = Sheeps('Selma', 'grey')
pig_1 = Pigs('Boris', 'pinky')
pig_2 = Pigs('Morris', 'spotted')

duck_1 = Duck('MacDuck', 'grey')
goose_1 = Goose('Hiddink', 'grey')
chicken_1 = Chicken('Coo', 'yellow')

print('---------------')
cow_1.say_your_name()
cow_1.sound_of_animal()
cow_1.type_of_products()
print('My color', cow_1.color)
print('---------------')
goat_1.say_your_name()
goat_1.sound_of_animal()
goat_1.type_of_products()
print('My color', goat_1.color)
print('---------------')
sheep_1.say_your_name()
sheep_1.sound_of_animal()
sheep_1.type_of_products()
print('My color', sheep_1.color)
print('---------------')
pig_1.say_your_name()
pig_1.sound_of_animal()
pig_1.type_of_products()
print('My color', pig_1.color)
print('---------------')
pig_2.say_your_name()
pig_2.sound_of_animal()
pig_2.type_of_products()
print('My color', pig_2.color)
print('---------------')
duck_1.say_your_name()
duck_1.sound_of_animal()
duck_1.type_of_products()
print('My color', duck_1.color)
print('---------------')
goose_1.say_your_name()
goose_1.sound_of_animal()
goose_1.type_of_products()
print('My color', goose_1.color)
print('---------------')
chicken_1.say_your_name()
chicken_1.sound_of_animal()
chicken_1.type_of_products()
print('My color', chicken_1.color)
print('---------------')
