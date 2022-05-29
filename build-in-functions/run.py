
# all(x)
# Logical And. Return true if all provided variables are true. 
# True in Python means non-zero, non-false and not NONE
sample = (0,2,2,1)
print (all (sample))

sample = (5,2,2,1)
print (all (sample))

# any(x)
# Logical Or. Return true if any of provided variables is true. 
sample = (0,2,0,0)
print (any (sample))

#bool()
# Return boolean value
sample=0
print(bool(sample))

# bin()
# Return the binary value for integer number
sample=255
print(bin(sample))

#chr()
# Return the Unicode symbol. Unicode code are defined in range from 0 through 1,114,111 
sample=1
print(chr(sample))

#ord()
# Inverse of chr(). Return the code value for Unicode symbols.
sample='$'
print(ord(sample))

# dir()
# Return full list of attributes and methods for a given object (object is optional). 
# If no parameter is passed, it returns a list of names in the current local scope. 
# Mainly used in debugging. 
print(dir())

# divmod(a, b)
# Return quotient and remainder
print (divmod(5, 2))
print (divmod(6, 2))

# enumerate(sample, start=0)
# Return an enumerate object. start=* is optional
sample = ['January', 'February', 'March', 'April', 'May']
result = list(enumerate(sample, start=1))
print(result)

# compile()
# Converts Python code in a string form into an object that cab be later executed or evaluated. Rarely used as it is a potential security hole.

# eval()
# Evaluate the argument. Rarely used as it is a potential security hole.

# exec()
# Dynamic execution of Python code. Rarely used as it is a potential security hole.

# format()
# Insert values into string's placeholder {}
print("Today's special is {}. Only ${}".format("Apple Pie",49.99))
# Same output 
print("Today's special is %s. Only $%s" % ("Apple Pie",49.99))

# hash()
# Return the hash value of the object
print(hash('Ellie'))

# hex()
# Return a lowercase hexadecimal string
print(hex(255))

# input()
# Reads user input and converts it to a string
name = input("Enter your name: ")










