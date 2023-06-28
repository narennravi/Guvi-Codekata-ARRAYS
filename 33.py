# Question:-
'''
Ram and Sita are playing a game. There are N rounds for the game and the results are tabulated in a table of dimensions N x N.
A ‘0’ in the table implies that Ram has won the game, while a ‘1’ denotes that Sita has won the game.
You must compute the number of times Ram and Sita have won the game,individually.

Note : Elements in table can only be either 1 or 0.


Input Description:
First line contains two space separated integers M,N denoting the size of the 2d matrix . Then in the next lines are the space separated values of the matrix mat[ ] [ ] . Constraints: 1<=M,N<=50 ,0<=mat[][]<=1

Output Description:
The output will be the number of 0s and number of 1s, displayed separately.


Sample Input :
1 3
1 1 1

Sample Output :
RAM: 0
SITA: 3
'''



# Solution:-
(m, n) = map(int, input().split())
l = []

for i in range(m):
    a = [str(x) for x in input().split()]
    l.extend(a)
print("RAM:", l.count("0"))
print("SITA:", l.count("1"))
