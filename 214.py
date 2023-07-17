# Question:-
'''
Given a number N,print number of all possible valid expressions with N pairs of brackets(use this {}).
For example({{{}}}
{{}{}}
{{}}{}
{}{{}}
{}{}{})3 brackets has 5 pairs.
Input Size : 1 <= N <= 100000


Sample Testcases :
INPUT
2

OUTPUT
2
'''


# Solution:-
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

N = int(input())

factorial_2n = factorial(2*N)
factorial_n_plus_1 = factorial(N + 1)
factorial_n = factorial(N)

result = factorial_2n // (factorial_n_plus_1 * factorial_n)

print(result)
