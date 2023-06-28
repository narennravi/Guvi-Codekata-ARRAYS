# Question:-
'''
Mr.Stark wants to order the employee ids, which are recorded in a 2D matrix, in ascending order. 
He wants to do it so as to allot a new id to a person who joins as a fresher. 
You are the CTO of the Stark industries and you are asked by Mr.Stark to sort the data.
 

Input Description:
Dimensions of the matrix m and n, followed by the elements of the matrix.

Output Description:
Matrix sorted in ascending order


Sample Input :
3 3
87 21 34
89 32 78
12 23 45

Sample Output :
12 21 23
32 34 45
78 87 89
'''



# Solution:-
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

flattened = [element for row in matrix for element in row]

sorted_list = sorted(flattened)

sorted_matrix = [sorted_list[i:i+n] for i in range(0, len(sorted_list), n)]

for row in sorted_matrix:
    print(' '.join(map(str, row)))
