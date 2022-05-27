# Simple calculator

# Collect user name
name = input("Enter your name: ")
print("Hello", name + "!")

# Collect first number
value1 = input("Enter first number: ")

# Collect second number
value2 = input("Enter second number: ")

# Collect operation symbol
operation = input("Select an operation from +, -, *, or / : ")

# Create expression
expression = value1 + " " + operation + " " + value2

# Check input
if operation not in "+-*/":
    print("Invalid input, try again")

else:
    # Use Python’s built-in function to evaluate expressions from a string-based input
    result = eval(expression) 
    print("%s = %s" % (expression, result))