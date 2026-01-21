'''Question 1: Write a Python program to check if a string is a palindrome.'''


'''
Write Python code to reverse a string.
'''

string = 'parth'
reversed = string[::-1]


rev_string = ''
for i in range(len(string)-1, -1, -1):
    rev_string = rev_string+string[i]
    print(rev_string)
