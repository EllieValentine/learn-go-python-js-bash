package main

// Imports package that contains the Println function.
import "fmt"

func main() {
	// Arrays
	// In Go the size of an array cannot be modified after it has been defined

	fmt.Println("** Arrays")
	fmt.Println("* New pre-defined array")
	//  Array Creation. The number of elements can be declared as [9], or [...], or []
	var arr = []int{7, 8, 3, -6, 0, 21, -40, 32, 1}
	fmt.Println(arr)

	// Declaration of an empty array (size must be determined as [number])
	fmt.Println("* New empty array")
	var fruits [7]string
	fmt.Println(fruits)

	// Add an element to the array to a specific index
	fmt.Println("* Add to the array")
	fruits[0] = "apple"
	fruits[1] = "pear"
	fruits[2] = "pineapple"
	fruits[3] = "mango"
	fruits[4] = "peach"
	fmt.Println(fruits)

	// Length of the array. Returns a pre-defined length
	// Note: cap() function will not work on arrays because the length and capacity of an array are always the same
	// len(arrayName)
	fmt.Println("* Length of the array")
	fmt.Println(len(fruits))

	// Print a specific range of elements.
	//array[1 : (1 + 3)] start from 1 and pick 3 elements
	fmt.Println("* Print elements 1,2,3")
	fmt.Println(fruits[1:4])
	//array[: (3)] start from the beginning and pick 3 elements
	fmt.Println("* Print elements 0,1,2")
	fmt.Println(fruits[:4])
	//array[1 : ] start from the beginning and pick all elements
	fmt.Println("* Print all elements")
	fmt.Println(fruits[1:])
	//array[3 : ] start from the 3 element and pick all elements to the end of the array
	fmt.Println("* Print all elements starting from the 3 element")
	fmt.Println(fruits[3:])

	// Copy the array to another array
	fmt.Println("* Copy the array to another array")
	var numbers = arr
	fmt.Println(numbers)

	// Slices
	// In Go a Slice is an ordered sequence of elements. The size of a slise can be changed at any time
	fmt.Println("** Slices")
	// len(arrayName)

	//  New pre-defined slice
	fmt.Println("* New pre-defined slice")
	var berries = []string{"cranberry", "blueberry", "strawberry"}
	fmt.Println(berries)

	// Print
	fmt.Println("* Another way to pring the slice")
	fmt.Printf("%q\n", berries)

	// Declaration of an empty slice. ([]string, 0) means no elements. ([]string, 3) will add 3 empty elements
	fmt.Println("* New empty slice")
	var vegetables = make([]string, 0)
	fmt.Println(vegetables)

	// Append multiple values to the slice (doesn't work with arrays)
	fmt.Println("* Append multiple values to the slice")
	vegetables = append(vegetables, "pumpkin", "avocado", "potato")
	fmt.Println(vegetables)

	// Converting from an Array to a Slice
	fmt.Println("* Converting from an Array to a Slice")
	slicedFruits := fruits[:]
	fmt.Printf("%q\n", slicedFruits)

	// Append 2 slices
	fmt.Println("* Append 2 slices")
	var freshProduce = append(vegetables, slicedFruits...)
	fmt.Printf("%q\n", freshProduce)

	// Delete element #5 from freshProduce
	fmt.Println("* Delete element #5 from freshProduce")
	freshProduce = append(freshProduce[:5], freshProduce[6:]...)
	fmt.Printf("%q\n", freshProduce)

	// Length of the slice.
	// len(arrayName)
	fmt.Println("* Length of the array")
	fmt.Println(len(freshProduce))

	// Capacity of the slice. How many elements the slice can hold
	// cap(arrayName)
	fmt.Println("* Length of the array")
	fmt.Println(cap(freshProduce))

}
