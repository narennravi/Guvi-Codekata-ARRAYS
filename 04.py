# Question:-
'''
You are given an array. Your task is to sort the array in given manner. Print the elements in increasing order of the frequency.
If frequency is same print smaller one first.

Input Description:
You are given a number ‘n’. Then in next line n space separated numbers.

Output Description:
Print the array as mentioned


Sample Input :
4
1 1 3 2

Sample Output :
2 3 1
'''


# Solution:-
n=int(input())
inp=list(map(int,input().split()))
#print(inp)
res=[]

for x in inp:
  if x not in res:
    res.append(x)

print(*res[::-1])
