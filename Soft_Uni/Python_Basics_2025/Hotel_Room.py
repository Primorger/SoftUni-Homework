month = str(input())  #  May  June  July  August  September  October
length_of_stay = int(input())
apartment_cost = 0
studio_cost = 0
apartment_discount = 0
studio_discount = 0

if month == "May" or month == "October":
    if length_of_stay > 7:
        studio_discount = 0.05
        if length_of_stay > 14:
            studio_discount = 0.30

    studio_cost = 50 * length_of_stay
    apartment_cost = 65 * length_of_stay

elif month == "June" or month == "September":
    if length_of_stay > 14:
        studio_discount = 0.20

    studio_cost = 75.20 * length_of_stay
    apartment_cost = 68.70 * length_of_stay

elif month == "July" or month == "August":
    studio_cost = 76 * length_of_stay
    apartment_cost = 77 * length_of_stay

if length_of_stay > 14:
    apartment_discount = 0.10

apartment_cost = apartment_cost * (1 - apartment_discount)
studio_cost = studio_cost * (1 - studio_discount)

print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")