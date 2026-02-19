class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f"Pair({self.first}, {self.second})"
    def __str__(self):
        return f"({self.first}, {self.second})"
# Example usage
if __name__ == "__main__":
    pair = Pair(1, 2)
    print(pair)  # This will call __str__
    print(repr(pair))  # This will call __repr__