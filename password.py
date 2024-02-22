import random
import string

def generate_password():
    while True:
        password = input("Enter a password (at least 8 characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character): ")
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        if not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter.")
            continue
        if not any(char.islower() for char in password):
            print("Password must contain at least one lowercase letter.")
            continue
        if not any(char.isdigit() for char in password):
            print("Password must contain at least one digit.")
            continue
        if not any(char in string.punctuation for char in password):
            print("Password must contain at least one special character.")
            continue
        return password

if __name__ == "__main__":
    password = generate_password()
    print("Generated password:", password)
