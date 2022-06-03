#!/bin/bash

x=10
y=3

# Arithmetic operators

printf "Arithmetic operators\n\n"

# Addition
echo Addition: $((x + y))

# Subtraction
echo Subtraction: $((x - y))

# Multiplication
echo Multiplication: $((x * y))

# Integer division. Returns the quotient of division
echo Integer division: $((x / y))

# Modulus. Returns the remainder of division
echo Modulus: $((x % y))

# Exponentiation. Same as x = x * x * x * x 
echo Exponentiation: $((x ** y))

# Comparison Operators

printf "\nComparison Operators\n\n"

# Equal (for string comparisons)
echo Equal string: $((x == y)) # or $((x = y))

# Equal (for numeric comparisons)
if [ $x -eq 3 ] ; then echo "Equal numeric: True" ; else echo "Equal numeric: False" ; fi
	
# Not equal (for string comparisons)
echo Not equal: $((x != y))

# Not equal (for numeric comparisons)
if [ $x -ne 3 ] ; then echo "Not equal numeric: True" ; else echo "Not equal numeric: False" ; fi

# Greater than (for string comparisons)
echo Greater than: $((x > y))

# Greater than  (for numeric comparisons)
if [ $x -gt 3 ] ; then echo "Greater than numeric: True" ; else echo "Greater than numeric: False" ; fi


# Less than (for string comparisons)
echo Less than: $((x < y))

# Less than (for numeric comparisons)
if [ $x -lt 3 ] ; then echo "Less than numeric: True" ; else echo "Less than numeric: False" ; fi

# Greater than or equal to (for string comparisons)
echo Greater than or equal to: $((x >= y))

# Greater than or equal to (for numeric comparisons)
if [ $x -ge 3 ] ; then echo "Greater than or equal to numeric: True" ; else echo "Greater than or equal to numeric: False" ; fi


# Less than or equal to (for string comparisons)
echo Less than or equal to: $((x <= y))

# Less than or equal to (for numeric comparisons)
if [ $x -le 3 ] ; then echo "Less than or equal to numeric: True" ; else echo "Less than or equal to numeric: False" ; fi


# Logical Operators

printf "\nLogical Operators\n\n"

# && - and. True if both statements are true
if (($x != $y)) && (($x > $y)) ; then echo "both statements are true: True" ; else echo "both statements are true: False" ; fi

# || - or. True if one of the statements is true
if (($x == $y)) || (($x < $y)) ; then echo "one of the statements is true: True" ; else echo "one of the statements is true: False" ; fi

# ! - not. False if the result is true
if !((($x == $y)) || (($x < $y))) ; then echo "False if the result is true: True" ; else echo "False if the result is true: False" ; fi


# Assign Operator

printf "\nAssign Operator\n\n"
x=3
echo Assign: $x

# Increment and Decrement Variables

printf "\nIncrement and Decrement Variables\n\n"

# Increment x+=1. Use x and then increment
x=3
echo Increment x+=1: $((x+=1))

# Increment x++. Use x and then increment
x=3
echo Increment x++: $((x++))

x=3
# Increment ++x. Increment and then use x 
echo Increment x++: $((++x))

# Decrement x--. Use x and then decrement
x=3
echo Decrement x-=1: $((x-=1))

# Decrement x--. Use x and then decrement
x=3
echo Decrement x--: $((x--))

x=3
# Decrement --x. Decrement and then use x 
echo Decrement x--: $((--x))