length = int(input())
wight = int(input())
height = int(input())
prosentage = float(input())

volume_of_aquarium =  length * wight * height
volume_in_litres = volume_of_aquarium / 1000
consumed_space = prosentage / 100
needed_litres = volume_in_litres * (1 - consumed_space)

print(needed_litres)