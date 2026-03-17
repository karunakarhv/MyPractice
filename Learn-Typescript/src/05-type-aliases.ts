// Type Aliases in TypeScript
// What is a type alias? A type alias is a way to create a new name for a type in TypeScript.
// It allows you to define a custom type that can be used throughout your codebase, making it easier to read and maintain.
// When is it used? Type aliases are used when you want to give a more descriptive name to a type, especially
// when the type is complex or used frequently. They can also be used to create union types, intersection types, and to simplify function signatures.

// Example 1: Basic Type Alias
type UserID = number;
type UserName = string;

let userId: UserID = 12345;
let userName: UserName = "Alice";

// Example 2: Union Type Alias
type Status = "active" | "inactive" | "pending";

function updateStatus(status: Status) {
  console.log(`Status updated to: ${status}`);
}

updateStatus("active"); // Valid
// updateStatus("archived"); // Error: Argument of type '"archived"' is not assignable to parameter of type 'Status'.

// Example 3: Intersection Type Alias
type Person = {
  name: string;
  age: number;
};

type Employee = {
  employeeId: number;
};

type EmployeePerson = Person & Employee;

const employee1: EmployeePerson = {
  name: "Bob",
  age: 30,
  employeeId: 101,
};

// Example 4: Function Type Alias
type MathOperation = (a: number, b: number) => number;

const add: MathOperation = (a, b) => a + b;
const multiply: MathOperation = (a, b) => a * b;

console.log(add(5, 3)); // Output: 8
console.log(multiply(5, 3)); // Output: 15

//Type alias vs Interface
// Type aliases and interfaces in TypeScript are both used to define custom types, but they have some differences in terms of capabilities and use cases.
// Type Alias: A type alias can represent any type, including primitives, unions, intersections, tuples, and more.
// It is more flexible and can be used to create complex types. However, it cannot be extended or implemented like an interface.
// Interface: An interface is primarily used to define the shape of an object. It can only represent object types
// and cannot represent primitives or other complex types. Interfaces can be extended and implemented, making them ideal for defining contracts in object-oriented programming.
// In general, if you need to define a simple type or a union/intersection type, a type alias is a good choice.
// If you need to define the structure of an object or want to take advantage of inheritance and implementation features, an interface is more suitable.

// Example of Type Alias vs Interface
type Point = {
  x: number;
  y: number;
};

interface IPoint {
  x: number;
  y: number;
}

const pointA: Point = { x: 10, y: 20 };
const pointB: IPoint = { x: 30, y: 40 };

console.log(pointA); // Output: { x: 10, y: 20 }
console.log(pointB); // Output: { x: 30, y: 40 }

// Extending Interfaces
interface Shape {
  color: string;
}

interface Circle extends Shape {
  radius: number;
}

const circle1: Circle = {
  color: "red",
  radius: 5,
};

console.log(circle1); // Output: { color: 'red', radius: 5 }
