#!/bin/sh

# Generate a random number from 1 to 10
machinePick=$((RANDOM%10+1))
guesses=0

echo "I picked a number from 1 to 10. Could you guess it in less than 6 turns?"


while (( $guesses < 6 )) ;
do
    read userPick

    # Check if the user input is a number
    check='^[0-9]+$'
    if ! [[ $userPick =~ $check ]]; then 
            echo "$userPick is not a number. Try again"

    # Check if the user input is in range from 1 to 10 
    elif (( $userPick < 1 )) || (( $userPick > 20 )) ; then 
            echo "$userPick is not in range from 1 to 10. Try again"

    else
            # Play game
            ((guesses++))
        
            if (( $userPick > $machinePick )) ; then
                echo "My number is lower. Try again"

            elif (( $userPick < $machinePick )) ; then
                echo "My number is bigger. Try again"

            else (( $userPick == $machinePick ))
                echo "Correct! My number is $machinePick, You guessed it in $guesses guess(es)"
                break
            fi
            
    fi
done

# No more guesses left
if (( $guesses == 6 )) ; then
    echo "No more guesses left! My number was $machinePick"
else 
:
fi