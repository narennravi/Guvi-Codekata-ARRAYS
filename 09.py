# Question:-
'''
You are given with an circular array .Your task is calculate the difference between two consecutive number.
And if difference is greater than ‘k’, print 1 else print 0

Input Description:
You are given two numbers ‘n’, ’m’. Next line contains n space separated integers.

Output Description:
Print 1 if the difference is greater than ‘m’.


Sample Input :
5 15
50 65 85 98 35

Sample Output :
0 1 0 1 0
'''


# Solution:-
n,k=(int(no) for no in input().split())
arr=list(map(int,input().split()))
a=[]
for i in range (n-1):
  if abs(arr[i]-arr[i+1])>k:
    a.append('1')
  else:
    a.append('0')

if abs(arr[-1]-arr[0])>k:
  a.append('1')
else:
  a.append('0')
print(*a)
