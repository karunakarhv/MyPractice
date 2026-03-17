// Object Type Annotations
// Whatis an Object Interface?
// An object interface in TypeScript is a way to define the structure of an object.
// It specifies the properties and their types that an object should have.
// This allows for better type safety and code readability when working with objects in TypeScript.
// When is it used?
// Object interfaces are used when you want to define the shape of an object,
// especially when you want to ensure that certain properties are present and have specific types.
// They are commonly used in function parameters, return types, and when defining complex data structures.
interface Person {
  name: string;
  age: number;
  isStudent: boolean;
}
function greet(person: Person): string {
  return `Hello, ${person.name}! You are ${person.age} years old and it is ${person.isStudent ? "great" : "not great"} that you are a student.`;
}
const person1: Person = {
  name: "Alice",
  age: 30,
  isStudent: true,
};
console.log(greet(person1)); // Output: Hello, Alice! You are 30 years old and it is great that you are a student.

// Optional Properties in Interfaces
// What is an optional property? An optional property is a property that may or may not be present in an object. It is denoted by a question mark (?) after the property name in the interface definition.
// When is it used? Optional properties are used when you want to allow an object to have certain properties that are not required.
// This is useful for cases where some information may be missing or not applicable, and you want to provide flexibility in the structure of the object.
interface Car {
  make: string;
  model: string;
  year: number;
  color?: string; // Optional property
}
const car1: Car = {
  make: "Toyota",
  model: "Camry",
  year: 2020,
};
const car2: Car = {
  make: "Honda",
  model: "Civic",
  year: 2019,
  color: "red",
};
console.log(car1); // Output: { make: 'Toyota', model: 'Camry', year: 2020 }
console.log(car2); // Output: { make: 'Honda', model: 'Civic', year: 2019, color: 'red' }

// Readonly Properties in Interfaces
// What is a readonly property? A readonly property is a property that can only be assigned a value once,
// either when it is declared or in the constructor of a class. Once a value is assigned to a readonly property, it cannot be changed.
// When is it used? Readonly properties are used when you want to ensure that a property cannot be modified after it has been initialized.
// This is particularly useful for properties that should remain constant throughout the lifecycle of an object,
// such as coordinates in a point or configuration settings.
interface Point {
  readonly x: number;
  readonly y: number;
}
const point1: Point = { x: 10, y: 20 };
// point1.x = 15; // Error: Cannot assign to 'x' because it is a read-only property.
console.log(point1); // Output: { x: 10, y: 20 }

// Index Signatures in Interfaces
// What is an index signature? An index signature is a way to define the type of properties that can be accessed
// using an index (like an array or object property access).
// When is it used? Index signatures are used when you want to define a type for objects that can
// have properties with dynamic names, such as when working with dictionaries or arrays.
interface StringArray {
  [index: number]: string;
}
const myArray: StringArray = ["Hello", "World"];
console.log(myArray[0]); // Output: Hello
console.log(myArray[1]); // Output: World
