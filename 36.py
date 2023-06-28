# Question:-
'''
Rahul is fond of numbers.He is given a list of queries. 1 means store that element,2 means means print the minimum element of the stored list.
For more clarity see the input and output example


Input Description:
The first line of the input N indicates the size of the query list. For N lines, the queries are given with the format of '1 M', where M indicates the number to be stored and 1 indicates the query type. Similarly, '2' which indicates the type of query and it does not contain M since it is not required by this query type. Briefly saying, '1 M' means store that element M in a list '2' means print the minimum element of stored list

Output Description:
Print the minimum element and -1 if there are no elements in stored list if the querytype is 2. Store the given number in the list if the query type is 1.


Sample Input :
5
1 60
2
1 58
2
1 69

Sample Output :
60 58
'''


# Solution:-
q = int(input())
l = []
b = []

for _ in range(q):
    a = [int(x) for x in input().split()]
    if a[0] == 1: l.append(a[1])
    if a[0] == 2:
        if len(l) == 0: b.append(-1)
        else: b.append(min(l))
print(*b)
