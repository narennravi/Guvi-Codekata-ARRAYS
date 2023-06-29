# Question:-
'''
Prakash is bored and wants to spends his time. He starts rolling a die (having the face values as 1, 2, 3, 4, 8, 15, 7, 9) and observes that some of the values keep repeating.
Also while rolling n times, some face appear once only. Find the number on its face.


Constraints
0 <   N  <= 100
0 <= A[i] <= 100

 
Input Description:
The first line contains a positive integer N, denoting the size of the array. The second line contains N positive integers, denoting the face values that appeared when the die was rolled.

Output Description:
Print out the singly occurring number. print 0 if no numbers are repeating.


Sample Input :
5
1 1 2 5 5

Sample Output :
2
'''


# Solution:-
from collections import defaultdict
n = int(input())
m = list(map(int,input().split()))
d = defaultdict(int)
for i in m:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

count = 0
for i in d:
    if d[i] == 1:
        count = i

print(count)
