# Question:-
'''
Ria is a 5 year old girl. Her mother wants to teach her how to sort words in the same order that they appear in a dictionary.
She decides to write a program to sort a given set of strings based on their alphabetical order. Help Ria’s mother to complete the program.

 
Input Description:
A set of N strings

Output Description:
Alphabetically sorted set of strings


Sample Input :
3
InfinityWar EndGame Avengers

Sample Output :
Avengers EndGame InfinityWar
'''



# Solution:-
no=int(input())
a=input().split()
l=[]
a.sort()
for i in a:
  l.append(i)
print(*l)
