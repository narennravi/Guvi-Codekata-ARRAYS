# Question:-
'''
Arvind Kejriwal wants to implement a revised version of the ODD/EVEN scheme for vehicles in order to reduce pollution in Delhi.
The vehicle numbers are stored in an array and instead of allowing only either of odd/even numbered vehicles on the road,
he decides to allow the vehicles at odd/even INDICES of the array on a particular day. The day being Monday, only vehicles at even indices are allowed on the road.
He wants to analyse the number of vehicles that are allowed on the road on that particular day and hence decides to order the data in ascending order.
Sort the elements at the even indices of the array in ascending order and help make the IITan’s idea a success! Kejriwal would be happy if you could it in O(Nlog N) complexity,
where N is the number of elements that are to be sorted.
 

Input Description:
Size of the array followed by the elements of the array

Output Description:
Array with elements at the even indexes sorted in ascending order.


Sample Input :
6
12 44 23 16 1 62

Sample Output :
1 44 12 16 23 62
'''

# Solution:-
n = int(input())
l = [int(x) for x in input().split()]
e = []

for i in range(n):
    if i % 2 == 0: e.append(l[i])
e.sort()
j = 0
ans = []
for i in range(n):
    if i % 2 == 0:
        ans.append(e[j])
        j += 1
    else: ans.append(l[i])
print(*ans)
