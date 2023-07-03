# Question:-
'''
Check whether the given 4 points form a square or not.

Example:
INPUT
10 10
10 20
20 20
20 10

OUTPUT
yes
'''


# Solution:-
def is_square(points):

  if len(points) != 4:
    return False

  # Check if all four points are distinct.
  if len(set(points)) != 4:
    return False

  # Check if the four points are arranged in a square.
  for i in range(3):
    if points[i][0] != points[i + 1][0] or points[i][1] != points[i + 1][1]:
      return False

  # Check if the four sides of the square are equal.
  for i in range(3):
    if points[i][0] != points[i + 1][0] or points[i][1] != points[i + 1][1]:
      return False

  return True


if __name__ == "__main__":
  points = [(10, 10), (10, 20), (20, 20), (20, 10)]

  if is_square(points):
    print("yes")
  else:
    print("no")
