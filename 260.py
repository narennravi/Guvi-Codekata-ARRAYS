# Question:-
'''
N students have the option for opting N different courses. The data about which student has opted for which course is represented in a table with rows representing the course ids and the columns having the student names.
The entries in the table are either 0 or 1. 1 if a particular student has opted for a particular course, and 0 if otherwise. Find the course id for which maximum number have opted for and also display the number of students who have opted for that course.
Note: Course ids start from 0 and go upto N.
 

Input Description:
The first line is two integers row and col denoting the no of rows and columns of table . Then in the next line are row*col space separated values of whether a student has opted a course or not.

Output Description:
Print the required course id and the number of students, separated by colons.


Sample Input :
3 4
0 1 1 1
0 0 1 1
0 0 1 1

Sample Output :
0:3
'''



# Solution:-
def find_max_students_course(table):
    max_students = 0
    course_id = -1

    for i, row in enumerate(table):
        students_count = sum(row)
        if students_count > max_students:
            max_students = students_count
            course_id = i

    return course_id, max_students

if __name__ == "__main__":
    row, col = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(row)]

    course_id, max_students = find_max_students_course(table)

    print(f"{course_id}:{max_students}")
