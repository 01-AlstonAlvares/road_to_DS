#check even or odd
a = int(input("Enter Number to check if it is even or odd: "))

def checker(a):
    if a%2 ==0:
        print(f"{a} is even number")
    else:
        print(f"{a} is odd number")

print(checker(a))