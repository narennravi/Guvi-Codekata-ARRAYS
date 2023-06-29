# Question:-
'''
The prison warden at Central jail is given a tip-off that a prison inmate is planning an escape.
The warden suspects a particular prisoner of planning an escape and wants to find out if he/she is present in his/her cell.
The layout of the prison is modelled in a matrix with every cell of the matrix representing a prison cell.
The matrix is filled with the prisoner ids at the corresponding cells. Find out whether the person the warden suspects is present in the prison or not.
 

Input Description:
First line contains the dimensions of the prison matrix, followed by the ids of prisoners as elements of the matrix. The third line contains the id to be searched.

Output Description:
(yes/no) whether the given element is present in the matrix or not.


Sample Input :
2 5
2 3 0 7 1 5 3 4 1 8
11

Sample Output :
no
'''


# Solution:-
n,a = input().split()
m = list(map(int,input().split()))
x = int(input())
result = None
for i in m:
    if i == x:
        result = "yes"
        break
    else:
        result = "no"
print(result)
