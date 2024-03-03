x = input("Enter an arithmetic operator: ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

def sum(a, b):
    print("Sum of a and b is:", a + b)

def subtraction(a, b):
    print("Subtraction of a and b is:", a - b)

def multiply(a, b):
    print("Multiplication of a and b is:", a * b)

def division(a, b):
    if b != 0:
        print("Division of a and b is:", a / b)
    else:
        print("Error: Division by zero")

if x == '+':
    sum(a, b)
elif x == '-':
    subtraction(a, b)
elif x == '*':
    multiply(a, b)
elif x == '/':
    division(a, b)
else:
    print("X is not an arithmetic operator")
