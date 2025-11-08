# Simple calculator program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

x= float(input("enter the number"))
r=x%2
if r==1:
    print("odd")
    if x>10:
        print("greater than num")
else:
    print("even")

print("venky") 


# Main program
print("Simple Calculator")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))

