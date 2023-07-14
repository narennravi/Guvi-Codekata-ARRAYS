# Question:-
'''
There are n people and k keys on a straight line. Every person wants to get to the office which is located on the line as well. 
To do that, he needs to reach some point with a key, take the key and then go to the office. Once a key is taken by somebody, it couldn't be taken by anybody else. 
You are to determine the minimum time needed for all n people to get to the office with keys. Assume that people move a unit distance per 1 second. 
If two people reach a key at the same time, only one of them can take the key. A person can pass through a point with a key without taking it.
The first line contains three integers n, k and p (1 ≤ n ≤ 1 000, n ≤ k ≤ 2 000, 1 ≤ p ≤ 1000000000) — the number of people, the number of keys and the office location.
The second line contains n distinct integers a1, a2, ..., an (1 ≤ ai ≤ 1000000000) — positions in which people are located initially. The positions are given in arbitrary order.
The third line contains k distinct integers b1, b2, ..., bk (1 ≤ bj ≤ 1000000000) — positions of the keys. The positions are given in arbitrary order. 
Note that there can't be more than one person or more than one key in the same point. A person and a key can be located in the same point.


Example:
INPUT
2 4 50
20 100
60 10 40 80

OUTPUT
50

'''



# Solution:-
import sys

def find_minimum_time(n, k, p, people, keys):
    people.sort()
    keys.sort()

    min_time = sys.maxsize

    for key in keys:
        curr_time = 0
        for i in range(n):
            curr_time = max(curr_time, abs(people[i] - key) + abs(key - p))
        
        min_time = min(min_time, curr_time)

    return min_time

# Example usage
n, k, p = map(int, input().split())
people = list(map(int, input().split()))
keys = list(map(int, input().split()))

min_time = find_minimum_time(n, k, p, people, keys)
print(min_time)





