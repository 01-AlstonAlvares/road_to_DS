#Create a base class Vehicle and a subclass Bike that overrides a method.
class Vehicle:
    def describe(self):
        print("This is a vehicle")

class Bike(Vehicle):
    def describe(self):
        print("This is a bike")

v = Vehicle()
v.describe()

b = Bike()
b.describe()