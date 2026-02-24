import re

all_matches = []
pattern = r"\d+"
line = input()
while line:
    matches = re.findall(pattern, line)
    if matches:
        all_matches += matches
    line = input()

print(" ".join(all_matches))