
name = input("Enter Student Name: ")
program = input("Enter Program: ")
semester = input("Enter Semester: ")

n = int(input("Enter number of courses: "))

courses = []

for i in range(n):
    course = input("Enter Course Name: ")
    marks = int(input("Enter Marks: "))
    courses.append((course, marks))

print("\n----- STUDENT DETAILS -----")
print("Name:", name)
print("Program:", program)
print("Semester:", semester)

print("\n----- COURSE DETAILS -----")

for course, marks in courses:
    print(course, ":", marks)

print("\n----- COURSES BELOW 50 MARKS -----")

for course, marks in courses:
    if marks < 50:
        print(course, ":", marks, "- Failed")
