package main

// Imports package that contains the Println function.
import "fmt"

// Define a bubble sort function
func bubbleSort(array[] int) []int {
	
	// The outer loop will traverse all the elements of the list
	for i:=0; i < len(array)-1; i++ {
		
		// The inner loop will compare elements
		for j:=0; j < len(array)-i-1; j++ {

			// Compare two elements 
      		// > sorts the array in ascending order
     		// < sorts the array in descending order
      		if (array[j] > array[j+1]){
				  
				  // If TRUE then swap the elements
				  var temp = array[j]
				  array[j] = array[j+1]
				  array[j+1] = temp
			  }
		}

	
	}
  return array
}

func main() {
	// Unsorted array
	numbers:= []int{5, 3, -7, 0, 6, 2, 8, -4, 1};
	fmt.Println("Unsorted array")
	fmt.Println(numbers)
	
	// Calling the function
	fmt.Println("Sorted array")
	fmt.Println(bubbleSort(numbers))
}