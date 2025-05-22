#Create a Student class with name, roll, and a method to display info.

class Student:
     def __init__(self, name, roll):
          self.name = name
          self.roll = roll

     def display(self):
          print(f"Students name is {self.name} and roll no is {self.roll}")

S1 = Student("Alston", 1)
S1.display()