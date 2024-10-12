import bcrypt
import random
import string
import json
import os

# File to store saved passwords
PASSWORD_FILE = 'passwords.json'

# Function to generate a random password
def generate_password(length=100):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to save a password with associated username and URL
def save_password(username, url, password):
    # Load existing passwords
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as f:
            passwords = json.load(f)
    else:
        passwords = {}

    # Add the new password
    passwords[url] = {
        'username': username,
        'password': bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')  # Hash the password
    }

    # Save updated passwords to the file
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f)

# Function to view saved passwords
def view_saved_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as f:
            passwords = json.load(f)
        return passwords
    else:
        return {}

# Example of usage
if __name__ == "__main__":
    # Generate a password
    password = generate_password()
    print(f"Generated Password: {password}")

    # Ask user if they want to keep the password
    keep_password = input("Do you want to keep this password? (yes/no): ")
    if keep_password.lower() == 'yes':
        username = input("Enter the username: ")
        url = input("Enter the website URL: ")
        save_password(username, url, password)
        print("Password saved successfully!")
    else:
        print("Password discarded.")
