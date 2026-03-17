// Type assertions and Type Guards
// What is a Type Assertion? A type assertion is a way to tell the TypeScript compiler to treat a value as a specific type.
// It is used when you have more information about the type of a value than the compiler can infer on its own.
// Type assertions are denoted by the 'as' keyword or by using angle brackets (< >).
// When is it used? Type assertions are used when you want to override the inferred type of a value,
// especially when you know that a value has a more specific type than what the compiler can infer.
// They are commonly used when working with DOM elements, third-party libraries, or when you want to narrow down the type of a variable in certain situations.
let someValue: any = "This is a string";
let strLength: number = (someValue as string).length; // Using 'as' syntax
// let strLength: number = (<string>someValue).length; // Using angle bracket syntax (not recommended in JSX files)
console.log(strLength); // Output: 16

// Type Guards
// What is a Type Guard? A type guard is a runtime check that allows you to narrow down the type of a variable within a specific block of code.
// It is used to ensure that a variable is of a certain type before performing operations on it.
// Type guards can be implemented using the 'typeof' operator, 'instanceof' operator, or by creating custom type guard functions.
// When is it used? Type guards are used when you want to perform type-specific operations on a variable,
// and you need to ensure that the variable is of the expected type before doing so.
// They are particularly useful when working with union types, where a variable can be one of several types, and you need to handle each type differently.
function isString(value: any): value is string {
  return typeof value === "string";
}
let unknownValue: any = "Hello, TypeScript!";
if (isString(unknownValue)) {
  console.log(unknownValue.toUpperCase()); // Output: HELLO, TYPESCRIPT!
} else {
  console.log("The value is not a string.");
}
