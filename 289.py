# Question:-
'''
Given 2 numbers N,Q and an array of N integers, followed by Q queries each consisting of L,R. Find the GCD of numbers in [L,R]. If there is only one number in the given range, then print the number itself.
Input Size : 1<=N<=1000


Example:
INPUT
5 2
1 2 3 4 5
1 2
4 5

OUTPUT
1
1
'''



# Solution:-
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
N, Q = map(int, input().split())
numbers = list(map(int, input().split()))

for _ in range(Q):
    L, R = map(int, input().split())
    if L == R:
        print(numbers[L-1])
    else:
        current_gcd = numbers[L-1]
        for i in range(L, R):
            current_gcd = gcd(current_gcd, numbers[i])
        print(current_gcd)
