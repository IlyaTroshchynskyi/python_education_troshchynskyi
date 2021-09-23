# -*- coding: utf-8 -*-
"""calc
   Implements the Transport and Engine
"""

import time
from abc import ABC, abstractmethod


class TransportInterface(ABC):
    """
    Interface of Transport
    """

    @abstractmethod
    def start_drive(self):
        """
        Interface start driving
        """
        ...

    @abstractmethod
    def drive(self, speed):
        """
        Interface driving
        """
        ...

    @abstractmethod
    def stop(self):
        """
        Interface stop driving
        """
        ...


class Transport(TransportInterface):
    """
    Implement basic behavior for transport
    """
    num_instances = 0

    def __init__(self, brand, type_transport, max_speed, number, length):
        self.brand = brand
        self.type = type_transport
        self.max_speed = max_speed
        self._number = number
        self.speed = 0
        self.length = length
        Transport.num_instances += 1

    def __le__(self, other):
        if self.max_speed == other.max_speed:
            print("Transport is equal")
        elif self.max_speed > other.max_speed:
            print(f"Transport with number {self._number} more powerful")
        elif self.max_speed < other.max_speed:
            print(f"Transport with number {self._number} more powerful. "
                  f"Speed both Transport {self.max_speed}--{other.max_speed}")
        else:
            raise ValueError("Something went wrong")

    def __ge__(self, other):
        self.__le__(other)

    def __getitem__(self, index):
        return self.brand[index]

    def __len__(self):
        return self.length

    def __getattr__(self, name):
        if name == 'wheels' and isinstance(self, Car):
            return 4
        if name == 'wheels' and isinstance(self, Truck):
            return 10
        if name == 'wheels' and isinstance(self, Motorbike):
            return 2
        if name == 'wheels' and isinstance(self, Tram):
            return 8
        raise AttributeError

    @classmethod
    def create_transport(cls, brand, type_transport, max_speed, number, length):
        """
        Create new transport
        """
        return cls(brand, type_transport, max_speed, number, length)

    @property
    def get_number_car(self):
        """
        Show the number of car
        """
        return self._number

    @staticmethod
    def print_num_instances():
        """
        Show count of created transports
        """
        print("Number of transport instances: %s" % (Transport.num_instances))

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
    def __init__(self, brand, type_transport, max_speed, number, length):
        Transport.__init__(self, brand, type_transport, max_speed, number, length)

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
    def __init__(self, brand, type_transport, max_speed, number, length):
        Transport.__init__(self, brand, type_transport, max_speed, number, length)

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
    def __init__(self, brand, type_transport, max_speed, number, length):
        Transport.__init__(self, brand, type_transport, max_speed, number, length)

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
    def __init__(self, brand, type_transport, max_speed, number, length):
        Transport.__init__(self, brand, type_transport, max_speed, number, length)

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


car = Car("BMV", "passenger", 250, 'AX131313', 3)
car1 = Car("BMV", "passenger", 260, 'AX131334', 3)
truck = Truck("DUF", "cargo", 140, 'AX131314', 9)
tram = Tram("tram", "public", 70, 'AX131315', 7)
motorbike = Motorbike("Yava", "passenger", 330, 'AX131316', 1.5)

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

print(car >= car1)
print(car <= car1)
print(car[:2])
Transport.print_num_instances()
print(car.get_number_car)
print(len(car))
print(car.wheels)
print(truck.wheels)
car3 = Car.create_transport("DUF1", "cargo", 145, 'AX131319', 8)
