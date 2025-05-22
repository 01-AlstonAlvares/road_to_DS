#Use itertools to print combinations of ['A', 'B', 'C'], 2 at a time
import itertools

items = ['A', 'B', 'C']
combinations = itertools.combinations(items, 2)

for pair in combinations:
    print(pair)