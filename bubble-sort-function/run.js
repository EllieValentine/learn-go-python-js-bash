// Define a bubble sort function
function bubbleSort(array) {
  // The outer loop will traverse all the elements of the list
  for (let i = 0; i < array.length; i++) {
    // The inner loop will compare elements
    for (let j = 0; j < array.length - i - 1; j++) {
      // Compare two elements
      // > sorts the array in ascending order
      // < sorts the array in descending order
      if (array[j] > array[j + 1]) {
        // If TRUE then swap the elements
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }

  console.log("Sorted array");
  console.log(array);
}

// Unsorted array
let numbers = [5, 3, -7, 0, 6, 2, 8, -4, 1];
console.log("Unsorted array");
console.log(numbers);

// Calling the function
bubbleSort(numbers);
