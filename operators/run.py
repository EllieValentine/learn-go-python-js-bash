
x = 10

y = 3

# Arithmetic operators

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Division
print(x / y)

# Modulus. Returns the remainder of division
print(x % y)

# Exponentiation. Same as x = x * x * x * x 
print(x ** y)

# Floor division. Returns the rounded quotient. If one of the operands is negative, the result is rounded towards negative infinity.
print(x // 4)

# Comparison Operators

# Equal
print(x == y)
	
# Not equal
print(x != y)

# Greater than
print(x > y)

# Less than
print(x < y)

# Greater than or equal to
print(x >= y)

# Less than or equal to
print(x <= y)


# Logical Operators

# and  - True if both statements are true
print(x < 12 and  x > 7)

# or - True if one of the statements is true
print(x < 12 or x < 4)

# not - False if the result is true
print(not(x < 12 and  x > 7))


# Assignment Operators

# Assign
x = 3
print(x)

# Same as x = x + 2
x += 2
print(x)

# same as x = x - 2
x -= 2
print(x)

# Same as x = x * 2
x *= 2
print(x)

x = 7
# Same as x = x / 2
x /= 2
print(x)

# Modulus. Same as x = x % 2 . 
x %= 2
print(x)

x = -13
# Floor. x // y == math.floor(x/y). 
x //= 3
print(x)

x = 2
# Exponentiation. 
x **= 4
print(x)

x = 5
#  a "bitwise and". Ssame as x = x&2 . Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x &= 2
print(x)

x = 5
# a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
x |= 2
print(x)

# a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
x ^= 2
print(x)

#	Signed right shift. Returns x with the bits shifted to the right by y places (pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off).
x >>= 2
print(x)

# Zero fill left shift. Returns x with the bits shifted to the left by y places (pushing zeros in from the right and let the leftmost bits fall off)
x <<= 2
print(x)


# Other operators

# Returns True if both variables are the same object
print(x is y)

# Returns True if both variables are not the same object
print(x is not y)

z = ["car", "cat"]
c = ["dog"]
# Returns True if a sequence with the specified value is present in the object
print(c in z)

# Returns True if a sequence with the specified value is not present in the object
print(c not in z)

# AND	Sets each bit to 1 if both bits are 1
print(x & y)

# OR	Sets each bit to 1 if one of two bits is 1
print(x | y)

# XOR	Sets each bit to 1 if only one of two bits is 1
print(x ^ y)

# NOT	Inverts all the bits
print(~x)