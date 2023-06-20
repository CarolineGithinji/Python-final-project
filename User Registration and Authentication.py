import tkinter as tk

def enter_data():
    print("enter data")

# create the main window
root=tk.Tk()
root.title=("LIBRARY MANAGMENT SYSTEM")
message=tk.Label(root,text="WELCOME TO LIBRARY MANAGMENT SYSTEM LOGIN")
message.pack()

#set minimum and maximum size of window
root.wm_geometry("370x180")
root.wm_geometry("480x255")

# Create label for user
root.username_label= tk.Label(root,text='User-Id',bg='gray',fg='black',font=('courier_new',18,'bold'))
root.username_label.pack()
root.username_entry=tk.Entry(root)
root.username_entry.pack()

#create label for password
root.password_label=root.password_label = tk.Label(root, text='Password', bg='gray', fg='black', font=('courier_new', 18, 'bold'))
root.password_label.pack()
root.password_entry=tk.Entry(root)
root.password_entry.pack()
enter=tk.Button(root,text='Login',command=enter_data)
enter.pack()

root.mainloop()
