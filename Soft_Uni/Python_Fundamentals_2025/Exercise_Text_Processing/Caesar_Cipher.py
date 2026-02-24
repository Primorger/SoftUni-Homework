input_str = input()
shift = 3
encrypted_str = ""

for char in input_str:
    encrypted_char = chr(ord(char) + shift)
    encrypted_str += encrypted_char
    
print(encrypted_str)