# -*- coding: utf-8 -*-
"""calc
   Implements the Restaurant
"""

import random
from datetime import date, datetime
from typing import Union, List
from collections import deque


class Restaurant:
    """
    Implement the restaurant
    """

    def __init__(self, count_tables=30, free_tables=30):
        self.count_tables = count_tables
        self.free_tables = free_tables
        self.busy_tables = set()
        self.barmen = None
        self.waiter = None
        self.chef = None
        self.online_operator = None
        self.menu = Menu('Menu')
        self.guests = deque([])
        self.online_guests = deque([])

    def add_tables(self, count: int):
        """
        Add new tables to count all tables of the restaurant.
        """
        self.count_tables += count
        self.free_tables += count

    def update_free_tables(self, is_come_customer: bool = True):
        """
        Update count free tables when customer go out from the restaurant.
        """
        if is_come_customer:
            self.free_tables -= 1
        else:
            self.free_tables += 1

    def update_busy_tables(self, table_number: int, is_come_customer: bool = True):
        """
        Update count of busy tables when customer is reserved the table or come to restaurant.
        """
        if is_come_customer:
            self.busy_tables.add(table_number)
        else:
            self.busy_tables.remove(table_number)

    def hire_employees(self):
        """
        Create employees after creating restaurant.
        """
        self.chef = Chef('Gleb', date(1995, 12, 31))
        self.waiter = Waiter("Lena", date(1995, 12, 31))
        self.barmen = Barmen('Den', date(1995, 12, 31))
        self.online_operator = OnlineOperator('Vlad', date(1995, 12, 31))


class MenuItem:
    """
    Implement simple MenuItem
    """
    def __init__(self, name: str, price: float, portion: int, type_food: str):
        self.name = name
        self.price = price
        self.portion = portion
        self.type_food = type_food

    def update_price(self, price: float):
        """
        Update price for the menu item.
        """
        self.price = price

    def update_portion(self, portion: int):
        """
        Update weight of the portion.
        """
        self.portion = portion


class Menu:
    """
    Implement simple Menu
    """
    def __init__(self, title: str):
        self.title = title
        self.menu_items = {'food': [], 'drinks': []}

    def add_menu_item(self, menu_item: MenuItem, type_item: str = 'food'):
        """
        Add menu item to the menu.
        """
        if type_item == 'food':
            self.menu_items['food'].append(menu_item)
        else:
            self.menu_items['drinks'].append(menu_item)

    def remove_menu_item(self, menu_item: MenuItem, type_item: str = 'food'):
        """
        Remove menu item from the menu.
        """
        try:
            self.menu_items.get(type_item).remove(menu_item)
        except ValueError as ex:
            print(ex)


class BaseOrder:
    """
    Implementation of simple BaseOrder.
    """
    order_id = 0

    def __init__(self):
        BaseOrder.order_id += 1
        self.order_id = BaseOrder.order_id
        self.order_status = False
        self.customer_order = []

    def add_meal(self, items: List[MenuItem]):
        """
        Add meal to customer order.
        """
        self.customer_order.extend(items)

    def remove_meal(self, item_of_order):
        """
        Remove meal from customer order.
        """
        try:
            self.customer_order.remove(item_of_order)
        except ValueError as ex:
            print(ex)

    def __str__(self):
        return f"Order of customer-food: {self.customer_order[0].name}, drink:" \
               f"{self.customer_order[1].name}"


class OnlineOrder(BaseOrder):
    """
    Implement the OnlineOrder
    """

    def __init__(self, time_delivery: datetime, address: str):
        self.time_delivery = time_delivery
        self.address = address
        super().__init__()


class Employee:
    """
    Implementation base class for Employee. All Employee will extend this class.
    """

    def __init__(self, name: str, birthday: date):
        self.name = name
        self._age = Employee.define_age_employee(birthday, Employee.year_is(date.today().year))
        self._birthday = birthday

    @staticmethod
    def year_is(year: int) -> int:
        """
        Define whether a year is high or not.
        """
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 366
        return 365

    @staticmethod
    def define_age_employee(birthday: date, divider: int) -> int:
        """
        Define age every employee.
        """
        delta = date.today() - birthday
        age = int(delta.days / divider)
        return age


