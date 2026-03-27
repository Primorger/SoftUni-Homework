from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger
from project.food import Vegetable, Fruit, Meat, Seed

owl = Owl("Pip", 10, 10)

print(owl)

meat = Meat(4)

print(owl.make_sound())

owl.feed(meat)

veg = Vegetable(1)

print(owl.feed(veg))

print(owl)