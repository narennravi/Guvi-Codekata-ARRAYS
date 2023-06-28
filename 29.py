# Question:-
'''
You are a software engineer at an MNC. You are given the task of sorting the employees in your company based on their salary.
Perform the task so that the employees, including yourself, will get a bonus from the management.


CONSTRAINT:
0<=salary<=1000000

Input Description:
Number of employees followed by their name and salary

Output Description:
Sorted list of employee names


Sample Input :
3
Karthik 23000 rohan 81734 varshini 12343

Sample Output :
varshini
Karthik
Rohan
'''


# Solution:-
n = int(input())
s = str(input()).split()
a = {}
b = []
for i in range(0, n*2, 2):
    a[s[i+1]] = s[i]
    b.append(s[i+1])
b.sort()
for i in b:
    print(a[i])
