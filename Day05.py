# Project: Student Grade Analyzer

def calculate_average(grades):
    return sum(grades) / len(grades)

def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def print_student_report(students):
    print("Student Report")
    print("-" * 40)
    for student in students:
        name = student['name']
        grades = student['grades']
        avg = calculate_average(grades)
        grade = assign_grade(avg)
        print(f"Name: {name}\nGrades: {grades}\nAverage: {avg:.2f}\nGrade: {grade}")
        print("-" * 40)

# Sample data
students = [
    {'name': 'Alice', 'grades': [85, 90, 78]},
    {'name': 'Bob', 'grades': [65, 70, 72]},
    {'name': 'Charlie', 'grades': [95, 100, 98]},
    {'name': 'Diana', 'grades': [55, 60, 58]}
]

# Run the report
print_student_report(students)
