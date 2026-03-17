//Primitives
let age: number = 25;
let name: string = "Adithya";
let isStudent: boolean = true;
let nullValue: null = null;
let undefinedValue: undefined = undefined;

// Arrays
let numbers: number[] = [1, 2, 3, 4, 5];
let names: string[] = ["Alice", "Bob", "Charlie"];

// Tuples
let person: [string, number] = ["Alice", 30];

// Enums
enum Color {
  Red,
  Green,
  Blue,
}
let favoriteColor: Color = Color.Green;

// Any
let randomValue: any = "Hello";
randomValue = 42; // No error

// Unknown
let unknownValue: unknown = "Hello";
// let strLength: number = unknownValue.length; // Error: Object is of type 'unknown'.
if (typeof unknownValue === "string") {
  let strLength: number = unknownValue.length; // No error
}

// Void
function logMessage(message: string): void {
  console.log(message);
}
logMessage("Hello, TypeScript!");

// Null and Undefined
let nullableValue: string | null = "Hello";
nullableValue = null; // No error

let optionalValue: string | undefined = "Hello";
optionalValue = undefined; // No error

// Never
function throwError(message: string): never {
  throw new Error(message);
}
// throwError("This is an error!"); // Uncommenting this will throw an error
