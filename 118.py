# Question:-
'''
Gunjan was going through the book of ‘hyp’ numbers. She is given task to find the nth hyp number.
Your task is to help gunjan. A hyp number is a number whose all digits are prime.


Input Description:
You are given a number ‘n’.

Output Description:
Print the ‘nth’ hyp number.


Sample Input :
3

Sample Output :
5
'''



# Solution:-
def is_prime_digit(num):
    prime_digits = {'2', '3', '5', '7'}
    for digit in str(num):
        if digit not in prime_digits:
            return False
    return True

def find_nth_hyp_number(n):
    hyp_count = 0
    num = 1

    while hyp_count < n:
        if is_prime_digit(num):
            hyp_count += 1
        num += 1

    return num - 1

if __name__ == "__main__":
    n = int(input())
    nth_hyp_number = find_nth_hyp_number(n)
    print(nth_hyp_number)
