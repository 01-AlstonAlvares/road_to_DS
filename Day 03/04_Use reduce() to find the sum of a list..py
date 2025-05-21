#Use reduce() to find the sum of a list.

from functools import reduce

num = [x for x in range(12)]

product = reduce(lambda x, y: x+y,num)
print(product)