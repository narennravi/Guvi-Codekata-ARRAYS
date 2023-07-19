# Question:-
'''
Ramesh is searching a solution to problem posted. The statement is as follows
Print the maximum sum produced by increasing subarray. Ramesh is very confused to see the question,Help him.


Input Description:
You are given a number ‘n’,Then next line contains n space separated numbers.

Output Description:
Maximum sum value produced by the increasing sub array of size 'n'


Sample Input :
6
2 1 4 7 3 6

Sample Output :
12
'''



# Solution:-
def max_increasing_subarray_sum(n, arr):
    if n == 0:
        return 0

    dp = [0] * n
    dp[0] = arr[0]
    max_sum = dp[0]

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            dp[i] = dp[i - 1] + arr[i]
        else:
            dp[i] = arr[i]

        max_sum = max(max_sum, dp[i])

    return max_sum

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    max_sum = max_increasing_subarray_sum(n, numbers)
    print(max_sum)
