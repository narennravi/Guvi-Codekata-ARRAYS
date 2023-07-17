# Question:-
'''
Your old mobile phone gets broken and so you want to purchase a new smartphone and decide to go through all the online websites to find out which dealer has the best offer for a particular model.
You document the prices of N dealers. Dealer ids start from 0 and go up to N.  Find out which dealer has the best price for you.


Constraints:
1 <= N <= 100
1 <= A[] <= 100000

 
Input Description:
Number of dealers followed by the price offered by each dealer

Output Description:
Dealer offering the best price.


Sample Input :
3
10000 11200 12030

Sample Output :
Dealer0
'''



# Solution:-
n = int(input())
m = list(map(int,input().split()))
low = min(m)

result = m.index(low)
print("Dealer"+str(result))
