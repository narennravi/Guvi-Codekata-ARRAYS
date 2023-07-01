# Question:-
'''
Jaspreet is a marketing manager and on inspecting the product ids of products documented as ‘sold’,
he finds out that the sales person has repeated a few of the product ids. He decides to warn the sales person who has repeated the same product id thrice.
Your task is to find out the number of triplets(ids occurring thrice) of product ids recorded.


Constraints:
1 <= N <= 100
1 <= A[] <= 1000

Input Description:
Number of product ids followed by the list of product ids

Output Description:
Number of triplets detected.


Sample Input :
10
2 1 1 3 1 8 7 2 2 6 

Sample Output :
2
'''


# Solution:-
n = int(input())
lst = list(map(int,input().split()))
triple = 0

l = list(set(lst))

for i in l:
    if lst.count(i) == 3:
        triple += 1
print(triple)
