# Question:-
'''
You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result

Input Description:
You are given a long string of digits

Output Description:
Print the desired result print -1 if result length is 0


Sample Input :
1331

Sample Output :
11
'''



#Solution:-
from itertools import groupby
no=int(input())
new_no=[int(no) for no in str(no)]
#print(no)
#res=[int[0] for i in groupby(new_no)]
#res = [i[0] for i in groupby(new_no)]
res = [i for i, j in groupby(new_no) if sum(1 for x in j) < 2]
print(*res,sep="")
