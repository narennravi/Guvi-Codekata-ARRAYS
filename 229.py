# Question:-

'''
You have been given stock prices for next N days. Find out: max profit in buying and selling 1 share Condition: Share must be sold any day after buying date. Given a number N followed by N integers print the maximum profit.
For example: Share price in thousands 5 1 4 6 7 8 4 3 7 9
Max benefit 9 – 1 = 8 thousand

Input Size : N <= 100000


Sample Testcase :
INPUT
10
5 1 4 6 7 8 4 3 7 9

OUTPUT
8
'''



# Solution:-
N = int(input())
prices = list(map(int, input().split()))

min_price = float('inf')
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

print(max_profit)
