# Question:-
'''
Rahul is given an array containing digits values ranging from 0-9,Rahul’s task is to find the sum of minimum two numbers formed by the digits,
but he has some other work to do, he called you and told you that he is busy with some work,your task is to do the same work for rahul

 
Input Description:
You are given a number ‘n’ denoting size of array Next line contains n space separated numbers

Output Description:
Print the sum of numbers formed by it


Sample Input :
6
6 8 4 5 2 3

Sample Output :
604
'''



# Solution:-
def sum_of_minimum_two_numbers(arr):
    arr.sort()
    num1 = 0
    num2 = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            num1 = num1 * 10 + arr[i]
        else:
            num2 = num2 * 10 + arr[i]

    return num1 + num2

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    result = sum_of_minimum_two_numbers(numbers)
    print(result)
