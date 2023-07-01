# Question:-
'''
Ram wants to be a leader. He is fascinated by any puzzle or news that has the word ‘leader’ in it. 
He comes across a puzzle about finding a leader amongst a list of numbers and is intrigued by the puzzle. 
As Ram is not good in either maths or logic, he is unable to solve the puzzle. Help Ram by finding out the leader among a given set of positive numbers.

Note: An element in an array is a leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader.


Constraints:
1 <= N <= 100
0 <= A[i] <= 100

Input Description:
The first line contains a single integer N denoting the size of array. The second line contains N space-separated integers denoting the elements of the array.

Output Description:
Print all the leaders.


Sample Input :
6
16 17 4 3 5 2

Sample Output :
17 5 2
'''


# Solution:-
n = int(input())
l = [int(x) for x in input().split()]
a = []

for i in range(n):
    flag = True
    for j in range(i, n):
        if l[i] < l[j]:
            flag = False
            break
    if flag:
        a.append(l[i])
print(*a)
