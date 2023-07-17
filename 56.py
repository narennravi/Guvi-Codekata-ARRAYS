# Question:-
'''
Rajesh was going through alternative array sorting. He wishes to print the array alternatively.
Hence hired you. Your task is to help rajesh in printing the array alternatively.

An alternative array is an array in which first element is maximum of the whole array second element is minimum of the whole array.
Third element is the second largest. Fourth element is the second smallest And so on. print the array in the desired manner.




Input Description:
You are given with the length of array ‘n’. followed by ‘n’ space separated numbers.

Output Description:
Print the array as mentioned.


Sample Input :
5 1 7 11 16 19

Sample Output :
19 1 16 7 11
'''



# Solution:-
def alternate_array_sort(arr):
    arr.sort()
    left, right = 0, len(arr) - 1
    result = []

    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[right])
            result.append(arr[left])

        left += 1
        right -= 1

    return result

if __name__ == "__main__":
    n, *numbers = map(int, input().split())
    result_array = alternate_array_sort(numbers)
    print(*result_array)
