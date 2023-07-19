# Question:-
'''
Karthick loves to analyse patterns in numbers. He is given a list of positive integers a1,a2...aN. 
He wants to count the number of pairs (ai,aj) such that: ai < aj. He solved it and wants to cross-check his answer with yours.
Compute the same and display the number of pairs possible so that Karthick can verify his answer.
 

Constraints:
1<=N<=10^3
1<=a[i]<=10^3
 

Input Description:
First line contains a positive integer N denoting the size of array.The second line contains N space-separated positive integers denoting the elements of array.

Output Description:
A single line containing number of pairs possible.


Sample Input :
3
2 1  

Sample Output :
1
'''



# Solution:-
def count_pairs(arr):
    arr.sort()
    n = len(arr)
    i = 0
    j = 1
    pairs_count = 0

    while j < n:
        if arr[i] < arr[j]:
            pairs_count += n - j
            i += 1
            j += 1
        else:
            i += 1
            if i == j:
                j += 1

    return pairs_count

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    pairs = count_pairs(numbers)
    print(pairs)
