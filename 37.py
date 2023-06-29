# Question:-
'''
Prakash is bored and wants to spends his time. He starts rolling a die and observes the value that is shown.
He rolls the dice N times and observes that just one number appears distinctly, all the others get repeated or does not appear at all.
Find out which was the number that puzzled Prakash for sometime, after which he realised that it was just a coincidence.


Constraints
0 <   N  <= 100
0 <= A[i] <= 100
 
Input Description:
The first line contains a positive integer N, denoting the size of the array. The second line contains N positive integers, denoting the face values that appeared when the die was rolled.

Output Description:
Print out the singly occurring number.


Sample Input :
5
1 1 2 5 5

Sample Output :
2
'''


# Solution:-
n = int(input())
lst = list(map(int,input().split()))
a = list(set(lst))
for i in a:
    if lst.count(i) == 1:
        print(i)
