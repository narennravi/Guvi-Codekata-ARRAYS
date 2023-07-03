# Question:-
'''
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), if it is not possible to select coins in such a way that they sum up to S then print '-1'.
Example: Given coins with values 1, 3, and 5. And the sum S is 11.
Output: 3, 2 coins of 3 and 1 coin of 5

Input Size : N<=10000

Example:
INPUT
3 11
1 3 5

OUTPUT
3
'''


# Solution:-
def min_coins(coins, S):
 
  # Initialize the dp table.
  dp = [float("inf")] * (S + 1)
  dp[0] = 0

  # Recursively compute the minimum number of coins required for each amount.
  for coin in coins:
    for i in range(coin, S + 1):
      dp[i] = min(dp[i], dp[i - coin] + 1)

  # Return the minimum number of coins required to make the change.
  if dp[S] == float("inf"):
    return -1
  else:
    return dp[S]


if __name__ == "__main__":
  # Read the input.
  N, S = map(int, input().split())
  coins = list(map(int, input().split()))

  # Find the minimum number of coins required.
  min_coins_required = min_coins(coins, S)

  # Print the output.
  if min_coins_required == -1:
    print("-1")
  else:
    print(min_coins_required)
