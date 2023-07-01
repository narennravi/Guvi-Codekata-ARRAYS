# Question:-
'''
Bala is the CEO of a company and decides to reward a few hardworking employees with an extra bonus. 
He wants to find out the number of employees who are working parallely on two different projects and give them a bonus.
The ids of employees working on a particular project are stored in an array.Given two arrays project1 and project2, 
find out whether the employees working on project2 are a subset of employees working on project1.


Constraints:
1 <= project1[i], project2[j] <= 100


Input Description:
First line denotes the number of employees working on project 1. Second line contains the employee ids of the employees working on project 1. Third line denotes the number of employees working on project 2 and 4th line contains employee ids of the employees working on project 2.

Output Description:
(yes/no) Whether the second array is a subset of the first array.


Sample Input :
3
1 2 3
2
1 2

Sample Output :
yes
'''



# Solution:-
# Read the input
n1 = int(input())  # Number of employees in project1
project1 = set(map(int, input().split()))  # Employee ids in project1

n2 = int(input())  # Number of employees in project2
project2 = set(map(int, input().split()))  # Employee ids in project2

# Check if project2 is a subset of project1
if project2.issubset(project1):
    print("yes")
else:
    print("no")
