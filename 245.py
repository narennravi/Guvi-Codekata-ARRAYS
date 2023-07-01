# Question:-
'''
Given an array of size N, find the minimum number of swaps required to sort the array.

Input Description:
Size of the array followed by the elements of the array

Output Description:
Minimum number of swaps required


Sample Input :
4
4 3 2 1

Sample Output :
2
'''


# Solution:-
def minimum_swaps(array):

  elements = []
 
  for element in array:
    elements.append(element)

  # Sort the elements in ascending order
  elements.sort()
  num_swaps = 0


  for i in range(len(array)):

    # If the current element is not in its correct position, swap it with the element in the correct position
    if elements[i] != array[i]:

      # Find the index of the element in the correct position
      index = elements.index(array[i])

      # Swap the elements
      array[i], array[index] = array[index], array[i]
      num_swaps += 1

  return num_swaps


def main():

  n = int(input())
  array = list(map(int, input().split()))

  # Find the minimum number of swaps required to sort the array
  num_swaps = minimum_swaps(array)
  print(num_swaps)


if __name__ == "__main__":
  main()
