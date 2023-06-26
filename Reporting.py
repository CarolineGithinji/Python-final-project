import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a database connection
conn = sqlite3.connect("library.db")
c = conn.cursor()

# Create the main application window
root = tk.Tk()
root.title("Reporting")
root.geometry("400x300")
root.config(bg="lightgray")

# Function to generate the list of available books report
def generate_available_books_report():
    c.execute("SELECT * FROM books WHERE id NOT IN (SELECT book_id FROM borrowings WHERE return_date IS NULL)")
    books = c.fetchall()

    report_text = ""
    if books:
        report_text = "Available Books:\n"
        for book in books:
            report_text += f"Title: {book[1]}\nAuthor: {book[2]}\nISBN: {book[3]}\nPublication Date: {book[4]}\n\n"
    else:
        report_text = "No available books."

    # Display the report in a message box
    messagebox.showinfo("Available Books Report", report_text)

# Function to generate the list of borrowed books report
def generate_borrowed_books_report():
    c.execute("SELECT * FROM books WHERE id IN (SELECT book_id FROM borrowings WHERE return_date IS NULL)")
    books = c.fetchall()

    report_text = ""
    if books:
        report_text = "Borrowed Books:\n"
        for book in books:
            report_text += f"Title: {book[1]}\nAuthor: {book[2]}\nISBN: {book[3]}\nPublication Date: {book[4]}\n\n"
    else:
        report_text = "No borrowed books."

    # Display the report in a message box
    messagebox.showinfo("Borrowed Books Report", report_text)

# Function to generate the list of overdue books report
def generate_overdue_books_report():
    c.execute("SELECT * FROM books WHERE id IN (SELECT book_id FROM borrowings WHERE return_date IS NULL AND due_date < DATE('now'))")
    books = c.fetchall()

    report_text = ""
    if books:
        report_text = "Overdue Books:\n"
        for book in books:
            report_text += f"Title: {book[1]}\nAuthor: {book[2]}\nISBN: {book[3]}\nPublication Date: {book[4]}\n\n"
    else:
        report_text = "No overdue books."

    # Display the report in a message box
    messagebox.showinfo("Overdue Books Report", report_text)

# Generate Available Books Report button
btn_available_books_report = tk.Button(root, text="Generate Available Books Report", command=generate_available_books_report, bg="lightgray", fg="black", font=("Arial", 12))
btn_available_books_report.pack()

# Generate Borrowed Books Report button
btn_borrowed_books_report = tk.Button(root, text="Generate Borrowed Books Report", command=generate_borrowed_books_report, bg="lightgray", fg="black", font=("Arial", 12))
btn_borrowed_books_report.pack()

# Generate Overdue Books Report button
btn_overdue_books_report = tk.Button(root, text="Generate Overdue Books Report", command=generate_overdue_books_report, bg="lightgray", fg="black", font=("Arial", 12))
btn_overdue_books_report.pack()

# Run the Tkinter event loop
root.mainloop()

# Close the database connection when the application is closed
conn.close()
