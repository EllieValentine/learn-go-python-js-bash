# Define a bubble sort function
function bubbleSort ()
{
    # Get the array parameter
    array=("$@")
    # Find an array length
    len=${#array[@]}
    
    # The outer loop will traverse all the elements of the list
    for ((i = 0; i<$len; i++)) do

        # The inner loop will compare elements
        for ((j = 0; j<$len-i-1; j++)) do

            # Compare two elements 
            # > sorts the array in ascending order
            # < sorts the array in descending order
            if [ ${array[j]} -gt ${array[$((j+1))]} ]
            then
                # If TRUE then swap the elements
                temp=${array[j]}
                array[$j]=${array[$((j+1))]}
                array[$((j+1))]=$temp
            fi
        done
    done

echo "Sorted array"
echo ${array[@]}

} 

# Unsorted array
numbers=(5 3 -7 0 6 2 8 -4 1)

echo "Unsorted array"
echo ${numbers[@]}

# Calling the function
bubbleSort "${numbers[@]}"

