# Question:-
'''
Bob has a strange counter. At the first second, t = 1, it displays the number 3. 
At each subsequent second, the number displayed by the counter decrements by 1. The counter counts down in cycles.
In the second after the counter counts down to 1, the number becomes 2x the initial number for that countdown cycle and then continues counting down from the new initial number in a new cycle.
The diagram shows the counter values for each time t in the first three cycles.Find the value corresponding to the given time t.
Input Size : t<=100000

Example:
INPUT
4

OUTPUT
6
'''


# Solution:-
t = int(input())

cycle = 1
initial_value = 3

while t > 3 * (2 ** (cycle - 1)):
    t -= 3 * (2 ** (cycle - 1))
    initial_value *= 2
    cycle += 1

value = initial_value - (t - 1)
print(value)
