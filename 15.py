# Question:-
'''
Shreya is a brilliant girl. She likes to memorize the numbers. These numbers will be shown to her.
As an examiner develop an algorithm to test her memory.


CONSTRAINTS
1<=Y,N,T<=1000

Input Description:
First line contains no. of test cases(Y). 
Next line contains a number N. 
Next line contains n space separated numbers Next line contains a number T denoting the number of questions asked from you regarding the given array. 
Next line contains T space separated numbers.

Output Description:
Print the occurrence of each number if present else “NOT PRESENT”


Sample Input :
10
1 1 1 2 2 2 3 8 9 7
5
1 2 3 0 5

Sample Output :
3 3 1 Not Present Not Present
'''



# Solution:-
n = int(input())
a = list(map(int,input().split(" ")))
b = int(input())
c = list(map(int,input().split(" ")))
output = []
for i in c:
    if i in a:
        output.append(a.count(i))
    else:
        output.append("Not Present")
print(*output)
