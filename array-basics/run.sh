#!/bin/bash

array=(zero one two three four five)

printf '\nprint an array\n'
echo ${array[@]}

# add to an array
array[6]=six 

printf '\nanother way to print an array\n'
echo ${array[*]}

printf '\nprint all elements one by one\n'
for i in "${array[@]}"; do echo "$i"; done

printf '\nprint all elements starting from the third one\n'
echo ${array[@]:2} 

printf '\ndisplay elements in a range\n'
echo ${array[@]:1:4} 

printf '\nlength of seventh element\n' 
echo ${#array[6]} 

printf '\nnumber of elements\n'
echo ${#array[@]} 

printf '\nreplacing substring \n'
echo ${array[@]//o/O}