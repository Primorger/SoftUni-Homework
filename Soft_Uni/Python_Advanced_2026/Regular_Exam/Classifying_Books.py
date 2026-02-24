def classify_books(*args, **kwargs):
    fiction = {}
    non_fiction = {}
    
    for genre, title in args:
        for isbn, book_title in kwargs.items():
            if book_title == title:
                if genre == "fiction":
                    fiction[isbn] = title
                elif genre == "non_fiction":
                    non_fiction[isbn] = title
                break
    
    sorted_fiction = sorted(fiction.items())
    
    sorted_non_fiction = sorted(non_fiction.items(), reverse=True)
    
    result = []
    
    if sorted_fiction:
        result.append("Fiction Books:")
        for isbn, title in sorted_fiction:
            result.append(f"~~~{isbn}#{title}")
    
    if sorted_non_fiction:
        result.append("Non-Fiction Books:")
        for isbn, title in sorted_non_fiction:
            result.append(f"***{isbn}#{title}")
    
    return "\n".join(result)

#-------------Test print-------------#

print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))