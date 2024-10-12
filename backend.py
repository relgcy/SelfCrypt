
import random
import string
import bcrypt
import sqlite3

# Function to generate a secure password
def generate_secure_password(length=100):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to encrypt a password using bcrypt
def encrypt_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Function to store the password in a SQLite database
def store_password(hashed_password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            password BLOB NOT NULL
        )
    ''')
    
    # Insert hashed password
    cursor.execute('INSERT INTO passwords (password) VALUES (?)', (hashed_password,))
    conn.commit()
    conn.close()

# Function to retrieve all stored passwords (for demonstration)
def get_stored_passwords():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM passwords')
    passwords = cursor.fetchall()
    conn.close()
    return passwords
