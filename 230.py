# Question:-
'''
Given an amount A(integer) find the number of currency notes required to make the amount up in the most optimal way. The available denominations are 1000,500,100,50,10,1. The question is set in PRE-DEMONITISATION era so 1000 rupee notes are available :)
eg: rs 689 (* currency notes are 500,100,50,10,1 )
500+100+50+(3*10)+(9*1)
count=15

Input Size : N <= 100000000


Sample Testcase :
INPUT
689

OUTPUT
15
'''

# Solution:-
def count_currency_notes(amount):
    denominations = [1000, 500, 100, 50, 10, 1]
    count = 0

    for denomination in denominations:
        count += amount // denomination
        amount %= denomination

    return count

# Read input
amount = int(input())

# Call the function to count currency notes
note_count = count_currency_notes(amount)

# Print the number of currency notes required
print(note_count)
