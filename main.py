import tkinter as tk
import time
from tkinter import ttk, messagebox
from backend import generate_password, save_password, view_saved_passwords

# Function to simulate loading
def show_loading_screen():
    # ... (Same as before)

def show_main_ui():
    main_window = tk.Tk()
    main_window.title("SelfCrypt")

    # Function to generate and save password
    def generate_and_save_password():
        password = generate_password()
        password_entry.delete(0, tk.END)  # Clear the entry field
        password_entry.insert(0, password)  # Show generated password

        keep_password = messagebox.askyesno("Keep Password", "Do you want to keep this password?")
        if keep_password:
            username = username_entry.get()
            url = url_entry.get()
            save_password(username, url, password)
            messagebox.showinfo("Success", "Password saved successfully!")
        else:
            messagebox.showinfo("Discarded", "Password discarded.")

    # Function to view saved passwords
    def view_passwords():
        passwords = view_saved_passwords()
        if passwords:
            saved_passwords_window = tk.Toplevel(main_window)
            saved_passwords_window.title("Saved Passwords")
            
            for url, data in passwords.items():
                tk.Label(saved_passwords_window, text=f"Website: {url} | Username: {data['username']}").pack()
        else:
            messagebox.showinfo("No Passwords", "No saved passwords found.")

    # UI Components
    tk.Label(main_window, text="Generated Password:").pack(pady=10)
    password_entry = tk.Entry(main_window, width=50)
    password_entry.pack(pady=5)

    tk.Label(main_window, text="Username:").pack(pady=10)
    username_entry = tk.Entry(main_window, width=50)
    username_entry.pack(pady=5)

    tk.Label(main_window, text="Website URL:").pack(pady=10)
    url_entry = tk.Entry(main_window, width=50)
    url_entry.pack(pady=5)

    generate_button = tk.Button(main_window, text="Generate and Save Password", command=generate_and_save_password)
    generate_button.pack(pady=20)

    view_button = tk.Button(main_window, text="View Saved Passwords", command=view_passwords)
    view_button.pack(pady=20)

    main_window.mainloop()

# Start the application
if __name__ == "__main__":
    show_loading_screen()
