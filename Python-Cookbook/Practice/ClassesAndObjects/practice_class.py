class MyPracticeClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")
        
class MyPracticeChildClass(MyPracticeClass):
    def say_goodbye(self):
        print(f"Goodbye, {self.name}!")

# Example usage
if __name__ == "__main__":
    my_object = MyPracticeClass("Alice")
    print(my_object)
    my_object.say_hello()

    my_child_object = MyPracticeChildClass("Bob")
    print(my_child_object)
    my_child_object.say_hello()
    my_child_object.say_goodbye()