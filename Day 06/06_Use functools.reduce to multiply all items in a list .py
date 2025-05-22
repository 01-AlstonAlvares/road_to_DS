#Use functools.reduce to multiply all items in a list

from functools import reduce


numbers = [2,3,4,5]
product = reduce(lambda x,y: x*y, numbers)

print("Product of all numbers", product)