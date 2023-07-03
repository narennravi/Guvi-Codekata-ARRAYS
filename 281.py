# Question:-
'''
Kedar has ordinary pan scales and several weights of an equal mass. Kedar has already put some weights on the scales, while other weights are untouched.
Kedar is now wondering whether it is possible to put all the remaining weights on the scales so that the scales were in equilibrium.
The scales is in equilibrium if the total sum of weights on the left pan is equal to the total sum of weights on the right pan.
The first line has a non-empty sequence of characters describing the scales. In this sequence, an uppercase English letter indicates a weight,
and the symbol '|' indicates the delimiter (the character occurs in the sequence exactly once).
All weights that are recorded in the sequence before the delimiter are initially on the left pan of the scale.
All weights that are recorded in the sequence after the delimiter are initially on the right pan of the scale.
The second line contains a non-empty sequence containing uppercase English letters. Each letter indicates a weight which is not used yet.
It is guaranteed that all the English letters in the input data are different. It is guaranteed that the input does not contain any extra characters.


Example:
INPUT
AC|T
L

OUTPUT
AC|TL
'''


# Solution:-
def balance_scales(scales, weights):
    left, right = scales.split('|')
    left_sum = sum(ord(c) for c in left)
    right_sum = sum(ord(c) for c in right)
    
    for weight in weights:
        if weight not in left and weight not in right:
            if left_sum <= right_sum:
                left += weight
                left_sum += ord(weight)
            else:
                right += weight
                right_sum += ord(weight)
    
    return left + '|' + right


# Read input
scales = input()
weights = input()

# Balance the scales
result = balance_scales(scales, weights)

# Print the result
print(result)
