import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a database connection
conn = sqlite3.connect("patrons.db")
c = conn.cursor()

# Create a table to store patron records
c.execute("""CREATE TABLE IF NOT EXISTS patrons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact_info TEXT,
                membership_status TEXT
            )""")
conn.commit()

# Create the main application window
root = tk.Tk()
root.title("Patron Management")
root.geometry("400x300")
root.config(bg="gray")

# Function to add a new patron record
def add_patron():
    name = entry_name.get()
    contact_info = entry_contact_info.get()
    membership_status = entry_membership_status.get()

    # Check if any field is empty
    if not name or not contact_info or not membership_status:
        messagebox.showerror("Error", "Please enter all fields.")
        return

    # Insert the new patron record into the database
    c.execute("INSERT INTO patrons (name, contact_info, membership_status) VALUES (?, ?, ?)",
              (name, contact_info, membership_status))
    conn.commit()
    messagebox.showinfo("Success", "Patron record added successfully.")

    # Clear the entry fields
    entry_name.delete(0, tk.END)
    entry_contact_info.delete(0, tk.END)
    entry_membership_status.delete(0, tk.END)

# Function to edit a patron record
def edit_patron():
    patron_id = entry_patron_id.get()
    name = entry_name.get()
    contact_info = entry_contact_info.get()
    membership_status = entry_membership_status.get()

    # Check if any field is empty
    if not patron_id or not name or not contact_info or not membership_status:
        messagebox.showerror("Error", "Please enter all fields.")
        return

    # Update the patron record in the database
    c.execute("UPDATE patrons SET name=?, contact_info=?, membership_status=? WHERE id=?",
              (name, contact_info, membership_status, patron_id))
    conn.commit()
    if c.rowcount > 0:
        messagebox.showinfo("Success", "Patron record updated successfully.")
    else:
        messagebox.showerror("Error", "Invalid patron ID.")

    # Clear the entry fields
    entry_patron_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_contact_info.delete(0, tk.END)
    entry_membership_status.delete(0, tk.END)

# Function to delete a patron record
def delete_patron():
    patron_id = entry_patron_id.get()

    # Check if the patron ID is empty
    if not patron_id:
        messagebox.showerror("Error", "Please enter a patron ID.")
        return

    # Delete the patron record from the database
    c.execute("DELETE FROM patrons WHERE id=?", (patron_id,))
    conn.commit()
    if c.rowcount > 0:
        messagebox.showinfo("Success", "Patron record deleted successfully.")
    else:
        messagebox.showerror("Error", "Invalid patron ID.")

    # Clear the entry fields
    entry_patron_id.delete(0, tk.END)

# Patron ID label and entry field
label_patron_id = tk.Label(root, text="Patron ID:", bg="lightgray", fg="black", font=("Arial", 12))
label_patron_id.pack()
entry_patron_id = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
entry_patron_id.pack()

# Name label and entry field
label_name = tk.Label(root, text="Name:", bg="lightgray", fg="black", font=("Arial", 12))
label_name.pack()
entry_name = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
entry_name.pack()

# Contact Information label and entry field
label_contact_info = tk.Label(root, text="Contact Information:", bg="lightgray", fg="black", font=("Arial", 12))
label_contact_info.pack()
entry_contact_info = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
entry_contact_info.pack()

# Membership Status label and entry field
label_membership_status = tk.Label(root, text="Membership Status:", bg="lightgray", fg="black", font=("Arial", 12))
label_membership_status.pack()
entry_membership_status = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
entry_membership_status.pack()

# Add Patron button
btn_add_patron = tk.Button(root, text="Add Patron", command=add_patron, bg="lightgray", fg="black", font=("Arial", 12))
btn_add_patron.pack()

# Edit Patron button
btn_edit_patron = tk.Button(root, text="Edit Patron", command=edit_patron, bg="lightgray", fg="black", font=("Arial", 12))
btn_edit_patron.pack()

# Delete Patron button
btn_delete_patron = tk.Button(root, text="Delete Patron", command=delete_patron, bg="lightgray", fg="black", font=("Arial", 12))
btn_delete_patron.pack()

# Run the Tkinter event loop
root.mainloop()

# Close the database connection when the application is closed
conn.close()
