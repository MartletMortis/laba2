def divide(x, y):
    try:
        div = x / y
        return div
    except ZeroDivisionError:
        print("U can't divide by zero")
        return
    finally:
        print("This kinda stuff just made smth")


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

print(divide(x, y))