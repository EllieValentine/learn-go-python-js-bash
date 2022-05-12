
# Python does not have built-in support for Arrays, but Python Lists can be used instead.

text = 'poetry is a form of literature'

# capitalize the first character.
print(text.capitalize())

# converts string into upper case.
print(text.upper())

# converts string into lower case.
print(text.lower())

# converts uppercase characters to lowercase and vice versa.
print(text.swapcase())

# all words start with uppercase characters.
print(text.title())

# check if all cased characters in the string are lowercase.
print(text.islower())

# check if all cased characters in the string are uppercase.
print(text.isupper())

# check if the string is a titlecased string.
print(text.istitle())

# check if all characters are alphanumeric (either alphabets or numbers). If whitespace found returns False.
print(text.isalnum())

# check if all characters are alphabetic.
print(text.isdigit())

# check if all characters are digits.
print(text.isalpha())

# check if all characters are whitespace characters.
print(text.isspace())

# add spaces to a string to make it 50 characters long, placing "text" in the middle.
print(text.center(50))

# returns a left-justified string of a given minimum width. 
print(text.ljust(50))

# number of occurrence of 'o'.
print(text.count('o'))

# find substring (returns the index of first occurrence). Returns -1 if not found.
print(text.find('is'))

# same as find but returns ValueError if substring is not found.
print(text.index('is'))

# replace each matching occurrence of substring with provided string.
print(text.replace('o', 'a'))

# breaks up a string at the specified separator, returns a list
print(text.split(' '))

list = ['a','b','c','d']
s = " - "

# join elements of text with space
print(' '.join(list))

# join elements of text with a separator from a variable
print(s.join(list))