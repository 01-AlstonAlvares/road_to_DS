#Write 5 names to a file, one per line

names = ["Alice", "Bob", "Charlie", "Arjun", "Anita"]

with open("example.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
