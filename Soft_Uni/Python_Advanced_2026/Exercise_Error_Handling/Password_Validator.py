class PasswordTooShortError(Exception):
    pass
class PasswordTooCommonError(Exception):
    pass
class PasswordNoSpecialCharactersError(Exception):
    pass
class PasswordContainsSpacesError(Exception):
    pass

SPLECIAL_CHARACTERS = {"@", "*", "&", "%"}

def password_too_common(password, specials):
    only_digits = password.isdigit()
    only_letters = password.isalpha()
    only_specials = all(char in specials for char in password)
    return only_digits or only_letters or only_specials

while True:
    command = input()
    if command == "Done":
        break

    if len(command) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    
    if password_too_common(command, SPLECIAL_CHARACTERS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    
    if not any(char in SPLECIAL_CHARACTERS for char in command):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    
    if " " in command:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    
    print("Password is valid")