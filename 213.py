# Question:-

'''
Tahir gets into an elevator. The elevator is programmed such that it moves up the number of floors mentioned at odd indexes of an array A[] and moves down the number of floors mentioned at even indexes of the array A[], in sequence.
Sort the array such that when Tahir gets out of the elevator, he is at any floor other than the floor at which he got into the elevator. The index of the ground floor is 1 and assume that the building has 100 floors.
The lift can move only up to the ground floor(i.e) floor indexes are positive integers.
 

Input Description:
Size of array followed by floor number at which Tahir gets into the elevator. The second line contains the number of elements in the array.

Output Description:
Sorted array according to the problem specifications. If no such arrangement is possible output “not possible”


Sample Input :
5 8
5 8 1 3 4

Sample Output :
1 3 4 5 8

'''



# Solution:-
def sort_elevator_array(floor, arr):
    arr.sort()

    # Swap the floor number at which Tahir got into the elevator with the last element
    arr[-1], arr[arr.index(floor)] = arr[arr.index(floor)], arr[-1]

    return arr


if __name__ == "__main__":
    # Read the input
    size, floor = map(int, input().split())
    elevator_array = list(map(int, input().split()))


    # Check if the elevator can move to a different floor after sorting
    if elevator_array.count(floor) == 1:
        # If there's only one occurrence of Tahir's floor, sort the array and print the result
        sorted_array = sort_elevator_array(floor, elevator_array)
        print(*sorted_array)
    
    else:
        # If there are multiple occurrences of Tahir's floor, it's not possible to find another floor
        print("not possible")
