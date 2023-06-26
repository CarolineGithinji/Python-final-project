import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("User Interface")
root.geometry("400x300")
root.config(bg="lightgray")

# Function to handle button click event
def handle_button_click():
    name = entry_name.get()
    email = entry_email.get()

    if not name or not email:
        messagebox.showerror("Error", "Please enter your name and email.")
        return

    messagebox.showinfo("Success", f"Welcome, {name}! Your email is {email}.")

    # Clear the entry fields
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Name label and entry field
label_name = tk.Label(root, text="Name:", bg="lightgray", fg="black", font=("Arial", 12))
label_name.pack()
entry_name = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
entry_name.pack()

# Email label and entry field
label_email = tk.Label(root, text="Email:", bg="lightgray", fg="black", font=("Arial", 12))
label_email.pack()
entry_email = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
entry_email.pack()

# Submit button
btn_submit = tk.Button(root, text="Submit", command=handle_button_click, bg="lightgray", fg="black", font=("Arial", 12))
btn_submit.pack()

# Run the Tkinter event loop
root.mainloop()
