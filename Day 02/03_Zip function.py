#Given two lists of equal length, print a formatted string like "Alice:85" using zip.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
#The zip() function lets you combine two (or more) lists element-wise.
    print(f"{name}, {score}")