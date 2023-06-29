# Question:-
'''
Given a number 'N' print the sum of each digit to the power of number of digits in given input.

Example :
Input => 1234
=> ( 1 ^ 4 ) + ( 2 ^ 4 ) + ( 3 ^ 4 ) + ( 4 ^ 4 )
=> 1 + 16 + 81 + 256
Output => 354
N <=100000000000

Sample Testcase :
INPUT
1234

OUTPUT
354
'''



# Solution:-
def sum_of_digit_powers(n):
    digits = list(str(n))
    num_digits = len(digits)
    digit_sum = 0
    for digit in digits:
        digit_sum += int(digit) ** num_digits
    return digit_sum

# Get the input
n = int(input())

# Calculate the sum of digit powers
result = sum_of_digit_powers(n)

# Print the result
print(result)
