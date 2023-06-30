# Question:-
'''
You are given N integer arrays, find if the same array occurs more than once. Print YES if it does, NO otherwise.
Two arrays A and B are same only if they are of equal size, say M, and for all 0 <= i <= M-1, A[i] = B[i].


Input Description:
The first line contains a single integer N, denoting the number of arrays. From the second line, 2*N lines follow. The (2i - 1)th line contains an integer M denoting the number of integers in the array. The 2i th line contains M space separated integers denoting the elements of the array.

Output Description:
Print a single line YES or NO


Sample Input :
3
5
1 8 3 1 2
1
9
1
9

Sample Output :
YES
'''


# Solution:-
N = int(input())

# Set to store unique arrays
unique_arrays = set()

# Iterate N times
for _ in range(N):
    M = int(input())  # Number of integers in the array
    array = tuple(map(int, input().split()))  # Array elements as a tuple

    # Check if the array already exists in unique_arrays set
    if array in unique_arrays:
        print("YES")
        exit()

    # Add the array to unique_arrays set
    unique_arrays.add(array)

# If the loop completes without printing "YES", print "NO"
print("NO")
