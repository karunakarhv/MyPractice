def checkParaenthesis(s):
    stack = []
    opening = set('([{')
    closing = set(')]}')
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in opening:
            print(f"Encountered opening parenthesis: {char}")
            print(f"Stack before appending: {stack}")
            stack.append(char)
            print(f"Stack after appending: {stack}")
        elif char in closing:
            print(f"Encountered closing parenthesis: {char}")
            print(f"Stack before popping: {stack}")
            if not stack or stack[-1] != mapping[char]:
                return 0
            stack.pop()
    return 1 if not stack else 0
# Example usage:
s = "({[]})"
print(checkParaenthesis(s))  # Output: 1 (valid parentheses)
s = "({[})"
print(checkParaenthesis(s))  # Output: 0 (invalid parentheses)
s = "((()))"
print(checkParaenthesis(s))  # Output: 1 (valid parentheses)
s = "(()"
print(checkParaenthesis(s))  # Output: 0 (invalid parentheses)