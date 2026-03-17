def fibnoacci(n):
    if n <= 1:
        return n
    else:
        return fibnoacci(n-1) + fibnoacci(n-2)
    

# Example usage:
n = 7
print(f"The {n}th Fibonacci number is: {fibnoacci(n)}")
