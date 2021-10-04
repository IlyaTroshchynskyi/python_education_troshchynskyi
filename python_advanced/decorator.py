# -*- coding: utf-8 -*-
"""
   Implements singleton decorator
"""


def singleton(some_class):
    """
    Implement singleton decorator for classes
    """
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = some_class(*args, **kwargs)
        return instance
    return wrapper


@singleton
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


transport = Transport("BMV", "passenger", 250, 'AX131313')
transport_1 = Transport("BMV1", "passenger1", 200, 'AX131314')
print(transport)
print(transport_1)
