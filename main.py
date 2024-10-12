import tkinter as tk
from tkinter import messagebox
import time

# Function to create a splash screen
def show_splash_screen():
    splash = tk.Tk()
    splash.title("SelfCrypt")
    splash.geometry("300x200")
    splash.configure(bg='black')

    logo = tk.PhotoImage(file='favicon.png')  # Make sure to have the logo file in the same directory
    logo_label = tk.Label(splash, image=logo, bg='black')
    logo_label.pack(pady=20)

    # Display the splash screen for 3 seconds
    splash.after(3000, splash.destroy)
    splash.mainloop()

# Function to create the welcome screen
def show_welcome_screen():
    welcome_window = tk.Tk()
    welcome_window.title("Welcome to SelfCrypt")
    welcome_window.geometry("400x300")
    welcome_window.configure(bg='black')

    welcome_label = tk.Label(welcome_window, text="Welcome to SelfCrypt", font=("Helvetica", 16), fg='white', bg='black')
    welcome_label.pack(pady=20)

    generate_button = tk.Button(welcome_window, text="Generate Password", command=generate_password, fg='black')
    generate_button.pack(pady=10)

    view_button = tk.Button(welcome_window, text="View Stored Passwords", command=view_passwords, fg='black')
    view_button.pack(pady=10)

    welcome_window.mainloop()

def generate_password():
    # Placeholder function for password generation
    messagebox.showinfo("Generate Password", "Password generation feature coming soon!")

def view_passwords():
    # Placeholder function for viewing stored passwords
    messagebox.showinfo("View Passwords", "View stored passwords feature coming soon!")

# Main function to run the application
if __name__ == "__main__":
    show_splash_screen()
    show_welcome_screen()
