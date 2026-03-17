function add(a: number, b: number): number {
  return a + b;
}

let sum: number = add(5, 10);
console.log("Sum:", sum);

function greet(name: string): string {
  return `Hello, ${name}!`;
}

let greeting: string = greet("Alice");
console.log(greeting);

function logMessage(message: string): void {
  console.log("Log:", message);
}

logMessage("This is a log message.");

function throwError(message: string): never {
  throw new Error(message);
}

//optional parameters
// What is an optional parameter? An optional parameter is a parameter that may or may not be provided when calling a function. It is denoted by a question mark (?) after the parameter name in the function definition.
// When it is used? Optional parameters are used when you want to allow a function to be called with fewer arguments than it defines,
// and you want to provide flexibility in how the function can be used.
function multiply(a: number, b?: number): number {
  if (b === undefined) {
    return a * a; // If b is not provided, multiply a by itself
  }
  return a * b;
}

console.log(multiply(5)); // Output: 25
console.log(multiply(5, 10)); // Output: 50

//default parameters
// What is a default parameter? A default parameter is a parameter that has a default value assigned to it.
// When it is used? Default parameters are used when you want to allow a function to be called with fewer arguments than it defines,
// and you want to provide a default value for the missing arguments.
function power(base: number, exponent: number = 2): number {
  return Math.pow(base, exponent);
}

console.log(power(5)); // Output: 25 (5 raised to the power of 2)
console.log(power(5, 3)); // Output: 125 (5 raised to the power of 3)

// Rest parameters
// What is a rest parameter?
// A rest parameter is a way to represent an indefinite number of arguments as an array in a function.
// It allows you to pass multiple arguments to a function without having to specify each one individually.
// When it is used?
// Rest parameters are used when you want to create a function that can accept a variable number of arguments.
// This is particularly useful for functions that perform operations on lists of items, such as summing numbers or concatenating strings.
function sumAll(...numbers: number[]): number {
  return numbers.reduce((acc, curr) => acc + curr, 0);
}

console.log(sumAll(1, 2, 3)); // Output: 6
console.log(sumAll(4, 5)); // Output: 9

// Arrow functions
// What is an arrow function? An arrow function is a concise way to write functions in TypeScript (and JavaScript).
// It uses the "fat arrow" syntax (=>) and does not have its own "this" context, making it particularly useful for callbacks and functional programming.
const subtract = (a: number, b: number): number => {
  return a - b;
};

console.log("Difference:", subtract(10, 5));

// Function Types
// A function type is a way to describe the type of a function, including its parameters and return type.
// When it is used?
// Function types are used when you want to define a variable that can hold a function,
// or when you want to specify the type of a function parameter or return value.
type Operation = (x: number, y: number) => number;

const divide: Operation = (a, b) => {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
};

console.log("Quotient:", divide(10, 2));

// Uncommenting the line below will throw an error
// throwError("This is an error!");
