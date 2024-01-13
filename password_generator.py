# Import the required libraries
import random
import string

TITLE_MESSAGE = "RUNNING PASSWORD GENERATOR TOOL"

def generate_random_password(pwd_length: int, include_letters: bool, include_numbers: bool, include_special_chars: bool):
    """
    Generate n digit length ramdom password

    :param pwd_length: length of the password
    :param include_letters: Whether to include letters in the password or not
    :param include_numbers: Whether to include numbers in the password or not
    :param include_special_chars: Whether to include special characters in the password or not
    :return: string containing the generated password
    """
    print('=' * 40 + f' {TITLE_MESSAGE} ' + '=' * 40)
    # Collect letters, numbers and special characters in individual variables
    english_letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation

    # Collect all letters, numbers and special characters in a string variable (based on function arguments)
    pwd_allowed_characters = ''
    if include_letters: pwd_allowed_characters = english_letters
    if include_numbers: pwd_allowed_characters = pwd_allowed_characters + numbers
    if include_special_chars: pwd_allowed_characters = pwd_allowed_characters + special_characters

    # Generate a password containing random letters, numbers special characters (based on applicability)
    has_letters = False
    has_digits = False
    has_special_chars = False
    generated_password = ''

    while len(generated_password) < pwd_length or include_letters != has_letters or include_numbers != has_digits \
            or include_special_chars != has_special_chars:
        new_char = random.choice(pwd_allowed_characters)
        generated_password += new_char
        if new_char in english_letters: has_letters = True
        if new_char in numbers: has_digits = True
        if new_char in special_characters: has_special_chars = True

    print('Password has been generated!')
    print(f'> Randomly generated password: {generated_password}')

    return generated_password


# Name-Main idiom to run it as a main script
if __name__ == "__main__":
    # Get the required input from the user
    pwd_length = int(input("Please provide length of the password: "))
    include_letters = input("Should password contain letters (y/n): ").lower() == 'y'
    include_numbers = input("Should password contain numbers (y/n): ").lower() == 'y'
    include_special_chars = input("Should password contain special characters (y/n): ").lower() == 'y'
    # Run the password generator function
    generate_random_password(pwd_length, include_letters, include_numbers, include_special_chars)
