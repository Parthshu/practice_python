# Generate the Fibonacci series using Python.
# 0 1 1 2 3 5 8 13 21

# Takes a number n (how many terms to generate),
# 	•	Then prints or returns the first n Fibonacci numbers.


start = 0
n = 10
l = [0, 1]


for i in range(2, n):
    l.append(l[i-1]+l[i-2])
    print(l)
