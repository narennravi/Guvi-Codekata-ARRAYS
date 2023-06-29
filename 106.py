# Question:-
'''
Ram is a marketing manager at GUVI. He observes that for every two batches of products, one package is extra in one of the batches.
He realises that someone is stealing the package from the other batch. He decides to document the discovery so as to report to his superior.
Find out the package number of the package that gets stolen from one of the batches of products.
 

Constraints:
1<=T<=100
1<=N<=100
1<=Ai<=1000

 
Input Description:
The first line of input contains an integer T, denoting the no of test cases. Then T test cases follow. The first line of each test case contains an integer N, denoting the number of packages in Batch A. The second line of each test case contains N space separated values of number of items in each package of Batch A. The Third line of each test case contains N-1 space separated number of items in each package of Batch B.

Output Description:
Return the package number of the corresponding package stolen from Batch B. The array index denotes the package number.


Sample Input :
2
7
2 4 6 8 9 10 12
2 4 6 8 10 12
6
3 5 7 9 11 13
3 5 7 11 13

Sample Output :
4
3
'''


# Solution:-
m = int(input())
ans_lst = []
for _ in range(m):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in a:
        if i not in b:
            ans_lst.append(a.index(i))
for i in ans_lst:
    print(i)
