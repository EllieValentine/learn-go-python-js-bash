
# Python does not have built-in support for Arrays, but Python Lists can be used instead.

array = ["zero", "one", "two", "three", "four", "five"]

print(array)

# add to an array
array.append("six")

# another way to print an array
print(' '.join(array)) # add comma if needed, like ', '

# modify the value of the last item:
array[6] = "last"

# print all elements one by one
for i in array:
  print(i)

# delete the element by its index
array.pop(6)

# delete the element by its value
array.remove("five")

# add an element at the specified position
array.insert(3, 'extra')

# sort the array
array.sort()

# reverse the order
array.reverse()