# Question:-

'''
You are given a string of different type of brackets. Your task is to check whether the given string is balanced or not balanced.
A string is said to be balanced if the number of opening brackets are equal to the number of closing brackets where the brackets should be of same kind.

Input Description:
You are given a string ‘s’.

Output Description:
Print 'yes' if the given string is balanced and no if it is not


Sample Input :
{}(())[][][{}]

Sample Output :
yes
'''



# Solution:-
s = str(input())
if (s.count('(') == s.count(')') and s.count('{') == s.count('}')) and s.count('[') == s.count(']'):
	print("yes")
else:
	print("no")
