# Question:-
'''
You are given an array a. Some element of this array ai is a local minimum iff it is strictly less than both of its neighbours (that is, ai < ai - 1 and ai < ai + 1).
Also the element can be called local maximum iff it is strictly greater than its neighbours (that is, ai > ai - 1 and ai > ai + 1).
Since a1 and an have only one neighbour each, they are neither local minima nor local maxima. 
An element is called a local extremum iff it is either local maximum or local minimum. Your task is to calculate the number of local extrema in the given array.


Input Size : N<=1000
Example:
INPUT
3
1 2 3

OUTPUT
2
'''



# Solution:-
N = int(input())
a = list(map(int, input().split()))

extrema_count = 0

for i in range(1, N-1):
    if (a[i] < a[i-1] and a[i] < a[i+1]) or (a[i] > a[i-1] and a[i] > a[i+1]):
        extrema_count += 1

print(extrema_count)
