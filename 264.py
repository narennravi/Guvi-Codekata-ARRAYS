# Question:-
'''
You are given with an array. Your task is to print the right rotated array after k operations.
Time:O(n)
Extra Space: O(1)

 
Input Description:
First line contains two number ‘n’ and ‘k’.Next line contains n space separated numbers.

Output Description:
Print the array as mentioned.

Sample Input :
14 117
15 26 35 98 61 1230 75 96 63 21 1654 98654 320145 987

Sample Output :
21 1654 98654 320145 987 15 26 35 98 61 1230 75 96 63
'''


# Solution:-
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Calculate effective number of right rotations
k = k % n

# Reverse the entire array
arr = arr[::-1]

# Reverse the first k elements
arr[:k] = arr[:k][::-1]

# Reverse the remaining n-k elements
arr[k:] = arr[k:][::-1]

# Print the modified array
print(*arr)
