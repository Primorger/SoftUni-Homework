import re

command = input()
pattern = r"([\*\^]+)([A-Za-z ]{6,})([\*\^]+)([^A-Za-z0-9]*)(\+[+-]?)(\d+\.?\d*),([+-]?\d+\.?\d*)(\++)"

matches = re.finditer(pattern, command)
matches_check = list(re.finditer(pattern, command))

if not matches_check:
    print("No valid artifacts found.")
    exit()

for match in matches:
    artifact = match.group(2)
    lat = float(match.group(5) + match.group(6))
    lon = float(match.group(7))

    print(f"Found {artifact} at coordinates {lat},{lon}.")