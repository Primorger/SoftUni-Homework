import re

pattern = "(www\.[a-z0-9\-]+(\.[a-z]+)+)"
line = input()
while line:
    match = re.search(pattern, line, re.IGNORECASE)
    if match:
        url = match.group(1)
        print(url)
    line = input()
