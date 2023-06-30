# Question:-
'''
You are given with the marks of N students in CS, Maths and English. Sort the students based on marks in maths.
If 2 students have the same marks in maths, sort them based on marks in CS. If there is a tie, sort based on marks in English.
All the sorting must be done in descending order.
 

Input Description:
Number of students followed by student id,marks in CS, Maths and English

Output Description:
Sorted list of students


Sample Input :
3
A 34 89 98
B 98 87 98
C 87 67 98

Sample Output :
A 34 89 98
B 98 87 98
C 87 67 98
'''


# Solution:-
n = int(input())
l = [[str(x) for x in input().split()] for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(i):
        cs1, m1, e1 = int(l[j][1]), int(l[j][2]), int(l[j][3])
        cs2, m2, e2 = int(l[j+1][1]), int(l[j+1][2]), int(l[j+1][3])
        if m1 == m2:
            if cs1 == cs2:
                if e1 == e2: continue
                elif e1 < e2: (l[j], l[j+1]) = (l[j+1], l[j])
                else: continue
            elif cs1 < cs2: (l[j], l[j+1]) = (l[j+1], l[j])
            else: continue
        elif m1 < m2: (l[j], l[j+1]) = (l[j+1], l[j])
        else: continue
for i in l: print(*i)
