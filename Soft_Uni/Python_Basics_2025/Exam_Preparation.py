allowed_bad_grades = int(input())
bad_grades = 0
command = input()
grade = 0
total_grade = 0
last_problem = ""
has_failed = False
num_of_grades = 0
while command != "Enough":
    last_problem = command
    grade = int(input())
    num_of_grades += 1
    total_grade += grade
    if grade <= 4:
        bad_grades += 1
        if bad_grades >= allowed_bad_grades:
            has_failed = True
            break
    command = input()
if has_failed:
    print(f"You need a break, {bad_grades} poor grades.")
if command == "Enough":
    print(f"Average score: {(total_grade/num_of_grades):.2f}")
    print(f"Number of problems: {num_of_grades}")
    print(f"Last problem: {last_problem}")


