# Question:-
'''
Varsha is a Machine learning scientist. She wants to apply a few ML algorithms on the dataset to do some research and for that,
she wants to merge two given arrays and sort them in ascending order. You are an intern working under Varsha and she has asked for your help for the same.
Given 2 arrays arr1[] and arr2[], find the union of both the arrays sorted in ascending order.  Note: Union of two arrays must have distinct elements.

 
Input Description:
Size of arr1[] followed by elements of arr1. Size of arr2[] followed by elements of arr2.

Output Description:
Union of arr1 and arr2 sorted in ascending order.


Sample Input :
2 
87 78
3
1 2 3

Sample Output :
1 2 3 78 87
'''

# Solution:-
sa1 = int(input())
a1 = [int(x) for x in input().split()]
sa2 = int(input())
a2 = [int(x) for x in input().split()]
for i in a2:
    if i not in a1:
        a1.append(i)
a1.sort()
print(*a1)
