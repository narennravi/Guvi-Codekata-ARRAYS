# Question:-
'''
Given a number N followed by an array of N integers, replace every element with the greatest element on the right side(to that element) in the array. Replace last element with 0 as there no element on the right side of it.
eg. if the array is {6, 7, 4, 3, 5, 2}, output {7, 5, 5, 5, 2, 0}.
Input Size : N <= 100000

Sample Testcase :
INPUT
6
6 7 4 3 5 2

OUTPUT
7 5 5 5 2 0
'''


# Solution:-
def replace_with_greatest(N, array):
    max_right = 0

    for i in range(N-1, -1, -1):
        current = array[i]
        array[i] = max_right
        max_right = max(max_right, current)

    array[N-1] = 0

    return array


# Example usage
N = int(input())
array = list(map(int, input().split()))

result = replace_with_greatest(N, array)
print(' '.join(map(str, result)))
