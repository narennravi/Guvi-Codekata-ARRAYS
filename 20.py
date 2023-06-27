# Question:-
'''
Ramesh is a student and wants to find out if there is any other student in his class who has got the same marks as his, in maths. Help him to find out.
 
Input Description:
First line contains the number of students in the class followed by Ramesh’s mark. Second line contains the marks of all students in the class.

Output Description:
Index of student who got mark same as Ramesh’s mark. If no such mark exists, return -1.


Sample Input :
2 10
1 2

Sample Output :
-1
'''


# Solution:-
n,mark = input().split()
n = int(n)
mark = int(mark)
m = list(map(int,input().split()))
answer = None
for i in m:
    if i == mark:
        answer = m.index(i)
        break
    else:
        answer = "-1"

print(answer)
