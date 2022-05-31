
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

# int()
# Convert a string into an integer
print(int(3.5))

# len()
# Return the length of an object
sample = ['January', 'February', 'March', 'April', 'May']
print(len(sample))

# max()
# Return the item with the highest value. For words, return the highest value, ordered alphabetically
sample = ['January', 'February', 'March', 'April']
print(max(sample))
sample = (5,2,6,1)
print (max(sample))

# min()
# Opposite to Max
sample = ['January', 'February', 'March', 'April']
print(min(sample))
sample = (5,2,6,1)
print (min(sample))

# next()
# Return the next item in an iterator
sample = iter(['January', 'February', 'March', 'April'])
print(next(sample)) # Returns January
print(next(sample)) # Returns February

# open(file, mode, options)
# open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# Open file accoirding to 'mode'
# Mode options 'r' - read, 'w' - overwrite, 'x' - create, 'a' - append, '+' - update (read and write)
# Example
# file = open("samplefile.txt", "r")
# print(file.read())

# print()
# Print object
print('Hello')

# reversed()
# Reverse the sequence
sample = ['January', 'February', 'March', 'April', 'May']
rsample = reversed(sample)
for i in rsample:
  print(i)

# round(number, ndigits)
# Return number rounded to ndigits precision
pi = 3.14159265359
print (round(pi, 4))

# set() 
# Creates a set object. The items in a set are unordered, so it will appear in random order
sample = set(('January', 'February', 'March', 'April', 'May'))
print(sample)

#sorted()
# Return a sorted list from the items in iterable 
sample = ('January', 'February', 'March', 'April', 'May')
print(sorted(sample))

# str()
# Return a string version of object
print(str(12547))

# sum()
# Return a sum of all items
sample = (2, 4, 6, 8, 10)
print(sum(sample))

# type()
# Return the type of an object
sample = set(('January', 'February', 'March', 'April', 'May'))
print(type(sample)) # Returns <class 'set'>