# Question:-
'''
You are given an array of N elements. Your task is to sort a subarray denoted by the index values i1 and i2 in descending order.
Note: Index values start at 0. The sorting must be completed in O(i2-i1+1)log(i2-i1+1)
 

Input Description:
Size of array followed by elements of the array. The third line contains the start and end indices of the subarray( i1 and i2)

Output Description:
A partially sorted array


Sample Input :
6
34 9 2 10 56
1 3

Sample Output :
34 2 9 10 56
'''


# Solution:-
n = int(input())
l = [int(x) for x in input().split()]
(i1, i2) = map(int, input().split())
a = []

for i in range(i1, i2+1):
    a.append(l.pop(i1))
a.sort()
for i in a:
    l.insert(i1, i)
print(*l)
