# Question:-
'''
There is one meeting room in Flipkart. There are n meetings in the form of (S [ i ], F [ i ]) where S [ i ] is start time of meeting i and F [ i ] is finish time of meeting i.
Given a number N followed by 2 arrays S and F of sizes N and N, What is the maximum number of meetings that can be accommodated in the meeting room assuming the room can only accommodate one meeting at a time.
Input Size : 1 <= N <= 100000


Sample Testcases :
INPUT
3
10 12 30
20 25 30

OUTPUT
2
'''




# Solution:-
N = int(input())
S = list(map(int, input().split()))
F = list(map(int, input().split()))

meetings = list(zip(S, F))
meetings.sort(key=lambda x: x[1])  # Sort the meetings based on finish time

count = 1
last_finish = meetings[0][1]

for i in range(1, N):
    if meetings[i][0] > last_finish:
        count += 1
        last_finish = meetings[i][1]

print(count)