class Chef(Employee):
    """
    Implement Chef of restaurant.
    """

    def __init__(self, name: str, birthday: date):
        self.orders = deque([])
        Employee.__init__(self, name, birthday)

    def take_order(self, order: MenuItem):
        """
        Take order form the waiter.
        """
        self.orders.append(order)
        print(f"Chef has taken order {order.name}")

    def cook(self):
        """
        Cook the order.
        """
        if self.orders:
            order = self.orders.popleft()
            print(f'Chef is cooking the order {order.name}')
        else:
            print('All orders were cooked')

    @staticmethod
    def give_order_to_waiter(order: MenuItem):
        """
        Chef give order to waiter.
        """
        print(f'Chef give order to waiter: {order.name}')


class Barmen(Employee):
    """
    Implement the Barmen of the restaurant.
    """

    def __init__(self, name: str, birthday: date):
        self.orders = deque([])
        Employee.__init__(self, name, birthday)

    def take_order(self, order: MenuItem):
        """
        Take order form the waiter.
        """
        self.orders.append(order)
        print(f"Barmen has taken order {order.name}")

    def cook(self):
        """
        Cook the order
        """
        if self.orders:
            order = self.orders.popleft()
            print(f'Barmen is cooking the order {order.name}')
        else:
            print('All orders were cooked')

    @staticmethod
    def give_order_to_waiter(order: MenuItem):
        """
        Barmen give order to waiter.
        """
        print(f'Barmen give order to waiter: {order.name}')


class Waiter(Employee):
    """
    Implement the Waiter of the Restaurant.
    """

    def __init__(self, name: str, birthday: date):
        self.orders = dict()
        super().__init__(name, birthday)

    def create_order(self, order: BaseOrder, table_number: int):
        """
        Create order for customer.
        """
        self.orders[table_number] = order
        print(f'Waiter has created order: {order.customer_order[0].name} and '
              f'{order.customer_order[1].name}')

    def set_status_order(self, table_number: int):
        """
        Set status order to True when order is cooked
        """
        self.orders[table_number].order_status = True

    def give_order_to_chef(self, table_number: int):
        """
        Waiter is giving order to Chef
        """
        print(f'Waiter is giving order to Chef: {self.orders[table_number].customer_order[0].name}')

    def give_order_to_customer(self, table_number: int):
        """
        Waiter is giving order to Customer.
        """
        print(f'Waiter is giving order to Customer: {self.orders[table_number]}')
        self.orders.pop(table_number)

    def give_order_to_barmen(self, table_number: int):
        """
        Waiter is giving order to Barmen
        """
        print(f'Waiter is giving order to Barmen: '
              f'{self.orders[table_number].customer_order[1].name}')


class OnlineOperator(Employee):
    """
    Implement OnlineOperator of the restaurant.
    """

    def __init__(self, name: str, birthday: date):
        self.orders = dict()
        Employee.__init__(self, name, birthday)

    def create_order(self, order: OnlineOrder, address: str):
        """
        Create order for customer.
        """
        self.orders[address] = order
        print(f'Online Operator has created order: {order.customer_order[0].name} '
              f'and {order.customer_order[1].name}')

    def set_status_order(self, address: str):
        """
        Set status order to True when order is cooked
        """
        self.orders[address].order_status = True

    def give_order_to_chef(self, address: str):
        """
        Online Operator is giving order to Chef.
        """
        print(f'Online Operator is giving order to Chef: '
              f'{self.orders[address].customer_order[0].name}')

    def give_order_to_customer(self, address: str):
        """
        Online Operator is giving order to Customer.
        """
        print(f'Online Operator is giving order to Customer: {self.orders[address]}')
        self.orders.pop(address)

    def give_order_to_barmen(self, address: str):
        """
        Online Operator is giving order to Barmen
        """
        print(f'Online Operator is giving order to Barmen: '
              f'{self.orders[address].customer_order[1].name}')


class Customer:
    """
    Implement simple Customer.
    """

    def __init__(self, name: str, table_number=0):
        self.name = name
        self.table_number = table_number
        self.restaurant = None
        self.order = None

    def make_reservation(self, restaurant: Restaurant):
        """
        Make reservation of free table in restaurant.
        """
        self.restaurant = restaurant
        while True:
            num_table = random.randint(1, 30)
            if num_table not in self.restaurant.busy_tables and self.restaurant.free_tables != 0:
                self.restaurant.update_busy_tables(num_table, is_come_customer=True)
                self.restaurant.update_free_tables(is_come_customer=True)
                self.table_number = num_table
                break

    def come_to_restaurant(self):
        """
        Customer come to restaurant.
        """
        self.restaurant.guests.append(self)
        print(f'Customer with name {self.name} come to restaurant and he Reserved '
              f'table: {self.table_number}')

    def call_to_restaurant(self, restaurant: Restaurant):
        """
        Customer call to restaurant make an order
        """
        self.restaurant = restaurant
        self.restaurant.online_guests.append(self)
        print(f'Customer with name {self.name} calling to restaurant')

    def request_order(self, menu: Menu, order: Union[BaseOrder, OnlineOrder]):
        """
        Customer create new order and give the order to waiter.
        """
        self.order = order
        my_order_food = random.choice(menu.menu_items.get('food'))
        my_order_drinks = random.choice(menu.menu_items.get('drinks'))
        self.order.add_meal([my_order_food, my_order_drinks])
        return self.order

    def ask_bill(self):
        """
        Customer ask bill for the order.
        """
        print(f'Customer ask bill for the meal: {self.order}')

    def pay_for_bill(self):
        """
        Customer pay for the order.
        """
        cost = 0
        for item_food in self.order.customer_order:
            cost += item_food.price
        print(f'Customer is paying {cost} GRN')


