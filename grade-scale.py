'''
The students of SMA Persekutuan Kajang have sat the Asas Sains Komputer subject final exam.
After finished marking the papers, Cikgu Noraznina gave a grade to each student based on the range of marks as below:

Grade	A	B	C	D	E   F
Marks	85-100	70-84	60-69	50-59	40-49	0-39

Given a search grade and a list of marks obtained by students, you are to count the number of students who obtained that grade.


3 lines of input.
The first line contains the string g, which represents the search grade.
The second line contains the integer n, which represents the number of students who sat the final exam.
The third line contains an integer for all integer mi that is space separated, where represents the marks obtained by each student.
'''

search_grade = input()
n = int(input())

marks = list(map(int, input().split()))

print(marks)

# Replace each mark with the grade
# Store the grade in list 'grades'

grades = []

for i in range(n):
    if marks[i] >= 85 and marks[i] <= 100:
        grades.append('A')
    elif marks[i] >= 70 and marks[i] <= 84:
        grades.append('B')
    elif marks[i] >= 60 and marks[i] <= 69:
        grades.append('C')
    elif marks[i] >= 50 and marks[i] <= 59:
        grades.append('D')
    elif marks[i] >= 40 and marks[i] <= 49:
        grades.append('E')
    elif marks[i] >= 0 and marks[i] <= 39:
        grades.append('F')

# Count the number of students who obtained the search grade
# Print the number of students who obtained the search grade

count = 0

for i in range(n):
    if grades[i] == search_grade:
        count += 1

print(count)
