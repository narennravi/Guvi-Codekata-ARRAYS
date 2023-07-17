# Question:-
'''
Ramit is given a list of both positive and negative integers. He has to tell the maximum sum out of all subarrays in the given list. 
He got confused and requested help from you. Now it is your task to find the maximum sum out of all subarrays in the given list.

Input Description:
You are given a number 'n'. Next line contains n space separated numbers.

Output Description:
Print the max sum of subarray.


Sample Input :
5
1 2 3 -2 5

Sample Output :
9
'''



# Solution:-
def max_subarray_sum(arr):
    max_so_far = max_ending_here = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    max_sum = max_subarray_sum(numbers)
    print(max_sum)
