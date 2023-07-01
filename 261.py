# Question:-
'''
Given an array of N elements, sort the elements of the array based on frequency.
If two numbers have the same frequency,then the smaller number comes first (eg) if the elements are 1,1,3,1,2,3,4 then the output is 2,4,3,3,1,1,1
 
Input Description:
Size of the array followed by the number of elements

Output Description:
Array elements sorted based on increasing frequency


Sample Input :
5
8 8 1 1 3

Sample Output :
3 1 1 8 8
'''


# Solution:-
n = int(input())
l = [int(x) for x in input().split()]
l.sort()

maxfreq = l.count(l[0])

for i in l:
    if maxfreq < l.count(i):
        maxfreq = l.count(i)
#print(maxfreq)
a = []

for i in range(maxfreq+1):
    for j in l:
        if l.count(j) == i:
            a.append(j)
print(*a)
