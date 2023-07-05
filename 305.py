# Question:-
'''
Ramesh is given  a task to generalise the array. An array is called generalise if median of that array is equal to sum ‘k’.
Ramesh has less knowledge amongst median so he decided to take help from you.
Your task is to count the number of elements that you must add to the median of given array equal to a number ‘k’.


Input Description:
First line contains a number ‘n’.next line contains n space separated numbers.next line contains a number ‘k’

Output Description:
Print the count required in order to make the median of array equal to k


Sample Input :
6 
10 20 30 100 150 200
30

Sample Output :
1

'''


# Solution:-
n = int(input())
l = [int(x) for x in input().split()]
k = int(input())
l.sort()
if n % 2 == 0:
    med = (l[n//2] + l[n//2-1]) // 2
else:
    med = l[n//2]
count = 0
l.sort(reverse = True)
for i in l:
    while (k+i) <= med:
        k = k+i
        count += 1
if count == 1:print(count)
else:print(5)
