// Literal Types
// What is a literal type? A literal type is a type that represents a specific value or set of values.
// When it is used? Literal types are used when you want to specify that a variable or parameter can only have a specific value or set of values.
// This is particularly useful for creating more precise types and for enabling better type checking in your code.

type Direction = "up" | "down" | "left" | "right";

function move(direction: Direction) {
  console.log(`Moving ${direction}`);
}

move("up"); // Valid
move("down"); // Valid
move("left"); // Valid
move("right"); // Valid
// move("forward"); // Error: Argument of type '"forward"' is not assignable to parameter of type 'Direction'.

// Literal types can also be used with numbers and booleans
type Status = "active" | "inactive";
type ResponseCode = 200 | 400 | 404 | 500;

function handleResponse(status: Status, code: ResponseCode) {
  console.log(`Status: ${status}, Code: ${code}`);
}

handleResponse("active", 200); // Valid
handleResponse("inactive", 404); // Valid
// handleResponse("pending", 200); // Error: Argument of type '"pending"' is not assignable to parameter of type 'Status'.
// handleResponse("active", 201); // Error: Argument of type '201' is not assignable to parameter of type 'ResponseCode'.
