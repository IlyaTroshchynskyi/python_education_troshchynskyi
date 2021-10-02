# -*- coding: utf-8 -*-
"""calc
   Implements the Transport
"""

import time


class Transport:
    """
    Implement basic behavior for transport
    """
    def __init__(self, brand, type_transport, max_speed, number):
        self.brand = brand
        self.type = type_transport
        self.max_speed = max_speed
        self._number = number
        self.speed = 0

    def start_drive(self):
        """
        Increases speed at start
        """
        self.speed += 2
        print(f"The transport with number: {self._number} and speed {self.speed} start drive")

    def drive(self, speed):
        """
        Increases speed during the driving
        """
        self.speed += speed
        print(f"The transport with number: {self._number} and speed {self.speed} is driving")

    def stop(self):
        """
        Stop the transport
        """
        self.speed = 0
        print(f"The transport with number: {self._number} is stopped")


class Car(Transport):
    """
    Implement class Car
    """
    def __init__(self, brand, type_transport, max_speed, number):
        Transport.__init__(self, brand, type_transport, max_speed, number)

    def start_drive(self):
        self.speed += 5
        print(f"The transport with number: {self._number} and speed {self.speed} start drive")

    def drive(self, speed):
        self.speed += speed * 2
        print(f"The transport with number: {self._number} and speed {self.speed} is driving")

    def stop(self):
        print("Car is stoping during one second")
        super().stop()


class Tram(Transport):
    """
    Implement class Tram
    """
    def __init__(self, brand, type_transport, max_speed, number):
        Transport.__init__(self, brand, type_transport, max_speed, number)

    def start_drive(self):
        self.speed += 1
        print(f"The transport with number: {self._number} and speed {self.speed} start drive")

    def drive(self, speed):
        self.speed += speed / 2
        print(f"The transport with number: {self._number} and speed {self.speed} is driving")

    def stop(self):
        print('Tram is stopping and switch of electricity')
        super().stop()


class Truck(Transport):
    """
    Implement class Truck
    """
    def __init__(self, brand, type_transport, max_speed, number):
        Transport.__init__(self, brand, type_transport, max_speed, number)

    def start_drive(self):
        self.speed += 1
        print(f"The transport with number: {self._number} and speed {self.speed} start drive")
        print("ZHHHHHHH")

    def drive(self, speed):
        self.speed += speed / 1.5
        print(f"The transport with number: {self._number} and speed {self.speed} is driving")

    def stop(self):
        print('stoping too slow')
        super().stop()


class Motorbike(Transport):
    """
    Implement class Motorbike
    """
    def __init__(self, brand, type_transport, max_speed, number):
        Transport.__init__(self, brand, type_transport, max_speed, number)

    def start_drive(self):
        self.speed += 10
        print(f"The transport with number: {self._number} and speed {self.speed} start drive")
        print("RRRRR")

    def drive(self, speed):
        self.speed += speed / 70
        print(f"The transport with number: {self._number} and speed {self.speed} is driving")

    def stop(self):
        print('With high speed to stop quite difficult')
        time.sleep(1)
        super().stop()


car = Car("BMV", "passenger", 250, 'AX131313')
truck = Truck("DUF", "cargo", 140, 'AX131314')
tram = Tram("tram", "public", 70, 'AX131315')
motorbike = Motorbike("Yava", "passenger", 330, 'AX131316')

car.start_drive()
car.drive(50)
car.stop()

truck.start_drive()
truck.drive(100)
truck.stop()

tram.start_drive()
tram.drive(100)
tram.stop()

motorbike.start_drive()
motorbike.drive(100)
motorbike.stop()
