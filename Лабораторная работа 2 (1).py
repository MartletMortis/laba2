def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multipy(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("U can't divide by zero wtf bro...")


operator = input("Enter the operator: ")
while operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '0':
    print("U can't type stuff like this...")
    operator = input("Enter the operator: ")

if operator == '0':
    print("The end?..")
    exit()

try:
    x = int(input("First number: "))
except ValueError:
    print("Well... no.")
    exit()

try:
    y = int(input("Second number: "))
except ValueError:
    print("Well.. no.")
    exit()

if operator == '+':
    print(plus(x, y))

elif operator == '-':
    print(minus(x, y))

elif operator == '*':
    print(multipy(x, y))

elif operator == '/':
    print(divide(x, y))