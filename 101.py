# Question:-
'''
J.S.Bhayana gave an integer array A of size N. If A[i] occurs A[i + 1] times in the array, i is called a beautiful index.
Find the number of beautiful indices in the array. (1 <= i < N) (1 based indexing)

Input Description:
The first line contains an integer N, denoting the size of the array. The next line contains N space separated integers.

Output Description:
Print a line containing the number of beautiful indices in the array.


Sample Input :
4
1 2 1 4 1 1

Sample Output :
3
'''



# Solution:-
def count_beautiful_indices(arr):
    occurrences = {}
    beautiful_indices = 0

    for num in arr:
        occurrences[num] = occurrences.get(num, 0) + 1

    for i in range(len(arr) - 1):
        if occurrences[arr[i]] == arr[i + 1]:
            beautiful_indices += 1

    return beautiful_indices

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    beautiful_indices_count = count_beautiful_indices(numbers)
    print(beautiful_indices_count)
