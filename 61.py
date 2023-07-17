# Question:-
'''
Rajat is given some special task to calculate the largest sum of two consecutive elements.He solved some of questions but he is not sure whether his answer is correct or not.
Your task is to help him in determining whether answers posted by him are correct or not.


Input Description:
The first line of the input is a integer N. The second line of the input consists of N space separated integer.

Output Description:
Print the max sum of two consecutive numbers from the given N numbers


Sample Input :
5
1 5 6 8 3

Sample Output :
14
'''



# Solution:-
def largest_sum_of_consecutive_elements(arr):
    max_sum = float('-inf')
    n = len(arr)

    for i in range(n - 1):
        current_sum = arr[i] + arr[i + 1]
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    max_sum = largest_sum_of_consecutive_elements(numbers)
    print(max_sum)
