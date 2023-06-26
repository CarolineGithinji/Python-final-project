import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import date, timedelta

# Create a database connection
conn = sqlite3.connect("library.db")
c = conn.cursor()

# Create a table to store book records
c.execute("""CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                isbn TEXT,
                publication_date TEXT
            )""")
conn.commit()

# Create a table to store patron records
c.execute("""CREATE TABLE IF NOT EXISTS patrons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact_info TEXT,
                membership_status TEXT
            )""")
conn.commit()

# Create a table to store borrowing records
c.execute("""CREATE TABLE IF NOT EXISTS borrowings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                patron_id INTEGER,
                borrow_date TEXT,
                due_date TEXT,
                return_date TEXT
            )""")
conn.commit()

# Create the main application window
root = tk.Tk()
root.title("Borrowing System")
root.geometry("400x300")
root.config(bg="lightgray")

# Function to handle book check-out
def check_out_book():
    book_id = entry_book_id.get()
    patron_id = entry_patron_id.get()
    borrow_date = date.today().strftime("%Y-%m-%d")
    due_date = (date.today() + timedelta(days=14)).strftime("%Y-%m-%d")  # Due date is set to 14 days from the borrow date

    # Check if any field is empty
    if not book_id or not patron_id:
        messagebox.showerror("Error", "Please enter all fields.")
        return

    # Check if the book and patron exist in the database
    c.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = c.fetchone()
    c.execute("SELECT * FROM patrons WHERE id=?", (patron_id,))
    patron = c.fetchone()

    if not book or not patron:
        messagebox.showerror("Error", "Invalid book ID or patron ID.")
        return

    # Check if the book is already checked out
    c.execute("SELECT * FROM borrowings WHERE book_id=? AND return_date IS NULL", (book_id,))
    existing_borrowing = c.fetchone()

    if existing_borrowing:
        messagebox.showerror("Error", "The book is already checked out.")
        return

    # Insert the borrowing record into the database
    c.execute("INSERT INTO borrowings (book_id, patron_id, borrow_date, due_date) VALUES (?, ?, ?, ?)",
              (book_id, patron_id, borrow_date, due_date))
    conn.commit()
    messagebox.showinfo("Success", "Book checked out successfully.")

    # Clear the entry fields
    entry_book_id.delete(0, tk.END)
    entry_patron_id.delete(0, tk.END)

# Function to handle book check-in
def check_in_book():
    book_id = entry_book_id.get()

    # Check if the book ID is empty
    if not book_id:
        messagebox.showerror("Error", "Please enter a book ID.")
        return

    # Check if the book exists in the database
    c.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = c.fetchone()

    if not book:
        messagebox.showerror("Error", "Invalid book ID.")
        return

    # Check if the book is currently checked out
    c.execute("SELECT * FROM borrowings WHERE book_id=? AND return_date IS NULL", (book_id,))
    borrowing = c.fetchone()

    if not borrowing:
        messagebox.showerror("Error", "The book is not checked out.")
        return

    # Update the borrowing record in the database
    return_date = date.today().strftime("%Y-%m-%d")
    c.execute("UPDATE borrowings SET return_date=? WHERE id=?", (return_date, borrowing[0]))
    conn.commit()
    messagebox.showinfo("Success", "Book checked in successfully.")

    # Clear the entry fields
    entry_book_id.delete(0, tk.END)

# Book ID label and entry field
label_book_id = tk.Label(root, text="Book ID:", bg="lightgray", fg="black", font=("Arial", 12))
label_book_id.pack()
entry_book_id = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
entry_book_id.pack()

# Patron ID label and entry field
label_patron_id = tk.Label(root, text="Patron ID:", bg="lightgray", fg="black", font=("Arial", 12))
label_patron_id.pack()
entry_patron_id = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
entry_patron_id.pack()

# Check Out Book button
btn_check_out_book = tk.Button(root, text="Check Out Book", command=check_out_book, bg="lightgray", fg="black", font=("Arial", 12))
btn_check_out_book.pack()

# Check In Book button
btn_check_in_book = tk.Button(root, text="Check In Book", command=check_in_book, bg="lightgray", fg="black", font=("Arial", 12))
btn_check_in_book.pack()

# Run the Tkinter event loop
root.mainloop()

# Close the database connection when the application is closed
conn.close()
