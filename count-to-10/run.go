package main

// Imports package that contains the Println function.
import "fmt"

func main() {

	// For loop
	for i := 1; i <= 10; i++ {
		fmt.Println("[FOR] Current iteration is", i)
	}

	// While
	i := 1
	for i <= 10 {
		fmt.Println("[WHILE] Current iteration is", i)
		i++
	}
}
