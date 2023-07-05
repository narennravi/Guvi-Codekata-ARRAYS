# Question:-
'''
Rohit is a bachelor and is looking for a suitable girl to marry.

He wants to marry a girl who has at least one of the 8 qualities mentioned below:-

1) The girl should be rich.
2) The girl should be an Engineer/Doctor.
3) The girl should be beautiful.
4) The girl should be of height 5.3".
5) The girl should be working in an MNC.
6) The girl should be an extrovert.
7) The girl should not have spectacles.
8) The girl should be kind and honest.


He is in search of a bride who has some or all of the 8 qualities mentioned above. On bride hunting, he may find more than one contenders to be his wife.
In that case, he wants to choose a girl whose house is closest to his house. Find a bride for Rohit who has maximum qualities.
If in case, there are more than one contenders who are at equal distance from Rohit's house; then print "“He's not interested in polygamy”".

In case there is no suitable girl who fits the criteria then print “"No suitable girl found"”
Given a Matrix N*M, Rohit's house is at (1, 1). It is denoted by value 1. In the same matrix, the location of a marriageable Girl is also denoted by 1.
Since, the location of the boy is at location (1, 1), it should not be considered as the location of a marriageable Girl’s location.
The qualities of that girl, as per Rohit's criteria, have to be decoded from the number of non-zero neighbors (max 8-way) she has. 
Similar to the condition above, 1 at location (1, 1) should not be considered as the quality of a Girl. See Example section to get a better understanding.

Find a suitable bride for Rohit and print the row and column of the bride, and find out the number of qualities that the Bride possesses.

NOTE: - Distance is calculated in number of hops in any direction i.e. (Left, Right, Up, Down and Diagonal)


Input Description:
First Line contains the row (N) and column (M) of the houses Next N lines contain the data about girls and their qualities.

Output Description:
It will contain the row and column of the bride, and the number of qualities that Bride possess separated by a colon (i.e. :).


Sample Input :
2 9
1 0 1 1 0 1 1 1 1
0 0 0 1 0 1 0 0 1

Sample Output :
1:7:3
'''


# Solution:-
def is_valid_cell(row, col, n, m):
    return row >= 0 and row < n and col >= 0 and col < m

def find_bride(matrix, n, m):
    max_qualities = 0
    bride_row, bride_col = -1, -1

    for row in range(n):
        for col in range(m):
            if row == 0 and col == 0:
                continue  # Skip Rohit's house

            if matrix[row][col] == 1:  # Potential bride
                qualities = 0

                # Check neighbors in the 8-way direction
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue  # Skip the current cell

                        if is_valid_cell(row+dr, col+dc, n, m) and matrix[row+dr][col+dc] == 1:
                            qualities += 1

                if qualities > max_qualities:
                    max_qualities = qualities
                    bride_row, bride_col = row+1, col+1

    if bride_row != -1 and bride_col != -1:
        return f"{bride_row}:{bride_col}:{max_qualities}"
    else:
        return "No suitable girl found"

# Read input
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the bride
result = find_bride(matrix, n, m)
print(result)
