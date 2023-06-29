# Question:-
'''
Given an array arr[] and a number K where K is smaller than the size of array, the task is to find the Kth smallest element in the given array.
It is given that all array elements are NOT distinct.


Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= arr[i] <= 105
1 <= K <= N


Input Description:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case consists of three lines. First line of each test case contains an integer N denoting size of the array. Second line contains N space separated integer denoting elements of the array. Third line of the test case contains an integer K.

Output Description:
Corresponding to each test case, print the desired output in a new line.


Sample Input :
2
6
7 10 4 3 3 4 
3
5
7 10 4 15 15
4

Sample Output :
7
15
'''


# Solution:-
n = int(input())
for i in range(n):
    n = int(input())
    l = {int(x) for x in input().split()}
    l = list(l)
    k = int(input())
    l.sort()
    print(l[k-1])
