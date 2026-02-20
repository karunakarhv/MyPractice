class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"
        self._protected_attribute = "I am protected"
        self.__private_attribute = "I am private"

    def public_method(self):
        print("I am a public method")

    def _protected_method(self):
        print("I am a protected method")

    def __private_method(self):
        print("I am a private method")

    def access_private(self):
        print(self.__private_attribute)
        self.__private_method()

obj = MyClass()

# Accessing public attributes and methods
print(obj.public_attribute)
obj.public_method()

# Accessing protected attributes and methods (not recommended)
print(obj._protected_attribute)
obj._protected_method()

# Accessing private attributes and methods (not recommended)
print(obj._MyClass__private_attribute)
obj._MyClass__private_method()

# Accessing private attributes and methods through a public method
obj.access_private()