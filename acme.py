#!/usr/bin/env python

from numpy import random

class Product:

    def __init__(self, name, price=10, weight=20, flammability=.5, identifier=None):
        if identifier is None:
            identifier = random.randint(1000000, 9999999)
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = int(identifier)
