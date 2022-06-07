let str =
  "The USA Today, the Wall Street Journal, the New York Times, are the leading newspapers";
let sub = "the";

console.log("* Returns the length of the string");
console.log(str.length);

console.log("* Replaces the first occurrence of t with @");
console.log(str.replace("t", "@"));

console.log("* Replaces all the occurrences of t with @");
let pattern = /t/g;
console.log(str.replace(pattern, "@"));

console.log("* Replaces all the occurrences of t with a, case-insensitive");
pattern = /t/gi;
console.log(str.replace(pattern, "@"));

console.log("* Converts string into upper case");
console.log(str.toUpperCase());

console.log("* Converts string into lower case");
console.log(str.toLowerCase());

console.log(
  "* Returns the index of first occurrence. Returns -1 if not found."
);
console.log(str.indexOf(sub));

console.log("* Returns the index of last occurrence. Returns -1 if not found.");
console.log(str.lastIndexOf("r"));

console.log("* Checks if a string contains a substring. True or False");
console.log(str.includes(sub));

console.log("* Returns a character at the specified index");
console.log(str.charAt(12));

console.log("* Checks if a string starts with a substring");
console.log(str.startsWith("The"));

console.log("* Checks if a string ends with a substring");
console.log(str.endsWith("e"));

console.log("* Checks if first n characters of a string ends with a substring");
console.log(str.endsWith("e", 15));

console.log("* Repeats a string n times");
console.log(str.repeat(2));

console.log("* Returns UTF-16 code for the character with a given index");
console.log(str.charCodeAt(12));

console.log("* Returns Unicode code for the character with a given index");
console.log(str.codePointAt(21));

console.log("* Returns a character for a given UTF-16 code");
console.log(String.fromCharCode(72, 69, 76, 76, 79));

console.log("* Returns a character for a given Unicode code");
console.log(String.fromCodePoint(65, 66, 67));

console.log("Matches a string against a regular expression");
pattern = /the\s[a-zA-Z]/gi;
console.log(str.match(pattern));

console.log(
  "* Appends a current string with a substring till n characters lenght is reached"
);
let text = "small text";
console.log(text.padEnd(20, "-"));

console.log(
  "* Adds a substring to the begining of a current string till n characters lenght is reached"
);
console.log(text.padStart(20, "-"));

console.log("Returns a substring starting from n to k");
console.log(str.substring(0, 13));

console.log("Divides the string");
console.log(str.split(" "));
