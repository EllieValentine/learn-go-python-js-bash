# Define a bubble sort function
def bubbleSort(array):
  # The outer loop will traverse all the elements of the list
  for i in range(0, len(array)):
    # The inner loop will compare elements
    for j in range(0, len(array) - i - 1):
      # Compare two elements 
      # > sorts the array in ascending order
      # < sorts the array in descending order
      if array[j] > array[j+1]:
        # If TRUE then swap elements
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

# Unsorted array
numbers = [5, 3, -7, 0, 6, 2, 8, -4, 1]

print('Unsorted array')
print(numbers)

# Calling the function
bubbleSort(numbers)

print('Sorted array')
print(numbers)

