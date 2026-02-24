n = int(input())

students_grades = {} 

for i in range(n):
    name, grade = input().split()
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(float(grade))

for name, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    grades_formatted = ' '.join(f"{grade:.2f}" for grade in grades)
    print(f"{name} -> {grades_formatted} (avg: {average_grade:.2f})")
    
