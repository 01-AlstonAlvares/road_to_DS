#Add a __str__ method to a class to print a friendly string when the object is printed.
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"Student Name: {self.name}, Roll No: {self.roll}"

s1 = Student("Alice", 101)
print(s1)