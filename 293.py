# Question:-
'''
Palash is fond of palindromic numbers.So he decided to give this knowledge to his younger brother.
Hence he decided to frame one question.To make him more clear he decided that he will tell his younger brother ‘suresh’ about this concept using problem.
The problem statement is as follows,You are given with array conatining digits 0-9 your task is to print the smallest palindromic number ’t’ but this number must be greater than the number obtained using digits.

Now your task is to help suresh to solve the this tricky question

 

Input Description:
You are given with size of array ‘n’. Next line contains n space separated integers

Output Description:
Print the smallest palindromic number.


Sample Input :
10
1 2 3 5 9 6 8 4 7 0

Sample Output :
1235995321
'''



# Solution:-
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def generate_smallest_palindrome(num):
    num += 1
    while not is_palindrome(num):
        num += 1
    return num

# Read the input
n = int(input())
array = list(map(int, input().split()))

# Convert the array to a number
given_number = int(''.join(map(str, array)))

# Generate the smallest palindromic number greater than the given number
result = generate_smallest_palindrome(given_number)

# Print the result
print(result)
