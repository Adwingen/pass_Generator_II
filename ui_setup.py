# modulo ui_setup.py
from tkinter import *
from tkinter import messagebox
import json

class UI_Setup:
    def __init__(self, password_manager):
        self.password_manager = password_manager
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)
        self.window.resizable(False, False)

        # Canvas
        self.canvas = Canvas(width=200, height=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(column=1, row=0, columnspan=3)

        # Website
        self.label_website = Label(text="Website: ", font=("Courier", 8))
        self.label_website.grid(column=0, row=1, sticky="e")
        self.input_website = Entry(width=35)
        self.input_website.grid(column=1, row=1, sticky="w")
        self.input_website.focus()

        # Email/Username
        self.label_email_username = Label(text="Email/Username: ", font=("Courier", 8))
        self.label_email_username.grid(column=0, row=2, sticky="e")
        self.input_email_username = Entry(width=35)
        self.input_email_username.grid(column=1, row=2, sticky="w", columnspan=2)
        self.input_email_username.insert(0, "carlosmiguelromao@gmail.com")

        # Password
        self.label_password = Label(text="Password: ", font=("Courier", 8))
        self.label_password.grid(column=0, row=3, sticky="e")
        self.input_password = Entry(width=35)
        self.input_password.grid(column=1, row=3, sticky="w", columnspan=2)

        # Generate Password Button
        self.button_generate = Button(text="Generate Password", command=self.generate_password, font=("Courier", 8))
        self.button_generate.grid(column=2, row=3, stick="e")

        # Save Button
        self.button_add = Button(text="Add", width=29, command=self.save_password, font=("Courier", 8))
        self.button_add.grid(column=1, row=5, stick="w")

        # Search Button
        self.button_search = Button(text="Search", width=15, font=("Courier", 8), command=self.find_password)
        self.button_search.grid(column=2, row=1)

    def generate_password(self):
        password = self.password_manager.generate_password()
        self.input_password.delete(0, END)
        self.input_password.insert(0, password)

    def save_password(self):
        website = self.input_website.get()
        email_username = self.input_email_username.get()
        password = self.input_password.get()

        new_data = {
            website: {
                "email": email_username,
                "password": password
            }
        }

        if not website or not password or not email_username:
            messagebox.showinfo(title="Error", message="Please fill out all fields.")
            return

        is_ok = messagebox.askokcancel(title="Please confirm", message=f"Is the data correct? \nWebsite: {website}\n"
                                                                       f"Email/Username: {email_username}\n"
                                                                       f"Password: {password}")
        if not is_ok:
            return

        try:
            with open("data.json", "r") as data_file:
                # load the data
                data = json.load(data_file)
                # update de data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # write the new data
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # write the new data
                json.dump(data, data_file, indent=4)

            messagebox.showinfo(title="Success", message="Data saved successfully!")

        finally:
            self.input_website.delete(0, END)
            self.input_password.delete(0, END)

    def find_password(self):
        website = self.input_website.get()

        if not website:
            messagebox.showinfo(title="Error", message="Please enter a website to search for.")
            return

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data found.")
        else:
            if website in data:
                info = data[website]
                messagebox.showinfo(title=website, message=f"Email/Username: {info['email']}\nPassword: {info['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"No entry found for {website}.")



