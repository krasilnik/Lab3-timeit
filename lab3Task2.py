from datetime import date
import calendar
import uuid
import json

ALL_INGREDIENTS = ["Tomato sauce", "Mozzarella", "Oregano", "Parmesan", "Eggs", "Bacon", "Anchovies", "Sausage",
                   "Fries", "Spicy salami", "Chili", "Ham", "Artichokes", "Mushrooms", "Olives", "Vienna sausage"]

class Pizza:
    def __init__(self, name, price, ingredients):
        if not isinstance(price, (int, float)) or not isinstance(name, str):
            raise TypeError('Invalid type')
        if price <= 0:
            raise ValueError('Invalid value')
        self.__name = name
        self.__price = price
        self.__ingredients = ingredients

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @property
    def ingredients(self):
        return self.__ingredients

    def __str__(self):
        the_ingredients_of_todays_pizza = ", ".join(self.__ingredients)
        return f'\nPizza:\n\tName: {self.__name}\n\tPrice: {self.__price}' \
               f'\n\tIngredients: {the_ingredients_of_todays_pizza}'

    def add_ingredient(self, ingredient):
        self.__ingredients.append(ingredient)

class MondayPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita", 145, ["Tomato sauce", "Mozzarella", "Oregano"])

class TuesdayPizza(Pizza):
    def __init__(self):
        super().__init__("Carbonara", 170, ["Tomato sauce", "Mozzarella", "Parmesan", "Eggs", "Bacon"])

class WednesdayPizza(Pizza):
    def __init__(self):
        super().__init__("Napoletana", 190, ["Tomato sauce", "Mozzarella", "Anchovies"])

class ThursdayPizza(Pizza):
    def __init__(self):
        super().__init__("Americana", 210, ["Tomato sauce", "Mozzarella", "Sausage", "Fries"])

class FridayPizza(Pizza):
    def __init__(self):
        super().__init__("Diavola", 185, ["Tomato sauce", "Mozzarella", "Spicy salami", "Chili"])

class SaturdayPizza(Pizza):
    def __init__(self):
        super().__init__("Capricciosa", 240, ["Tomato sauce", "Mozzarella", "Ham", "Artichokes", "Mushrooms", "Olives"])

class SundayPizza(Pizza):
    def __init__(self):
        super().__init__("Tedesca", 160, ["Tomato sauce", "Mozzarella", "Vienna sausage"])

class Order:
    def __init__(self):
        self.number = str(uuid.uuid4().int)[:6]
        self.pizza = None
        self.count = 0

    def current_day(self):
        current_date = date.today()
        return calendar.day_name[current_date.weekday()]

    def make_order(self):
        class_name = self.current_day() + "Pizza"
        pizza_dict = {"MondayPizza": MondayPizza(), "TuesdayPizza": TuesdayPizza(), "WednesdayPizza": WednesdayPizza(),
                "ThursdayPizza": ThursdayPizza(), "FridayPizza": FridayPizza(), "SaturdayPizza": SaturdayPizza(),
                "SundayPizza": SundayPizza()}
        self.pizza = pizza_dict[class_name]
        the_ingredients_of_todays_pizza = ", ".join(self.pizza.ingredients)
        ingredients = set(ALL_INGREDIENTS) - set(self.pizza.ingredients)
        ingredients_to_add = ", ".join(ingredients)
        print(f'\nToday is {self.current_day()} and today we have {self.pizza.name}! '
              f'With ingredients: {the_ingredients_of_todays_pizza}'
              f'\nDo you want to add something from this ingredients: {ingredients_to_add}?'
              f'\nTo refuse write no or to add write name of ingredient: ')
        self.choose(ingredients)
        count = int(input("How many pizzas do you want? "))
        if count <= 0:
            raise ValueError("Invalid value")
        self.count = count
        self.write()

    def choose(self, ingredients, question = ""):
        choice = input(question)
        if choice == "no":
            print("Ok!")
            return
        elif choice not in ingredients:
            raise ValueError("Invalid input")
        self.pizza.add_ingredient(choice)
        self.choose(ingredients, "Do you want add more ingredients? ")

    def __str__(self):
        return '\nOrder:' + self.pizza.__str__() + f'\n\tCount: {self.count}\n\tTotal: {self.pizza.price * self.count}'

    def write(self):
        with open('pizza.json', 'r') as f:
            data = json.load(f)

            order = {'number': self.number,
                     'pizza': self.pizza.name,
                     'count': self.count,
                     'total': self.pizza.price * self.count}

            data.append(order)

        with open('pizza.json', 'w') as write_file:
            json.dump(data, write_file, indent = 3)

    def find_order(self, order_number):
        with open('pizza.json', 'r') as f:
            data = json.load(f)
        if not order_number or not isinstance(order_number, str):
            raise TypeError('Ticket ticket_number extinct')
        if not any(i['number'] == order_number for i in data):
            raise ValueError('Ticket extinct')
        res = None
        for i in data:
            if i['number'] == order_number:
                name = i['pizza']
                count = i['count']
                total = i['total']
                res = f'\nOrder:\nPizza:\n\tNumber: {order_number}\n\tName: {name}\n\tCount: {count}\n\tTotal: {total}'
        return res

def main():
    order = Order()
    order.make_order()
    print(order.__str__())
    print(order.find_order("798431"))

main()






