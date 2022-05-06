// For loop
for (let i = 1; i <= 10; i++) {
  console.log(`[FOR] Current iteration is ${i}`);
}

// While
let i = 1;
while (i <= 10) {
  console.log(`[WHILE] Current iteration is ${i}`);
  i = i + 1; // or i++, i+=1, ++i
}

// Do while
i = 1; // not adding let because i is already declared
do {
  console.log(`[DO-WHILE] Current iteration is ${i}`);
  i = i + 1;
} while (i <= 10);
