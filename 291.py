# Question:-
'''
Recently Kohli bought a very interesting book. He knows that it will take t seconds to read the book.
Kohli wants to finish reading as fast as he can.But he has some work to do in each of n next days.
The number of seconds that Kohli has to spend working during i-th day is ai. If some free time remains, he can spend it on reading.
Help Kohli to determine the minimum number of day when He finishes reading. It is guaranteed that the answer doesn't exceed n.
Remember that there are 86400 seconds in a day.
Input Size : N<=100T<=1000000

example
INPUT
2 2
86400 86398

OUTPUT
2
'''


# Solution:-
n, t = map(int, input().split())
work_time = list(map(int, input().split()))

remaining_time = t
for i in range(n):
    remaining_time -= (86400 - work_time[i])
    if remaining_time <= 0:
        print(i + 1)
        break
else:
    print(n)
