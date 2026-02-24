# Write a program that reads different floating-point numbers from the console. When it receives a number between
# 1 and 100 inclusive, the program should stop reading and should print "The number {number} is between 1
# and 100".
num = 0

while num < 1 or num > 100:
    num = float(input())

print(f"The number {num} is between 1 and 100")