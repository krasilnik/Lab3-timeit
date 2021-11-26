from json import load
from json import dump
from datetime import date
from random import randint

MENU_BORDER = 25
PIZZA_FILE = "pizza-of-the-day.json"
INGREDIENTS_FILE = "ingredients.json"


class BaseRandomPizza:

    def __init__(self):
        day = str(randint(0, 6))
        with open(PIZZA_FILE, "r") as f:
            data = load(f)
        self.ingredients = data[day]['ingredients']
        self.day = day

    @property
    def day(self):
        return self.__day

    @property
    def ingredients(self):
        return self.__ingredients

    @day.setter
    def day(self, day):
        if not isinstance(day, str):
            raise TypeError("Day has to be str type!")
        self.__day = day

    @ingredients.setter
    def ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise TypeError("Ingredients have to be list!")
        self.__ingredients = ingredients

    def __str__(self):
        with open(PIZZA_FILE, "r") as f:
            data = load(f)
            temp = '|  ' + str(data[self.day]['name']) + '\n'
        temp += '-' * MENU_BORDER + '\n'
        for index in self.ingredients:
            temp += '| ' + index + '\n'
        return temp

    def add_ingredients(self, ing):
        with open(INGREDIENTS_FILE, "r") as f:
            ingredients = load(f)
        if self.ingredients.count(ingredients[int(ing)]) > 0:
            self.ingredients.append("Extra " + ingredients[int(ing)])
        else:
            self.ingredients.append(ingredients[int(ing)])

    @staticmethod
    def show_ingredients():
        with open(INGREDIENTS_FILE, "r") as f:
            ingredients = load(f)
        temp = '|  Ingredients:\n' + '-' * MENU_BORDER + ' \n'
        for index in range(len(ingredients)):
            temp += str(index) + '  -  ' + ingredients[index] + ' \n'
        return temp

    def form_order(self):
        with open(PIZZA_FILE, "r") as f:
            data = load(f)
            dumped = data[self.day]
            dumped['ingredients'] = self.ingredients
            dumped['date'] = str(date.today())
        with open("order.json", 'w') as f:
            dump(dumped, f, indent=4)


class PizzaOfTheDay(BaseRandomPizza):

    def __init__(self):
        super().__init__()
        with open(PIZZA_FILE, "r") as f:
            self.day = str(date.today().weekday())
            data = load(f)
            self.day = list(data)[date.today().weekday()]


try:
    pizza = PizzaOfTheDay()
    while True:
        print('Your pizza-of-the-day for today is:\n' + str(pizza))
        temp_input = input('Would you like to add some ingredients? / If no - enter "0" to save your order...\n')
        if temp_input == '0':
            print("Your order completed! Thank you for choosing our pizzeria! ;)")
            break
        else:
            print(pizza.show_ingredients())
            pizza.add_ingredients(input('Please, choose what you want to add:\n'))
            pizza.form_order()
except SystemError:
    print('Error! Something went wrong...')
    







