# import random module
import random

# Generate a random number from 1 to 10
machinePick = random.randint(1, 10)
guesses = 0

print("I picked a number from 1 to 10. Could you guess it in less than 6 turns?")

while guesses < 6 :
    userPick = input('Your guess:') 
    
    # Check if the user input is a number, and it is in range from 1 to 10 
    if userPick.isdigit() != True :
        print("%s is not a number. Try again" %(userPick))
    elif int(userPick) < 0 or int(userPick) > 10:
        print("%s is not in range from 1 to 10. Try again" %(userPick))
    else:
        # Play game
        guesses += 1        
        if int(userPick) > machinePick :
            print("My number is lower. Try again")
        elif int(userPick) < machinePick :
            print("My number is bigger. Try again")
        else:
            print("Correct! My number is %s, You guessed it in %s guess(es)" %(machinePick,guesses))
            break

# No more guesses left
if guesses == 6 :
    print("No more guesses left! My number was %s" %(machinePick))