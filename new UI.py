import os
import tkinter as tk
from tkinter import messagebox

def save_entry(entry_name, entry_type, username, email, password, pin, name, date_of_birth, phone_number, address):
    directory = "sledger_data"
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, f"{entry_name}.txt")

    with open(file_path, 'w') as file:
        file.write(f"Name: {entry_name}\n")
        file.write(f"Type: {entry_type}\n")

        if entry_type == "account":
            file.write(f"Username: {username}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")
        elif entry_type == "pin":
            file.write(f"Pin: {pin}\n")
        elif entry_type == "person specs":
            file.write(f"Full Name: {name}\n")
            file.write(f"Date of Birth: {date_of_birth}\n")
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"Address: {address}\n")

    messagebox.showinfo("Success", f"Details saved to {file_path}")

def main():
    def on_submit():
        entry_name = entry_name_var.get()
        entry_type = entry_type_var.get().lower()

        if entry_type == "account":
            save_entry(entry_name, entry_type, username_var.get(), email_var.get(), password_var.get(), "", "", "", "", "")
        elif entry_type == "pin":
            save_entry(entry_name, entry_type, "", "", "", pin_var.get(), "", "", "", "")
        elif entry_type == "person specs":
            save_entry(entry_name, entry_type, "", "", "", "", name_var.get(), dob_var.get(), phone_var.get(), address_var.get())
        else:
            messagebox.showerror("Error", "Invalid entry type")

    root = tk.Tk()
    root.title("Sledger")

    tk.Label(root, text="Entry Name").grid(row=0, column=0)
    entry_name_var = tk.StringVar()
    tk.Entry(root, textvariable=entry_name_var).grid(row=0, column=1)

    tk.Label(root, text="Entry Type").grid(row=1, column=0)
    entry_type_var = tk.StringVar()
    tk.Entry(root, textvariable=entry_type_var).grid(row=1, column=1)

    tk.Label(root, text="Username").grid(row=2, column=0)
    username_var = tk.StringVar()
    tk.Entry(root, textvariable=username_var).grid(row=2, column=1)

    tk.Label(root, text="Email").grid(row=3, column=0)
    email_var = tk.StringVar()
    tk.Entry(root, textvariable=email_var).grid(row=3, column=1)

    tk.Label(root, text="Password").grid(row=4, column=0)
    password_var = tk.StringVar()
    tk.Entry(root, textvariable=password_var, show="*").grid(row=4, column=1)

    tk.Label(root, text="PIN").grid(row=5, column=0)
    pin_var = tk.StringVar()
    tk.Entry(root, textvariable=pin_var).grid(row=5, column=1)

    tk.Label(root, text="Full Name").grid(row=6, column=0)
    name_var = tk.StringVar()
    tk.Entry(root, textvariable=name_var).grid(row=6, column=1)

    tk.Label(root, text="Date of Birth").grid(row=7, column=0)
    dob_var = tk.StringVar()
    tk.Entry(root, textvariable=dob_var).grid(row=7, column=1)

    tk.Label(root, text="Phone Number").grid(row=8, column=0)
    phone_var = tk.StringVar()
    tk.Entry(root, textvariable=phone_var).grid(row=8, column=1)

    tk.Label(root, text="Address").grid(row=9, column=0)
    address_var = tk.StringVar()
    tk.Entry(root, textvariable=address_var).grid(row=9, column=1)

    tk.Button(root, text="Submit", command=on_submit).grid(row=10, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()