shelf = input().split("&")

while True:
    answer = input().split(" | ")

    if answer[0] == "Done":
        break

    elif answer[0] == "Add Book":
        command, book_name = answer
        if book_name in shelf:
            continue
        shelf.insert(0, book_name)
    elif answer[0] == "Take Book":
        command, book_name = answer
        if not book_name in shelf:
            continue
        shelf.remove(book_name)
    elif answer[0] == "Swap Books":
        command, book_1, book_2 = answer
        if not book_1 in shelf or not book_2 in shelf:
            continue
        book_1_index = shelf.index(book_1)
        book_2_index = shelf.index(book_2)
        shelf[book_1_index], shelf[book_2_index] = shelf[book_2_index], shelf[book_1_index]
    elif answer[0] == "Insert Book":
        command, book_name = answer
        if book_name in shelf:
            continue
        shelf.append(book_name)
    elif answer[0] == "Check Book":
        command, index = answer
        index = int(index)
        if index > len(shelf) - 1 or index < 0:
            continue
        print(shelf[index])

print(", ".join(shelf))