days = int(input())
total_food = float(input())
cookies = 0
food_eaten = 0
food_dog_eaten = 0
food_cat_eaten = 0
for current_day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    food_eaten += (dog_food + cat_food)
    if current_day % 3 == 0:
        cookies += (dog_food + cat_food) * 0.10

    food_dog_eaten += dog_food
    food_cat_eaten += cat_food

percent_cookies = round(cookies)
percent_food_eaten =  (food_eaten / total_food) * 100
percent_dog_food_eaten = (food_dog_eaten / food_eaten) * 100
percent_cat_food_eaten = (food_cat_eaten / food_eaten) * 100

print(f"Total eaten biscuits: {percent_cookies}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog_food_eaten:.2f}% eaten from the dog.")
print(f"{percent_cat_food_eaten:.2f}% eaten from the cat.")