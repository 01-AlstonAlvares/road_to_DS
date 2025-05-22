#Read file and print names starting with 'A'
names = ["Alice", "Bob", "Charlie", "Arjun", "Anita"]

with open("example.txt", "w") as file:
    for name in names:
        if name.startswith("A"):
            print(name)
