# Question:-
'''
You are given an array of non-negative integers representing height of walls at index i as Ai and the width of each block is 1.
Compute how much air can be encapsulated between the walls of chamber.


Input Description:
Each line contains an integer ‘N’ denoting the size of the array Next line contains N space separated numbers to be stored in array.

Output Description:
Output the total unit of Air encapsulated between the walls of chamber.


Sample Input :
3
7 4 9

Sample Output :
3
'''



# Solution:-
def maxAir(arr,n):
  res=0
  for i in range(1,n-1):
      left=arr[i]
      for j in range(i):
        left=max(left,arr[j])

      right=arr[i]
      for j in range(i+1,n):
        right=max(right,arr[j])

      res=res+(min(left,right)-arr[i])

  return res

N=int(input())
arr=list(map(int,input().split()))
n=len(arr)

print(maxAir(arr,n))
