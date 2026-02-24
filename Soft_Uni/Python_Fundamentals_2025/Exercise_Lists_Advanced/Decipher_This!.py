messages = input().split()
deciphered_messages = []

for message in messages:
    message = list(message)
    numbers_as_str = ""
    for i in range(len(message)):
        if message[i].isdigit():
            numbers_as_str += message[i]
        else:
            break
    numbers_as_letter = chr(int(numbers_as_str))
    message = [numbers_as_letter] + message[i:]
    message[1], message[-1] = message[-1], message[1]
    deciphered_messages.append("".join(message))

print(" ".join(deciphered_messages))