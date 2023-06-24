# Question:-
'''
You are given an array of numbers. Print the least occurring element. 
If there is more than 1 element print all of them in decreasing order of their value.


Input Description:
You are given a number ‘n’ denoting size of array. Next line contains n space separated numbers.

Output Description:
Print the number as mentioned


Sample Input :
9
1 6 4 56 56 56 6 4 2

Sample Output :
2 1

'''



# Solution:-
n = int(input())
arr = list(map(int, input().split()))

# count the occurrences of each number
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

# find the least occurring number
least_freq = min(freq.values())

# collect all numbers with least frequency
result = []
for num, count in freq.items():
    if count == least_freq:
        result.append(num)

# sort the result in decreasing order
result.sort(reverse=True)

# print the result
print(*result)
