# Question:-
'''
ind the man who will survive. There is a scenario that only one person will survive. ‘N’ person will stand in a circle. Initially first person will be holding the gun.
You are given with number ‘k’. The person who is holding the gun has to count to ‘k’ starting from him and shoot the person at which k ends and then pass the gun to next alive person. 
Your task is to find the place where you will survive.


Input Description:
Two numbers – ‘N’ and ‘k’

Output Description:
Find the place where you will be safe (indexing at 1)


Sample Input :
2
1

Sample Output :
2
'''


# Solution:-
N = int(input())  
k = int(input())  

people = [1] * N  
current = 0  


while people.count(1) > 1:
    count = 0
    while count < k:
        if people[current] == 1:
            count += 1
        if count < k:
            current = (current + 1) % N

    people[current] = 0
    current = (current + 1) % N


last_person_index = people.index(1) + 1

print(last_person_index)
