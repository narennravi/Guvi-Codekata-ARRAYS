# Question:-
'''
In a cricket match the coach wanted to check the performance of batsmen o he decided strike rate as criteria.
He planned that the two batsmen whose strike rate difference minimum will be sent no. 3 and no.4 in next match.
Now your task is to help the coach in finding the two batsmen.


Input Description:
You are given an integer ’n’ denoting the size of array. Next line contains n space separated integers.

Output Description:
Print the strike rate of two batsmen in same order of their occurence


Sample Input :
6
138.3 156.5 156.6 160.2 198.3 146.2

Sample Output :
156.5 156.6
'''


# Solution:-
n = int(input())
strike_rates = list(map(float, input().split()))

min_diff = float('inf')
batsman1 = 0
batsman2 = 0

for i in range(n):
    for j in range(i+1, n):
        diff = abs(strike_rates[i] - strike_rates[j])
        if diff < min_diff:
            min_diff = diff
            batsman1 = strike_rates[i]
            batsman2 = strike_rates[j]

print(batsman1, batsman2)
