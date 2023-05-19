from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_number = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        finally:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ----------------------------- Search -------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except(FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title="Oops", message="No Data file found.")
    else:
        if data.get(website):
            messagebox.showinfo(title="your key", message=f" Email: {data[website]['email']} \n"
                                                          f" Password: {data.get(website)['password']}")
        else:
            messagebox.showinfo(title="Oops", message="No entry found for this website")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)
# website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# Email Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
# password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entry Website
website_entry = Entry(width=18)  # 35
website_entry.grid(column=1, row=1)
website_entry.focus()
# email Entry
email_entry = Entry(width=34)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@gmail.com")
# password Entry
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

# Generate Password Button
password_button = Button(text="Generate Password", width=12, command=generate_password)
password_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=13, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Add search button
search_button = Button(text="Search", width=12, command=search)
search_button.grid(column=2, row=1)
window.mainloop()
