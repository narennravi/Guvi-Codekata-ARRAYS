# Question:-
'''
Sensex has never been steady and stock values have been rising and falling in the past.
Ram is a stock broker and on analysing the trend of change in sensex points,
he decides that there was a period when the points was at its all time high and investing during that period would have earned him a huge profit in trade.
Ram immediately regrets not having done any trade in that particular period. Find out which period in time was Ram referring to.

Constraints:
3 ≤ N ≤ 106
 

Input Description:
The size of array N, the number of periods Ram has assessed. The values of the array are the values of the sensex points.

Output Description:
Period in which the points was at its max value. The array index is the period value.


Sample Input :
9
1 15 25 45 42 21 17 12 11

Sample Output :
3
'''


# Solution:-
n = int(input())
lst = list(map(int,input().split()))
value = max(lst)
print(lst.index(value))
