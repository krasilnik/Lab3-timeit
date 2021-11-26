from datetime import datetime, date
import uuid
import json

ADVANCE_DATE = 60
LATE_DATE = 10
ADVANCE_TICKET_DISCOUNT = 0.6
STUDENT_TICKET_DISCOUNT = 0.5
LATE_TICKET_ADDITIONAL = 1.1

class Event:
    def __init__(self, title, date, price):
        if not isinstance(title, str):
            raise TypeError('Invalid type')
        if price <= 0:
            raise ValueError('Invalid value')
        self.title = title
        self.date = date
        self.price = price

    def write(self):
        with open('events.json', 'r') as f:
            data = json.load(f)

            event = {'title': self.title,
                     'date': self.date,
                     'price': self.price}

            data.append(event)

        with open('events.json', 'w') as write_file:
            json.dump(data, write_file, indent = 3)

    def __str__(self):
        return f'\nEvent: \n\tTitle: {self.title}\n\tDate: {self.date}\n\tPrice: {self.price}'

class RegularTicket:
    def __init__(self, price, event_title, type = "Regular ticket"):
        if not isinstance(price, (int, float)) or not isinstance(event_title, str) or not isinstance(type, str):
            raise TypeError('Invalid type')
        if price <= 0:
            raise ValueError('Invalid value')
        self.__type = type
        self.__number = str(uuid.uuid4().int)[:6]
        self.__price = price
        self.__event = event_title

    @property
    def price(self):
        return self.__price

    @property
    def type(self):
        return self.__type

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return f'\nTicket: \n\tType: {self.__type}\n\tNumber: {self.__number}\n\tPrice: {self.__price}\n\tEvent: ' \
               f'{self.__event}'

    def write(self):
        with open('tickets.json', 'r') as f:
            data = json.load(f)

            ticket = {'type': self.__type,
                      'number': self.__number,
                      'price': self.__price,
                      'event': self.__event}

            data.append(ticket)

        with open('tickets.json', 'w') as write_file:
            json.dump(data, write_file, indent = 3)

class AdvanceTicket(RegularTicket):
    def __init__(self, price, event):
        super().__init__(price * ADVANCE_TICKET_DISCOUNT, event, "Advance ticket")

class LateTicket(RegularTicket):
    def __init__(self, price, event):
        super().__init__(price * LATE_TICKET_ADDITIONAL, event, "Late ticket")

class StudentTicket(RegularTicket):
    def __init__(self, price, event):
        super().__init__(price * STUDENT_TICKET_DISCOUNT, event, "Student ticket")

class Order:
    def __init__(self):
        self.selected_event = None
        self.ticket = None

    def select(self):
        with open('events.json', 'r') as f:
            data = json.load(f)
            for i in data:
                temp_event = Event(i['title'], i['date'], i['price'])
                print(temp_event.__str__())
        selection = input('\nSelect your event: ')
        if not any(i['title'] == selection for i in data):
            raise ValueError('Invalid input')
        for i in data:
            if i['title'] == selection:
                self.selected_event = i

    @staticmethod
    def get_date_difference(event_date):
        data = datetime.now()
        current_date = (data.year, data.month, data.day)
        event_date = tuple(int(i) for i in reversed(event_date.split('.')))
        if current_date > event_date:
            raise TimeoutError('Event ended')
        return (date(data.year, data.month, data.day) - date(event_date[0], event_date[1], event_date[2])).days

    def make_order(self):
        ticket_type = input('\nEnter ticket type: Advanced/Student/Regular/Late\n')
        days_difference = abs(Order.get_date_difference(self.selected_event['date']))
        if not (ticket_type in ('Advanced', 'Student', 'Regular', 'Late')):
            Order.make_order(self)
        if ticket_type == 'Advanced':
            if days_difference < ADVANCE_DATE:
                raise TimeoutError('Sorry, you can not order advanced ticked, because '
                                   'less than 60 days left before the event')
            self.ticket = AdvanceTicket(self.selected_event['price'], self.selected_event['title'])
        elif ticket_type == 'Student':
            self.ticket = StudentTicket(self.selected_event['price'], self.selected_event['title'])
        elif ticket_type == 'Regular':
            self.ticket = RegularTicket(self.selected_event['price'], self.selected_event['title'])
        elif ticket_type == 'Late':
            if days_difference >= LATE_DATE:
                raise TimeoutError('Sorry, you can not order late ticked, because '
                                   'there are at least 10 days left before the event')
            self.ticket = LateTicket(self.selected_event['price'], self.selected_event['title'])
        self.ticket.write()

    @staticmethod
    def search_ticket(ticket_number):
        with open('tickets.json', 'r') as f:
            data = json.load(f)
        if not ticket_number or not isinstance(ticket_number, str):
            raise TypeError('Ticket ticket_number extinct')
        if not any(i['number'] == ticket_number for i in data):
            raise ValueError('Ticket extinct')
        res = None
        for i in data:
            if i['number'] == ticket_number:
                type = i['type']
                price = i['price']
                event = i['event']
                res = f'\nTicket:\n\tType: {type}\n\tNumber: {ticket_number}\n\tPrice: {price}\n\tEvent: {event}'
        return res

    def __str__(self):
        event_title = self.selected['title']
        return f'\nYour order:\n\tEvent: {event_title}\n\tTicket type: {self.ticket.type}\n\t' \
               f'Price: {self.ticket.price}\n\tNumber: {self.ticket.number}'

def main():
    order = Order()
    order.select()
    order.make_order()
    print(order.search_ticket("190157"))
    print(order.__str__())

main()








