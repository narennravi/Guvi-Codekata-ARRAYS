# Question:-
'''
Rahul was learning about numbers in list. He came across one word ground of a number.
A ground of a number is defined as the number which is just smaller or equal to the number given to you.Hence he started solving some assignments related to it.
He got struck in some questions. Your task is to help him.
 
O(n) time complexity
O(n) Auxilary space


Input Description:
First line contains two numbers ‘n’ denoting number of integers and ‘k’ whose ground is to be check. Next line contains n space separated numbers.

Output Description:
Print the index of val.Print -1 if equal or near exqual number


Sample Input :
7 3
1 2 3 4 5 6 7

Sample Output :
2
'''


# Solution:-
def find_ground_index(n, k, numbers):
    ground_index = -1  # Default index if no ground is found
    for i in range(n):
        if numbers[i] <= k:
            ground_index = i
        else:
            break
    return ground_index


# Read the input values
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Find the index of the ground of k in the list
ground_index = find_ground_index(n, k, numbers)

# Print the result
print(ground_index)
