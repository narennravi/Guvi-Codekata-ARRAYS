# Question:-
'''
The Romans have attacked again. This time they are much more than the Persians but Shapur is ready to defeat them. He says: 'A lion is never afraid of a hundred sheep'.
Nevertheless Shapur has to find weaknesses in the Roman army to defeat them. So he gives the army a weakness number.
In Shapur's opinion the weakness of an army is equal to the number of triplets i, j, k such that i < j < k and ai > aj > ak where ax is the power of man standing at position x.
The Roman army has one special trait — powers of all the people in it are distinct.
Help Shapur find out how weak the Romans are.

The first line of input contains a single number n, the number of men in Roman army. Next line contains n different positive integers powers of men in the Roman army.
Input Size : N<=100000


Example:
INPUT
3
3 2 1
OUTPUT
1
'''


# Solution:-
def find_weakness(powers):

  # Create a list of triplets of powers.
  triplets = []
  for i in range(len(powers) - 2):
    for j in range(i + 1, len(powers) - 1):
      for k in range(j + 1, len(powers)):
        triplets.append((powers[i], powers[j], powers[k]))

  # Count the number of triplets where the first power is greater than the second power, which is greater than the third power.
  weakness = 0
  for triplet in triplets:
    if triplet[0] > triplet[1] > triplet[2]:
      weakness += 1

  return weakness


if __name__ == "__main__":
  # Read the number of men in the Roman army.
  n = int(input())

  # Read the powers of the men in the Roman army.
  powers = list(map(int, input().split()))

  # Find the weakness of the Roman army.
  weakness = find_weakness(powers)

  # Print the weakness of the Roman army.
  print(weakness)
