#Use filter() to get all numbers > 10 from a list.
num = [x for x in range(31)]


even = list(filter(lambda x: x > 10 , num))
print(even)
