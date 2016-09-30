"""
@author: Maxim Kravchenko
"""

import os
import string


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def get_number_number_of_special_characters(list_of_letters):
    special_sings_count = 0
    for char in list_of_letters:
        if char in string.punctuation or char == ' ':
            special_sings_count += 1

    if special_sings_count >= 3:
        return 3
    elif 3 > special_sings_count > 0:
        return 2
    else:
        return 0


def is_pass_contains_ascii_letters(list_of_letters):
    for char in list_of_letters:
        if char in string.ascii_letters:
            return True
    return False


def is_pass_contains_ascii_lowercase(list_of_letters):
    for char in list_of_letters:
        if char in string.ascii_lowercase:
            return True
    return False


def is_pass_contains_ascii_uppercase(list_of_letters):
    for char in list_of_letters:
        if char in string.ascii_uppercase:
            return True
    return False


def is_pass_contains_digits(list_of_letters):
    for char in list_of_letters:
        if char in string.digits:
            return True
    return False


def get_password_strength(password, most_used_passwords):
    password_strength_count = 0
    list_most_used_passwords = [password_to_list for password_to_list in most_used_passwords.split()]

    if password in list_most_used_passwords:
        return 0

    list_of_sings = [sign for sign in password]

    if len(list_of_sings) <= 3:
        return 1

    elif len(list_of_sings) >= 8:
        password_strength_count += 1
        if len(list_of_sings) >= 15:
            password_strength_count += 1
        if len(list_of_sings) >= 15:
            password_strength_count += 1
        if is_pass_contains_ascii_letters(list_of_sings):
            password_strength_count += 1
        if is_pass_contains_ascii_lowercase(list_of_sings):
            password_strength_count += 1
        if is_pass_contains_ascii_uppercase(list_of_sings):
            password_strength_count += 1
        if is_pass_contains_digits(list_of_sings):
            password_strength_count += 1

        password_strength_count += get_number_number_of_special_characters(list_of_sings)
    else:
        return 2
    return password_strength_count


def print_password_stregth(password_strength_count):
    print("The password strength is: {}".format(password_strength_count))


if __name__ == '__main__':
    path_to_file = input("Enter path to file with list of most used passwords: ")
    load_data(path_to_file)
    most_used_passwords = load_data(path_to_file)
    while True:
        password = input("Enter the password: ")
        if not password:
            break
        password_strength = get_password_strength(password, most_used_passwords)
        print_password_stregth(password_strength)
