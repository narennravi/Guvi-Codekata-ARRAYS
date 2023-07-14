# Question:-
'''
You are given with arrays containing some non negative integers.Your task is to make the largest number out of it.

Input Description:
First line contains the size of array ’n’. Second line contains the n space separated integers.

Output Description:
Print the largest element that can be form out of the array


Sample Input :
6
12 19 546 60

Sample Output :
605461912

'''



# Solution:-
def largest_number(arr):
    arr = list(map(str, arr))
    arr.sort(key=lambda x: x + x[::-1], reverse=True)
    return ''.join(arr)

# Example usage
n = int(input())
arr = list(map(int, input().split()))

largest_num = largest_number(arr)
print(largest_num)
