import json
import uuid
from datetime import date
import calendar


class Pizza:
    def __init__(self, name, price, ingredients):
        self.__name = name
        self.__price = price
        self.__ingredients = ingredients

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, (str)):
            raise TypeError("Name must be a string type")
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Pizza's price must be a digit")
        if value <= 0:
            raise ValueError("Pizza cant cost nothing!")
        self.__price = value

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, (list)):
            raise TypeError("Ingredients type must be sting")
        self.__ingredients = value

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        return f"\t Pizza's name: {self.__name} \n\t Pizza's price: {self.__price} \n\t ingredients: {self.__ingredients} \n"

class MondayPizza(Pizza):
    def __init__(self):
        super().__init__("Neapolitan", 145, ["tomatoes", "garlic", "oregano"])

class TuesdayPizza(Pizza):
    def __init__(self):
        super().__init__("Chicago", 170, ["tomato sauce", "ground beef", "pepperoni", "green peppers", "mushrooms"])

class WednesdayPizza(Pizza):
    def __init__(self):
        super().__init__("New York-Style", 190, ["mushroom and anchovies", "Mozzarella", "pepperoni and sausage", "tomato sauce"])

class ThursdayPizza(Pizza):
    def __init__(self):
        super().__init__("Sicilian", 210, ["robust tomato sauce", "bits of tomato", "onion", "anchovies"])

class FridayPizza(Pizza):
    def __init__(self):
        super().__init__("Greek", 185, ["tangy tomato paste", "mozzarella and cheddar", "black olives", "red onion"])

class SaturdayPizza(Pizza):
    def __init__(self):
        super().__init__("California", 240, ["chicken", "artichokes", "goat cheese", "egg"])

class SundayPizza(Pizza):
    def __init__(self):
        super().__init__("Detroit", 160, ["pepperoni", "brick Wisconsin cheese", "tomato sause"])


class Order:
    def __init__(self):
        self.id = str(uuid.uuid4().int)
        self.pizza = 0

    def day(self):
        today_date = date.today()
        return calendar.day_name[today_date.weekday()]

    def your_order(self):
        name = self.day()
        dict = {"Monday": MondayPizza(), "Tuesday": TuesdayPizza(), "Wednesday": WednesdayPizza(),
                "Thursday": ThursdayPizza(), "Friday": FridayPizza(), "Saturday": SaturdayPizza(),
                "Sunday": SundayPizza()}
        self.pizza = dict[name]
        print(f"Today we have {self.pizza.name} pizza! \n if you wand to add an ingredient - type it. If not - type 'no'")
        self.add()
        self.write()

    def add(self, text = ""):
        answer = input(text)
        if answer == 'no':
            print("any extra ingrediets")
            return
        else:
            self.pizza.add_ingredient(answer)
        self.add("Do you want more extra ingredients? If yes - type it")

    def write(self):
        with open('pizza.json', 'r') as f:
            data = json.load(f)

            order = {'id': self.id,
                     'pizza': self.pizza.name,}

            data.append(order)

        with open('pizza.json', 'w') as write_file:
            json.dump(data, write_file, indent=3)


def main():
    order = Order()
    order.your_order()
    print(order.__str__())

main()








