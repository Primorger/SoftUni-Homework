command = ""
coffees = 0

# "".isupper()   "".lower() 

wakeups = ("coding", "dog", "cat", "movie")

while command != "END":
    command = input()

    if command == "END":
        if coffees > 5:
            print("You need extra sleep")  
        else:
            print(coffees)
        break

    if command.lower() in wakeups:
        if command.isupper():
            coffees += 2
        else:
            coffees += 1

      


    