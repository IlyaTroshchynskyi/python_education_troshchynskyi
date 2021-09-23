# -*- coding: utf-8 -*-
"""calc
   Implements the Transport and Engine
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




class Engine:
    """
    Implement basic behavior for Engine
    """

    def start_engine(self):
        """
        Starts the engine
        """
        print(f'Turn the key and engine is working for transport {self}')

    def turn_of_engine(self):
        """
        Turn of the engine
        """
        print(f"Turn of the key and engine isn't working for transport {self}'")


class Car(Transport, Engine):
    """
    Implement class Car
    """
    def __init__(self, brand, type_transport, max_speed, number):
        Transport.__init__(self, brand, type_transport, max_speed, number)

    def start_drive(self):
        self.start_engine()
        self.speed += 5
        print(f"The transport with number: {self._number} and speed {self.speed} start drive")

    def drive(self, speed):
        self.speed += speed * 2
        print(f"The transport with number: {self._number} and speed {self.speed} is driving")

    def stop(self):
        print("Car is stoping during one second")
        super().stop()
        self.turn_of_engine()


class Tram(Transport, Engine):
    """
    Implement class Tram
    """
    def __init__(self, brand, type_transport, max_speed, number):
        Transport.__init__(self, brand, type_transport, max_speed, number)

    def start_drive(self):
        self.start_engine()
        self.speed += 1
        print(f"The transport with number: {self._number} and speed {self.speed} start drive")

    def drive(self, speed):
        self.speed += speed / 2
        print(f"The transport with number: {self._number} and speed {self.speed} is driving")

    def stop(self):
        print('Tram is stopping and switch of electricity')
        super().stop()
        self.turn_of_engine()


class Truck(Transport, Engine):
    """
    Implement class Truck
    """
    def __init__(self, brand, type_transport, max_speed, number):
        Transport.__init__(self, brand, type_transport, max_speed, number)

    def start_drive(self):
        self.start_engine()
        self.speed += 1
        print(f"The transport with number: {self._number} and speed {self.speed} start drive")
        print("ZHHHHHHH")

    def drive(self, speed):
        self.speed += speed / 1.5
        print(f"The transport with number: {self._number} and speed {self.speed} is driving")

    def stop(self):
        print('stoping too slow')
        super().stop()
        self.turn_of_engine()


class Motorbike(Transport, Engine):
    """
    Implement class Motorbike
    """
    def __init__(self, brand, type_transport, max_speed, number):
        Transport.__init__(self, brand, type_transport, max_speed, number)

    def start_drive(self):
        self.start_engine()
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
        self.turn_of_engine()

car = Car("BMV", "passenger", 250, 'AX131313')
car1 = Car("BMV", "passenger", 260, 'AX131334')
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
