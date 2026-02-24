type_of_projection = input()
rows = int(input())
columns = int(input())
ticket_price = 0

if type_of_projection == "Premiere":
    ticket_price = 12.00
elif type_of_projection == "Normal":
    ticket_price = 7.50
elif type_of_projection == "Discount":
    ticket_price = 5.00

capacity = rows * columns

total_income = capacity * ticket_price
print(f"{total_income:.2f}")