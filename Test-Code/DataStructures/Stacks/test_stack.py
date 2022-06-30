import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.myStack = Stack()

    def test_peek(self):
        self.myStack.push(1)
        self.myStack.push(2)
        self.myStack.push(3)
        self.assertEqual(self.myStack.peek(), 3)

    def test_sizeOfStack(self):
        self.myStack.push(1)
        self.myStack.push(2)
        self.myStack.push(3)
        self.assertEqual(self.myStack.sizeStack(), 3)

    def test_push(self):
        self.myStack.push(1)
        self.myStack.push(2)
        self.myStack.push(3)
        self.assertEqual(self.myStack.displayItems(), [1, 2, 3])

    def test_pop(self):
        self.myStack.push(1)
        self.myStack.push(2)
        self.myStack.push(3)
        self.myStack.pop()
        self.assertEqual(self.myStack.displayItems(), [1, 2])

    def test_isEmpty(self):
        self.myStack.push(1)
        self.myStack.push(2)
        self.myStack.push(3)
        self.myStack.pop()
        self.myStack.pop()
        self.myStack.pop()
        self.assertTrue(self.myStack.isEmpty())

    def test_reverse_number(self):
        # Does not work for float numbers
        number = 123456
        self.myStack.push(number)
        self.assertEqual(self.myStack.reverseNumber(), 654321)

    def test_reverse_string(self):
        # Does not work for float numbers
        testString = '123456 the word'
        self.myStack.push(testString)
        self.assertEqual(self.myStack.reverseString(), 'drow eht 654321')

    def test_balanced(self):
        for idx in ["[[[]]]", "[{}]", "(({}))"]:
            self.assertTrue(self.myStack.paraenthsisMatching(idx))

    def test_unbalanced(self):
        for idx in ["[[[]]", "[{}", "(({})"]:
            self.assertFalse(self.myStack.paraenthsisMatching(idx))

    def test_getMax(self):
        self.myStack.items = [4,3,2,-1.0]
        self.assertEqual(self.myStack.getMax(), 4)

if __name__ == "__main__":
    unittest.main()