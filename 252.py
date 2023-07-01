# Question:-
'''
Vishal is a competitive coder and he loves problems on sorting and searching. He is bored right now and decides to solve a sorting problem with a modification. 
He decides to sort the elements at the even indices of an array in ascending order and the elements at the odd indices in descending order.
Vishal goes outside his room after coding the solution, but his laptop crashes and he is unable to show it to his teacher.
Can you help Vishal by coding the solution to the problem?


Constraints:
0<=array[i]<=10000

Input Description:
Size of the array followed by the elements of the array

Output Description:
Sorted elements of the array


Sample Input :
10 
9 8 7 1 2 3 6 5 4 10

Sample Output :
2 10 4 8 6 5 7 3 9 1
'''


# Solution:-
n = int(input())
l = [int(x) for x in input().split()]
e = []
o = []

for i in range(n):
    if i % 2 == 0:
        e.append(l[i])
    else:
        o.append(l[i])


e.sort()
o.sort(reverse = True)
p = 0
q = 0
l = []

for i in range(n):
    if i%2==0:
        l.append(e[p])
        p+=1
    else:
        l.append(o[q])
        q+=1
print(*l)
