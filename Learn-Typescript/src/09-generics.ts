// Generics in TypeScript allow you to create reusable components that can work with a variety of types rather than a single one. This is particularly useful for functions, classes, and interfaces that need to operate on different data types while maintaining type safety.

// Example of a generic function
function identity<T>(arg: T): T {
  return arg;
}

// Using the generic function with different types
let output1 = identity<string>("Hello, Generics!");
let output2 = identity<number>(42);

console.log(output1); // Output: Hello, Generics!
console.log(output2); // Output: 42

// Example of a generic class
class GenericNumber<T> {
  zeroValue: T;
  add: (x: T, y: T) => T;

  constructor(zeroValue: T, addFunction: (x: T, y: T) => T) {
    this.zeroValue = zeroValue;
    this.add = addFunction;
  }
}

// Using the generic class with numbers
let myGenericNumber = new GenericNumber<number>(0, (x, y) => x + y);
console.log(myGenericNumber.add(5, 10)); // Output: 15

// Using the generic class with strings
let myGenericString = new GenericNumber<string>("", (x, y) => x + y);
console.log(myGenericString.add("Hello, ", "Generics!")); // Output: Hello, Generics!

// Example of a generic interface
interface GenericIdentityFn<T> {
  (arg: T): T;
}

function identityFunction<T>(arg: T): T {
  return arg;
}

let myIdentity: GenericIdentityFn<number> = identityFunction;
console.log(myIdentity(100)); // Output: 100
// Example of a generic constraint
interface Lengthwise {
  length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
  console.log(arg.length); // Now we know it has a .length property, so no error
  return arg;
}

loggingIdentity("Hello, Generics!"); // Output: 17
loggingIdentity([1, 2, 3, 4]); // Output: 4
// loggingIdentity(42); // Error: Argument of type 'number' is not assignable to parameter of type 'Lengthwise'.
