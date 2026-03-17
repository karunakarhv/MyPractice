class Person {
  private name: string;
  protected age: number;
  private email: string;

  constructor(name: string, age: number, email: string) {
    this.name = name;
    this.age = age;
    this.email = email;
  }

  public greet(): string {
    return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
  }

  // Getters and Setters
  public getName(): string {
    return this.name;
  }

  public setName(name: string): void {
    this.name = name;
  }

  public getAge(): number {
    return this.age;
  }

  public setAge(age: number): void {
    this.age = age;
  }

  public getEmail(): string {
    return this.email;
  }

  public setEmail(email: string): void {
    this.email = email;
  }
}

class Student extends Person {
  private studentId: number;

  constructor(name: string, age: number, email: string, studentId: number) {
    super(name, age, email);
    this.studentId = studentId;
  }

  public getStudentId(): number {
    return this.studentId;
  }

  public setStudentId(studentId: number): void {
    this.studentId = studentId;
  }
}

const student1 = new Student("Alice", 20, "alice@example.com", 1234);
console.log(student1.greet()); // Output: Hello, my name is Alice and I am 20 years old.
console.log("Student ID:", student1.getStudentId()); // Output: Student ID: 1234
