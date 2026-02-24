import re

words_str = input()
pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
mirror_words = []
matches = re.findall(pattern, words_str)
for match in matches:
    word_1 = match[1]
    word_2 = match[2]
    if word_1 == word_2[::-1]:
        mirror_words.append(f"{word_1} <=> {word_2}")

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))