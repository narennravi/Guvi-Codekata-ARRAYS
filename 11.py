# Question:-
'''
You are given with two arrays. Your task is to merge the array such that first array is in ascending order and second one in descending order.

Input Description:
First line contains two integer ‘n’ and ‘m’. ‘n’ denotes length of array 1 and ‘m’ of array 2.Next line contains n space separated numbers and third line contains ‘m’ space separated numbers

Output Description:
Print a single array in desired order


Sample Input :
3 3
23 15 16
357 65 10

Sample Output :
15 16 23 357 65 10
'''



# Solution:-
(n, m)= map(int, input().split())
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l1.sort()
l2.sort(reverse = True)
l1.extend(l2)
print(*l1)
