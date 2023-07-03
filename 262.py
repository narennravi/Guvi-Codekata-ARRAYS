# Question:-
'''
Given a string containing a mix of upper and lowercase characters, sort the letters in ascending order such that the positions of upper and lowercase letters do not change.
(eg) If the string is guVIONLineCoDIng, then the output must be  egCDIILginNnOVou
 

Input Description:
A string

Output Description:
Letters of the string sorted such that positions of upper and lower characters do not change.


Sample Input :
GuVi

Sample Output :
GiVu
'''


# Solution:-
def sort_letters(string):
    # Separate uppercase and lowercase letters
    uppercase_letters = sorted([c for c in string if c.isupper()])
    lowercase_letters = sorted([c for c in string if c.islower()])

    # Initialize pointers
    uppercase_pointer = 0
    lowercase_pointer = 0

    # Create the result string
    result = ''
    for c in string:
        if c.isupper():
            result += uppercase_letters[uppercase_pointer]
            uppercase_pointer += 1
        elif c.islower():
            result += lowercase_letters[lowercase_pointer]
            lowercase_pointer += 1
        else:
            result += c

    return result


# Read input
string = input()

# Sort the letters
sorted_string = sort_letters(string)

# Print the sorted string
print(sorted_string)
