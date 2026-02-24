book_needed = input()
counter = -1
book_in_lib = ""
while book_needed != book_in_lib:
    book_in_lib = input()
    counter += 1
    if book_in_lib == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {counter} books.")
        break
else:
    print(f"You checked {counter} books and found it.")