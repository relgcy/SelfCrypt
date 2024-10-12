import tkinter as tk
import time
from tkinter import ttk, messagebox
from backend import generate_password, save_password, view_saved_passwords

# Function to simulate loading
def show_loading_screen():
    # Create a loading window
    loading_window = tk.Tk()
    loading_window.title("Loading")
    
    # Set window size
    loading_window.geometry("400x300")
    loading_window.configure(bg="#1a1a1a")  # Dark background

    logo_image = tk.PhotoImage(file="favicon.png")  # Load your logo here
    logo_label = tk.Label(loading_window, image=logo_image, bg="#1a1a1a")
    logo_label.pack(pady=20)

    loading_label = tk.Label(loading_window, text="Loading, please wait...", font=("Helvetica", 16), bg="#1a1a1a", fg="#ffffff")
    loading_label.pack(pady=20)

    # Create a loading spinner
    spinner = ttk.Progressbar(loading_window, mode='indeterminate', length=200)
    spinner.pack(pady=20)
    spinner.start()  # Start the spinner

    # Simulate loading time
    for _ in range(3):
        loading_window.update()
        time.sleep(1)

    spinner.stop()  # Stop the spinner
    loading_window.destroy()  # Close the loading window
    show_main_ui()  # Call the main UI function

def show_main_ui():
    main_window = tk.Tk()
    main_window.title("SelfCrypt")

    # Set window to full screen but in a windowed mode
    main_window.attributes('-fullscreen', True)  # Full-screen windowed mode
    main_window.geometry("800x600")  # Set default size (optional)

    # Dark background for main UI
    main_window.configure(bg="#2e2e2e")  

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
            saved_passwords_window.configure(bg="#2e2e2e")

            for url, data in passwords.items():
                tk.Label(saved_passwords_window, text=f"Website: {url} | Username: {data['username']} | Password: {data['password']}", bg="#2e2e2e", fg="#ffffff").pack(pady=5)
        else:
            messagebox.showinfo("No Passwords", "No saved passwords found.")

    # UI Components
    tk.Label(main_window, text="Generated Password:", bg="#2e2e2e", fg="#ffffff", font=("Helvetica", 12)).pack(pady=10)

    password_entry = tk.Entry(main_window, width=50, font=("Helvetica", 12), bg="#ffffff", fg="#000000", borderwidth=2, relief="rounded")
    password_entry.pack(pady=10)

    username_entry = tk.Entry(main_window, width=50, font=("Helvetica", 12), bg="#ffffff", fg="#000000", borderwidth=2, relief="rounded")
    username_entry.pack(pady=10)
    username_entry.insert(0, "Username")

    url_entry = tk.Entry(main_window, width=50, font=("Helvetica", 12), bg="#ffffff", fg="#000000", borderwidth=2, relief="rounded")
    url_entry.pack(pady=10)
    url_entry.insert(0, "Website URL")

    generate_button = tk.Button(main_window, text="Generate and Save Password", command=generate_and_save_password, font=("Helvetica", 12), bg="#ffffff", fg="#000000", borderwidth=2, relief="raised")
    generate_button.pack(pady=20)

    view_button = tk.Button(main_window, text="View Saved Passwords", command=view_passwords, font=("Helvetica", 12), bg="#ffffff", fg="#000000", borderwidth=2, relief="raised")
    view_button.pack(pady=20)

    main_window.mainloop()

# Show the loading screen when the app starts
show_loading_screen()
