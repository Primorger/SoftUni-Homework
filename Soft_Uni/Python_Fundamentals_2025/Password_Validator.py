password = input()
letters = tuple([chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)])
digits = tuple([chr(i) for i in range(48, 58)])

def password_length(password):
    if not 6 <= len(password) <= 10:
        return "Password must be between 6 and 10 characters"
    
def password_letters_and_digits(password):
    for char in password:
        if not (char in letters or char in digits):
            return "Password must consist only of letters and digits"
        
def password_at_least_2_digits(password):
    counter = 0
    for char in password:
        if char in digits:
            counter += 1
    if counter < 2:
        return "Password must have at least 2 digits"
    

validation_errors = []

length_error = password_length(password)
if length_error:
    validation_errors.append(length_error)

letters_digits_error = password_letters_and_digits(password)
if letters_digits_error:
    validation_errors.append(letters_digits_error)

digits_error = password_at_least_2_digits(password)
if digits_error:
    validation_errors.append(digits_error)

if validation_errors:
    for error in validation_errors:
        print(error)
else:
    print("Password is valid")