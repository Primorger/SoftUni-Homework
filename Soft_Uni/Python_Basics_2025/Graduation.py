name = input()

grades_counter = 0
years_counter = 0
failed_counter = 0

while years_counter < 12:
    grade = float(input())

    if grade < 4:
        failed_counter += 1
        if failed_counter > 1:
            excluded_year = years_counter + 1
            print(f"{name} has been excluded at {excluded_year} grade")
            break

        continue
    years_counter += 1
    grades_counter += grade

    if years_counter == 12:
        avg_grade = grades_counter / 12
        print(f"{name} graduated. Average grade: {avg_grade:.2f}")
        break