borsch = MenuItem("borsch", 50, 300, 'food')
soup = MenuItem("soup", 50, 300, 'food')
seafood_salad = MenuItem("seafood salad", 300, 300, 'food')
cutlet = MenuItem("cutlet", 50, 120, 'food')
chop = MenuItem("chop", 60, 150, 'food')
coffee = MenuItem("coffee", 50, 250, 'drinks')
whiskey = MenuItem("whiskey", 100, 50, 'drinks')
vodka = MenuItem("vodka", 50, 50, 'drinks')
cocktail = MenuItem("cocktail", 150, 300, 'drinks')
barbecue = MenuItem("barbecue", 250, 300, 'food')
potatoes = MenuItem("potatoes", 50, 300, 'food')
pizza = MenuItem("pizza", 300, 600, 'food')
sushi = MenuItem("sushi", 250, 300, 'food')
dessert = MenuItem("dessert", 120, 150, 'food')
lemonade = MenuItem("lemonade ", 70, 300, 'drinks')


my_restaurant = Restaurant()
my_restaurant.hire_employees()

for item in [borsch, soup, seafood_salad, cutlet, chop, coffee, whiskey, vodka,
             cocktail, barbecue, potatoes, pizza, sushi, dessert, lemonade]:
    my_restaurant.menu.add_menu_item(item, item.type_food)


def handle_order(order):
    """
    Handle the order.
    """
    for item_order in order:
        if item.type_food == 'food':
            my_restaurant.chef.take_order(item_order)
            my_restaurant.chef.cook()
        else:
            my_restaurant.barmen.take_order(item_order)
            my_restaurant.barmen.cook()


def main():
    """
    Entry point of restaurant.
    """

    print("Restaurant guests========================")
    customer_1 = Customer("Ivan")
    customer_1.make_reservation(my_restaurant)
    customer_1.come_to_restaurant()
    while my_restaurant.guests:

        guest = my_restaurant.guests.popleft()
        base_order = guest.request_order(my_restaurant.menu, BaseOrder())
        my_restaurant.waiter.create_order(base_order, guest.table_number)
        my_restaurant.waiter.give_order_to_chef(guest.table_number)
        my_restaurant.waiter.give_order_to_barmen(guest.table_number)
        handle_order(base_order.customer_order)
        my_restaurant.waiter.set_status_order(guest.table_number)
        my_restaurant.chef.give_order_to_waiter(base_order.customer_order[0])
        my_restaurant.barmen.give_order_to_waiter(base_order.customer_order[1])
        my_restaurant.waiter.give_order_to_customer(guest.table_number)
        guest.ask_bill()
        guest.pay_for_bill()
        my_restaurant.update_busy_tables(guest.table_number, is_come_customer=False)
        my_restaurant.update_free_tables(is_come_customer=False)

    print('Online guests======================================================')
    customer_2 = Customer("Ivan1")
    customer_2.call_to_restaurant(my_restaurant)
    while my_restaurant.online_guests:
        guest = my_restaurant.online_guests.popleft()
        online_order = guest.request_order(my_restaurant.menu,
                                           OnlineOrder(time_delivery=datetime.now(),
                                                       address='Sumska 69'))
        my_restaurant.online_operator.create_order(online_order, guest.order.address)
        my_restaurant.online_operator.give_order_to_chef(online_order.address)
        my_restaurant.online_operator.give_order_to_barmen(online_order.address)
        handle_order(online_order.customer_order)
        my_restaurant.online_operator.set_status_order(guest.order.address)
        my_restaurant.online_operator.give_order_to_customer(online_order.address)
        guest.ask_bill()
        guest.pay_for_bill()


if __name__ == '__main__':
    main()
