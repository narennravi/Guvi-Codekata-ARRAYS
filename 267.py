# Question:-
'''
You are given a postfix expression. Evaluate the given expression and print the result.

Input Description:
The first line of the input is a string N, containing operators and numbers seperated by the single space which forms a postfix expression

Output Description:
Evaluate the post expression and print the result.


Sample Input :
5 3 1 * + 9 -

Sample Output :
-1
'''


# Solution:-
s = input().split()
stk = []
for i in range(len(s)):
    if s[i] not in "+-*/%":
        stk.insert(0, s[i])
    else:
        a = int(stk.pop(0))
        b = int(stk.pop(0))
        if s[i] == '+' : stk.insert(0, b + a)
        elif s[i] == '-' : stk.insert(0, b - a)
        elif s[i] == '*' : stk.insert(0, b * a)
        elif s[i] == '/' : stk.insert(0, b / a)
        elif s[i] == '%' : stk.insert(0, b % a)
        else: continue
print(stk[0])
