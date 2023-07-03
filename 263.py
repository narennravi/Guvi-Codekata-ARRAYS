# Question:-
'''
Das lives in a city which is having skyscrapers. Das has a wish and wants to see the buildings on which sunlight falls when the sun sets.
Help him in counting the number of buildings receiving the sunlight. Note: A taller building casts a shadow on a shorter building.
Given an array H denoting heights of buildings. You have to count the buildings which will see the sun set 
(Assume : Sun set on the side of array ending i.e at the last element of the array).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
1 ≤ Hi ≤ 108

 
Input Description:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the number of buildings. The second line of each test case contains separated values of heights of buildings.

Output Description:
Print the total number of buildings which will see the sunset.


Sample Input :
2
5
7 4 8 2 9
4
5 3 4 1

Sample Output :
1
3
'''


# Solution:-
# Function to count the number of buildings that will see the sunset
def count_buildings_with_sunset(heights):
    count = 0
    max_height = 0

    # Iterate through the array from right to left
    for height in reversed(heights):
        if height > max_height:
            count += 1
            max_height = height

    return count


# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the number of buildings and the heights
    N = int(input())
    heights = list(map(int, input().split()))

    # Count the number of buildings that will see the sunset
    result = count_buildings_with_sunset(heights)

    # Print the result
    print(result)
