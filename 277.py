# Question:-
'''
Once detective saikat was solving a murder case. While going to the crime scene he took the stairs and saw that a number is written on every stair.
He found it suspicious and decides to remember all the numbers that he has seen till now. While remembering the numbers he found that he can find some pattern in those numbers.
So he decides that for each number on the stairs he will note down the sum of all the numbers previously seen on the stairs which are smaller than the present number. 
Calculate the sum of all the numbers written on his notes diary.
Input Size : 1<=N<=1000

Example:
INPUT
3
1 2 3

OUTPUT
4(0+1+1+2)
'''


# Solution:-
def sum_of_notes(N, numbers):
    total_sum = 0  # Initialize the total sum of notes
    seen_numbers = []  # List to store the previously seen numbers

    for num in numbers:
        smaller_numbers_sum = sum([x for x in seen_numbers if x < num])
        total_sum += smaller_numbers_sum
        seen_numbers.append(num)

    return total_sum

# Read input
N = int(input())
numbers = list(map(int, input().split()))

# Call the function and print the result
print(sum_of_notes(N, numbers))
