'''
 Write a Python program to find the factorial of a number.
'''


def find_factorial(n):
    if n in [0, 1]:
        return 1
    else:
        factorial = n*find_factorial(n-1)
        return factorial


print(find_factorial(10))
