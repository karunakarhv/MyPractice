class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"MyClass instance with value: {self.value}"
    
    def __add__(self, other):
        return MyClass(self.value + other.value)
    
    def __enter__(self):
        print("Entering context...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context...")

obj1 = MyClass(5)
obj2 = MyClass(10)

print(obj1)  # Calls __str__
result = obj1 + obj2  # Calls __add__

with obj1:  # Calls __enter__ and __exit__
    print("Inside context block")