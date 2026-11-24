
name = input("Enter Student Name: ") if __import__('sys').stdin.isatty() else "Shylini"
program = input("Enter Program: ") if __import__('sys').stdin.isatty() else "BCA"
semester = input("Enter Semester: ") if __import__('sys').stdin.isatty() else "3"

n = int(input("Enter number of courses: ")) if __import__('sys').stdin.isatty() else 3

courses = []

for i in range(n):
    if __import__('sys').stdin.isatty():
        course = input("Enter Course Name: ")
        marks = int(input("Enter Marks: "))
    else:
        course = ["Python", "Java", "Data Mining"][i]
        marks = [75, 40, 85][i]

    courses.append((course, marks))

print("\n----- Student Details -----")
print("Name:", name)
print("Program:", program)
print("Semester:", semester)

print("\n----- Course Details -----")

for course, marks in courses:
    print(course, ":", marks)

print("\n----- Courses with Marks Below 50 -----")

for course, marks in courses:
    if marks < 50:
        print(course, ":", marks, "(Below 50)")