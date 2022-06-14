let array = ["zero", "one", "two", "three", "four", "five"];

console.log("* Print the array");
console.log(array);

console.log("* Copy the array");
let arrayCopy = array.slice();
console.log(arrayCopy);

console.log("* Returns the length (number of elements) of the array");
console.log(array.length);

console.log("* Add elements to the array");
array.push("six");
console.log(array);

console.log("* Remove an element from the end of the array");
array.pop();
console.log(array);

console.log("* Remove an element from the beginning of the array");
array.shift();
console.log(array);

console.log("* Add elements to the beginning of an array");
array.unshift("new", "new", "new");
console.log(array);

console.log("* Another way to clone the array");
array = [...arrayCopy];
console.log(array);

console.log("* Access an element using index");
console.log(array[3]);

console.log("* Check if a Value is an Array");
console.log(Array.isArray(["zero", "one", "two"]));

console.log("* Returns the array in reverse order");
console.log(array.reverse());

console.log("* Returns the array after sorting");
console.log(array.sort());

console.log("* Fill the array with a value");
array.fill("new");
console.log(array);

array = arrayCopy.slice();
console.log(
  "* Fill the array with a value from index 3 to index 5 (excluding 5)"
);
array.fill("new", 3, 5);
console.log(array);

array = arrayCopy.slice();
console.log("* Make a string from the array");
console.log(array.toString());

console.log(
  "* Another way to make a string from the array (separator is optional)"
);
console.log(array.join("; "));
