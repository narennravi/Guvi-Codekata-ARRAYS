# Question:-
'''
You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.

Input Description:
First line contains a number ‘n’. Then next line contains n space separated numbers.

Output Description:
Print the difference of indices of largest and smallest array


Sample Input :
5
1 6 4 0 3

Sample Output :
-2
'''



# Solution:-
a = int(input())
arr = list(map(int,input().split()))
print(arr.index(max(arr))-arr.index(min(arr)))
