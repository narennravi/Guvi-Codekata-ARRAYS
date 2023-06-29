# Question:-
'''
There is a business analysis company named “AJ”. It hired two interns “A” and “B”.
Both of them are given tasks to sell product in n days.The one who will sell more share will get the job.
As A and B are good friends they decided that they will equalize the collected money, they are only allowed to swap more than one day’s share to make the total of each same.
Your task is to help them.


Constraints
1<=N,a[i],b[i]<=50

Input Description:
First line contains no of days. Next line contains the n space separated integers representing sale of A. Next line contains Space separated integers representing sale of B.

Output Description:
Print “yes” if it is possible by one one swap. Else no


Sample Input :
4 
5 7 4 6
1 2 3 8

Sample Output :
yes
'''



# Solution:-
def check_swap_possibility(n, sales_a, sales_b):
    sum_a = sum(sales_a)
    sum_b = sum(sales_b)

    if (sum_a - sum_b) % 2 != 0:
        return "no"

    diff = (sum_a - sum_b) // 2
    possible_swaps = set()

    for a in sales_a:
        b = a - diff
        if b in sales_b:
            possible_swaps.add((a, b))

    if len(possible_swaps) == 0:
        return "no"
    else:
        return "yes"


# Read input
n = int(input())
sales_a = list(map(int, input().split()))
sales_b = list(map(int, input().split()))

# Check if swap is possible and print the result
result = check_swap_possibility(n, sales_a, sales_b)
print(result)
