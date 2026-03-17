# Need a code to print a star pattern like this:
# *
# * **
# * ** ***
# * ** *** ****
def print_star_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print('* ' * j, end=' ')
        print()  # Move to the next line after each row
# Example usage:
n = 4
print_star_pattern(n)