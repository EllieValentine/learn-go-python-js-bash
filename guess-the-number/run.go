package main

// Imports packages that contains Println, time and Rand functions.
import (
	"fmt"
	"math/rand"
	"strconv"
	"time"
)

func main() {
	// Plain Rand function in GO always gives the same number.
	// Seed function is needed to initialize the default Source to get random numbers with Rand
	rand.Seed(time.Now().UnixNano())
	min := 1
	max := 10
	machinePick := rand.Intn(max-min+1) + min
	fmt.Println(machinePick)
	guesses := 0

	fmt.Println("I picked a number from 1 to 10. Could you guess it in less than 6 turns?")

	for guesses < 6 {
		var userPick int

		fmt.Scanln(&userPick)

		// Check if the user input is a number in range from 1 to 10

		if (userPick < 1) || (userPick > 10) {
			fmt.Println("Your guess is not a number in range from 1 to 10. Try again")

		} else {
			// Play game
			guesses++
			if userPick > machinePick {
				fmt.Println("My number is lower. Try again")
			} else if userPick < machinePick {
				fmt.Println("My number is bigger. Try again")
			} else {
				// Convert Int to string and combine the response
				response := "Correct! My number is " + strconv.Itoa(machinePick) + ", You guessed it in " + strconv.Itoa(guesses) + " guess(es)"
				fmt.Println(response)
				break
			}
		}
	}
	// No more guesses left

	if guesses == 6 {
		response := "No more guesses left! My number was " + strconv.Itoa(machinePick)
		fmt.Println(response)
	}

}
