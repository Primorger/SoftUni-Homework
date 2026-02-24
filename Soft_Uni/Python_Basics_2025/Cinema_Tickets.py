command = input()
total_tickets = 0
total_students = 0
total_standard = 0
total_kid = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0

while command != "Finish":
    movie_name = command
    seats = int(input())
    sold_tickets = 0
    student_tickets = 0
    standard_tickets = 0
    kid_tickets = 0

    while sold_tickets < seats:
        ticket_type = input()
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        elif ticket_type == "End":
            break

        sold_tickets += 1

    total_tickets += sold_tickets
    total_students += student_tickets
    total_standard += standard_tickets
    total_kid += kid_tickets
    total_student_tickets += student_tickets
    total_standard_tickets += standard_tickets
    total_kid_tickets += kid_tickets

    print(f"{movie_name} - {sold_tickets / seats * 100:.2f}% full.")

    command = input()

print(f"Total tickets: {total_tickets}")
print(f"{total_students / total_tickets * 100:.2f}% student tickets.")
print(f"{total_standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{total_kid / total_tickets * 100:.2f}% kids tickets.")
