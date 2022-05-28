# Simple calculator (only to learn how input works in Python)
# Note: According to cyber security experts, it is the best practice to never use the eval() function in production environment, because the function will dynamically evaluate (execute) any expression. 


# Collect user name
name = input("Enter your name: ")

# Print a variable in text
print("Hello", name + "!")

# Collect first number
value1 = input("Enter first number: ")

# Collect operation symbol
operation = input("Select an operation from +, -, *, or / : ")

# Collect second number
value2 = input("Enter second number: ")

# Check input
if operation not in "+-*/" or value1.isdigit() != True or value2.isdigit() != True:
    print("Invalid input, try again")
else:
      # Create expression
      expression = value1 + " " + operation + " " + value2
      # Use Python’s built-in function to evaluate expressions from a string-based input
      result = eval(expression) 
      # Another way to print variables in text 
      print("%s = %s" % (expression, result))


# Simple calculator (Version 2. Only to learn how input works in Python)

print(name + ", let's try another way")

# Collect expression
expression = input("Enter the entire expression, example 6 + 7 - 3: ")

# Check if input is a math expression
for i in expression.split():
    if i in ['+','-','*','/'] or i.isdigit():
        ismath = True
    else:
        print("Invalid input, try again")
        ismath = False

# If it is a mathematical expression, calculate the result
if ismath == True:
    result = eval(expression) 
    print("%s = %s" % (expression, result))