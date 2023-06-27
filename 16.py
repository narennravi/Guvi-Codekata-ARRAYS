# Question:-
'''
Loki wants to steal the tesseract but in order to do so, he has to rearrange the elements in an array in a specific manner which is mentioned in a clue.
The clue says ‘cursed are the odd and sorted are the even’. Loki manages to decode the clue which translates to “sort the even positioned elements of an array,
starting from the element at index 0, in ascending order”. Manipulate the array so as to help Loki steal the tesseract.
 

Input Description:
Size of the array followed by the elements of the array

Output Description:
Even index array elements sorted in ascending order


Sample Input :
5
3 9 1 44 6

Sample Output :
1 9 3 44 6
'''



# Solution:-
n=int(input())
arr=list(map(int,input().split()))
odd=[]
even=[]
res=[]
for i in range(n):
  if i%2==0 or i==0:
    even.append(arr[i])
    #print(even)
  else:
    odd.append(arr[i])
    #print(odd)
even.sort()
#print(even)

for i in range(len(even)):
  res.append(even[i])
  if i <len(odd):
    res.append(odd[i])
print(*res)
