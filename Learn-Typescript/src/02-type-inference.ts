//Type Inference is the ability of the TypeScript compiler to automatically infer types based on the values assigned to variables, function return types, and other expressions. This allows developers to write less verbose code while still benefiting from type safety.

//Example 1: Variable Type Inference
let message = "Hello, TypeScript!"; // TypeScript infers the type as 'string'
let count = 42; // TypeScript infers the type as 'number'
let isActive = true; // TypeScript infers the type as 'boolean'

//Example 2: Function Return Type Inference
function add(a: number, b: number) {
  return a + b; // TypeScript infers the return type as 'number'
}

//Example 3: Array Type Inference
let numbers = [1, 2, 3]; // TypeScript infers the type as 'number[]'
let names = ["Alice", "Bob", "Charlie"]; // TypeScript infers the type as 'string[]'

//Example 4: Object Type Inference
let person = {
  name: "Alice",
  age: 30,
}; // TypeScript infers the type as { name: string; age: number }

//Example 5: Contextual Typing
window.addEventListener("click", (event) => {
  console.log(event.clientX, event.clientY); // TypeScript infers the type of 'event' as 'MouseEvent'
});

//Example 6: Type Inference with Generics
function identity<T>(arg: T): T {
  return arg; // TypeScript infers the type of 'T' based on the argument passed
}
let output = identity("Hello"); // TypeScript infers the type of 'output' as 'string'
let output2 = identity(42); // TypeScript infers the type of 'output2' as 'number'
