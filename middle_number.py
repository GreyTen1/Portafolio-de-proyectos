import sys

print("Welcome to my programm!")
print("You'll have the middle number")
print("The numbers have to be different from each other")

def check(number):
    while float(number) is False:
        number = input("Please, enter a valid number: ")
    return float(number)

def result(number):
    print(f"the middle number is {number}.")

def executing():
    n1 = input("Enter the first number: ")
    n1 = check(n1)
    n2 = input("Enter the second number: ")
    n2 = check(n2)
    while n2 == n1:
        n2 = input(f"The number has to be different from {n1}: ")
    n3 = input("Enter the third number: ")
    n3 = check(n3)
    while n3 == n1 or n3 == n2:
        n3 = input(f"The number has to be different from {n1} or {n2}: ")

    if (n1 < n2 < n3) or (n1 > n2 > n3):
        result(n2)
    elif (n1 < n3 < n2) or (n1 > n3 > n2):
        result(n3)
    elif (n2 < n1 < n3) or (n2 > n1 > n3):
        result(n1)

def EXIT():
    salida = input("Do you want to do another operation? (y or n) ")
    if salida == "y":
        return
    elif salida == "n":
        print("Good Bye!")
        sys.exit()
    else:
        EXIT()

while True:
    executing()
    EXIT()