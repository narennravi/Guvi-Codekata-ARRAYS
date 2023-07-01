# Question:-
'''
Given a number N followed by an unsorted array of N numbers and a number K, find if there exists a pair of elements in the array whose difference is K. Return count of such pairs.
Example k=4 and a[]={7,6,23,19,10,11,9,3,15}
Output should be : 6
Pairs can be:
7,11
7,3
6,10
19,23
15,19
15,11
Input Size : N <= 100000


Sample Testcase :
INPUT
6 4
8 12 16 4 0 20

OUTPUT
5
'''


# Solution:-
def count_pairs_with_difference(arr, k):
    num_set = set(arr)
    count = 0

    for num in arr:
        if num + k in num_set:
            count += 1
        if num - k in num_set:
            count += 1

    return count // 2  # divide by 2 to avoid counting duplicates


# Read input
n, k = map(int, input().split())
array = list(map(int, input().split()))

# Count pairs with the given difference
pair_count = count_pairs_with_difference(array, k)

# Print the result
print(pair_count)
