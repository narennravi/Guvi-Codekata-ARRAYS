# Question:-
'''
For 2 arrays A1 and A2 , sort A1 in such a way that the relative order among the elements will be the same as those in A2.
For the elements not present in A2, append them at last to A1, in SORTED ORDER.

Note: Number of elements in A2[] are smaller than or equal to the number of elements in A1[]. A2[] has all distinct elements.

Constraints:
1 ≤ N,M  ≤ 106
1 ≤ A1[], A2[] <= 106


Input Description:
First line of input contains length of arrays N and M and next two line contains elements of A1 and A2 respectively.

Output Description:
Print the sorted array.


Sample Input :
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3

Sample Output :
2 2 1 1 8 8 3 5 6 7 9
'''


# Solution:-
n, m = map(int, input().split())
l = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
f = []
for i in a:
    for j in range(l.count(i)):
        f.append(i)
g = []
for i in l:
    if i not in a:
        g.append(i)
g.sort()
f.extend(g)
print(*f)
