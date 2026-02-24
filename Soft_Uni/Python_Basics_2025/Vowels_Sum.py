word = input()
score = 0
for char in range(len(word)):
    if word[char] == "a":
        score += 1
    elif word[char] == "e":
        score += 2
    elif word[char] == "i":
        score += 3
    elif word[char] == "o":
        score += 4
    elif word[char] == "u":
        score += 5
    
print(score)

