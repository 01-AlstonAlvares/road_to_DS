#Create a list of all odd numbers from 1 to 30 using list comprehension.
odd = [x for x in range(31) if x % 2 != 0]
print(odd)