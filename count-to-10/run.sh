#!/bin/bash

# For loop
for ((i=1; i<=10; i++))
do
    echo "[FOR] Current iteration is $i"
done

# For ranges

for i in {1..10} # can be decreased and then increased {10..0..5}
do
    echo "[FOR ranges] Current iteration is $i"
done

# While
i=1
while [ $i -le 10 ]
do
    echo "[WHILE] Current iteration is $i"
    i=$(($i+1)) # or  ((i++)) or ((i+=1))
done

# Until
i=1
until [ $i -gt 10 ] 
do
echo "[UNTIL] Current iteration is $i"
i=$(($i+1))
done