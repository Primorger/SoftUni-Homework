import re

sentance = input()
searched_str = input()
pattern = fr"\b{searched_str}\b"
matches = re.findall(pattern, sentance, re.IGNORECASE)
print(len(matches))