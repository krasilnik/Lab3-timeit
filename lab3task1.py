
import uuid

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f'{self.name}, {self.date}'


class Ticket:
    def __init__(self, event, price, type = "Regular"):
        self.__ticket_type = type
        self.__id = uuid.uuid1()
        self.__event = event
        self.__price = price

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"\n Ticket's type: {self.__ticket_type} \n\tTicket's id: {self.__id}\n\tEvent's name and date: {self.__event}\n\tTicket's price: {self.__price}"

class Student(Ticket):
    def __init__(self, event, price):
            super().__init__(event, price * 0.5, "Student")

class Late(Ticket):
    def __init__(self, event, price):
            super().__init__(event, price * 1.2, "Late")

class Advance(Ticket):
    def __init__(self, event, price):
            super().__init__(event, price * 0.4, "Advance")

def start():
    normal_price = 150
    some_event = Event("some_event", "15.01.2002")
    first = Ticket(some_event, normal_price)
    second = Student(some_event, normal_price)
    third = Late(some_event, normal_price)
    forth = Advance(some_event, normal_price)
    print(first.__str__())
    print(second.__str__())
    print(third.__str__())
    print(forth.__str__())

start()
