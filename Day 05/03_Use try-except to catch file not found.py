#Use try-except to catch file not found

try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found.")
