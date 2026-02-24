import re

single_str = input()
patern = fr"\s(([a-z0-9]+)([a-z0-9\.\_\-]+)([a-z0-9]+)@([a-z\-]+)(\.[a-z]+)+)\b"
emails = re.findall(patern, single_str)
for email in emails:
    print(email[0])